#!/usr/bin/env python3
"""Prepare the input for the Codex pull request review and publish its findings.

Used by .github/workflows/pr-review.yml:

  python scripts/codex_review.py prepare --base <ref> --event <event.json> --out .codex-run
  python scripts/codex_review.py publish --review codex-output.json --lines added-lines.json \
      --pr <number> --head <sha> [--result success] [--dry-run]

``prepare`` writes the diff, the changed files, the pull request metadata, and
the added line numbers per file.

``publish`` posts the findings on lines the pull request added as one review
with inline comments, and keeps a single summary comment up to date. Inline
comments from earlier runs are hidden as outdated so each push shows only the
latest review. It needs GITHUB_TOKEN and GITHUB_REPOSITORY.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from github_api import GitHub  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
MARKER = "<!-- codex-pr-review -->"
SUMMARY_MARKER = "<!-- codex-pr-review-summary -->"
HUNK_RE = re.compile(r"^@@ -\S+ \+(\d+)(?:,(\d+))? @@")
SEVERITY_ICONS = {"high": "🔴", "medium": "🟠", "low": "🟡"}


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True, encoding="utf-8", cwd=REPO_ROOT,
    ).stdout


def added_lines(diff: str) -> dict[str, list[int]]:
    result: dict[str, list[int]] = {}
    path = None
    for line in diff.splitlines():
        if line.startswith("+++ "):
            path = line[6:] if line.startswith("+++ b/") else None
        elif path and (hunk := HUNK_RE.match(line)):
            start, count = int(hunk.group(1)), int(hunk.group(2) or 1)
            result.setdefault(path, []).extend(range(start, start + count))
    return result


def cmd_prepare(args) -> int:
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    merge_base = git("merge-base", args.base, "HEAD").strip()
    scope = [merge_base, "HEAD", "--find-renames", "--", "docs/"]
    (out / "pr.diff").write_text(git("diff", *scope), encoding="utf-8")
    (out / "changed-files.txt").write_text(git("diff", "--name-status", *scope), encoding="utf-8")
    lines = added_lines(git("diff", "--unified=0", "--no-color", *scope))
    (out / "added-lines.json").write_text(json.dumps(lines, indent=2), encoding="utf-8")
    event = json.loads(Path(args.event).read_text(encoding="utf-8"))
    pull_request = event["pull_request"]
    metadata = {
        "number": pull_request["number"],
        "title": pull_request["title"],
        "description": pull_request.get("body") or "",
        "author": pull_request["user"]["login"],
        "base_commit": merge_base,
        "head_commit": git("rev-parse", "HEAD").strip(),
    }
    (out / "pr.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"{len(lines)} changed file(s) with added lines")
    return 0


def comment_body(finding: dict) -> str:
    icon = SEVERITY_ICONS.get(finding["severity"], "")
    body = f"{icon} **{finding['severity']} · {finding['category']}**: {finding['problem']}"
    if finding["suggestion"]:
        body += f"\n\n{finding['suggestion']}"
    if finding["replacement_line"]:
        body += f"\n\n```suggestion\n{finding['replacement_line']}\n```"
    return f"{body}\n\n{MARKER}"


def summary_body(review: dict | None, inline: list[dict], other: list[dict], head: str, run_url: str) -> str:
    lines = [SUMMARY_MARKER, "## Codex review", ""]
    if review is None:
        lines += [f"The review did not finish for `{head[:7]}`. See the [workflow run]({run_url})."]
        return "\n".join(lines)
    lines += [review["summary"], ""]
    findings = inline + other
    if findings:
        counts = ", ".join(
            f"{SEVERITY_ICONS[s]} {s}: {n}"
            for s in ("high", "medium", "low")
            if (n := sum(f["severity"] == s for f in findings))
        )
        lines += [f"**{len(findings)} finding(s)** ({counts}); {len(inline)} posted as inline comments.", ""]
    if other:
        lines += ["Findings outside the changed lines:", "", "| Severity | Location | Problem | Suggestion |", "|---|---|---|---|"]
        for f in other:
            cells = [f["severity"], f"`{f['path']}:{f['line']}`", f["problem"], f["suggestion"]]
            lines.append("| " + " | ".join(c.replace("|", "\\|").replace("\n", " ") for c in cells) + " |")
        lines.append("")
    lines.append(f"<sub>Commit `{head[:7]}` · [workflow run]({run_url}) · Report-only; it does not block merging.</sub>")
    return "\n".join(lines)


def cmd_publish(args) -> int:
    review = None
    if args.result == "success" and Path(args.review).is_file():
        try:
            review = json.loads(Path(args.review).read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            print(f"::warning::Codex output is not valid JSON: {error}")
    lines = json.loads(Path(args.lines).read_text(encoding="utf-8")) if Path(args.lines).is_file() else {}
    findings = review["findings"] if review else []
    inline = [f for f in findings if f["line"] in lines.get(f["path"], ())]
    other = [f for f in findings if f not in inline]

    server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
    run_url = f"{server}/{os.environ.get('GITHUB_REPOSITORY', '')}/actions/runs/{os.environ.get('GITHUB_RUN_ID', '')}"
    summary = summary_body(review, inline, other, args.head, run_url)
    comments = [
        {"path": f["path"], "line": f["line"], "side": "RIGHT", "body": comment_body(f)} for f in inline
    ]
    if args.dry_run:
        print(summary)
        print(json.dumps(comments, indent=2, ensure_ascii=False))
        return 0

    github = GitHub(os.environ["GITHUB_REPOSITORY"], os.environ["GITHUB_TOKEN"])
    pr = args.pr
    # Hide the inline comments of earlier runs; the new review replaces them.
    for old in github.paged(f"pulls/{pr}/comments"):
        if MARKER in old["body"] and old["user"]["login"] == "github-actions[bot]":
            github.graphql(
                "mutation($id: ID!) { minimizeComment(input: {subjectId: $id, classifier: OUTDATED}) "
                "{ minimizedComment { isMinimized } } }",
                {"id": old["node_id"]},
            )
    if comments:
        github.request("POST", f"pulls/{pr}/reviews", {
            "commit_id": args.head,
            "event": "COMMENT",
            "body": f"Codex found {len(comments)} problem(s) on the changed lines. {MARKER}",
            "comments": comments,
        })
    existing = next(
        (c for c in github.paged(f"issues/{pr}/comments")
         if SUMMARY_MARKER in c["body"] and c["user"]["login"] == "github-actions[bot]"),
        None,
    )
    if existing:
        github.request("PATCH", f"issues/comments/{existing['id']}", {"body": summary})
    else:
        github.request("POST", f"issues/{pr}/comments", {"body": summary})
    print(f"Published {len(comments)} inline comment(s) and {len(other)} summary finding(s).")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Codex pull request review helper.")
    commands = parser.add_subparsers(dest="command", required=True)
    prepare = commands.add_parser("prepare", help="write the review input")
    prepare.add_argument("--base", required=True, help="base branch ref, e.g. origin/master")
    prepare.add_argument("--event", required=True, help="GitHub event payload (GITHUB_EVENT_PATH)")
    prepare.add_argument("--out", required=True, help="output directory")
    publish = commands.add_parser("publish", help="post the review on the pull request")
    publish.add_argument("--review", required=True, help="Codex output JSON")
    publish.add_argument("--lines", required=True, help="added-lines.json from prepare")
    publish.add_argument("--pr", required=True, type=int)
    publish.add_argument("--head", required=True, help="head commit SHA")
    publish.add_argument("--result", default="success", help="result of the review job")
    publish.add_argument("--dry-run", action="store_true", help="print instead of posting")
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    return cmd_prepare(args) if args.command == "prepare" else cmd_publish(args)


if __name__ == "__main__":
    sys.exit(main())
