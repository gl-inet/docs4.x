#!/usr/bin/env python3
"""Prepare a docs diff and publish validated Codex findings using trusted tooling.

Only stdlib dependencies. --repo is an untrusted, data-only checkout; never
import from it or execute its scripts. Publish recomputes lines, not artifacts.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from github_api import GitHub

MARKER = "<!-- codex-pr-review -->"
SUMMARY_MARKER = "<!-- codex-pr-review-summary -->"
CATEGORIES = {"accuracy", "copy-paste", "link", "image", "grammar", "spelling",
              "terminology", "ui-label", "structure", "translation", "other"}
SHA = re.compile(r"[0-9a-f]{40}")
HUNK = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")


def safe_path(path):
    if (not isinstance(path, str) or len(path) > 500 or not path.startswith("docs/")
            or "\\" in path or any(ord(c) < 32 or ord(c) == 127 for c in path)
            or any(p in ("", ".", "..") for p in path.split("/"))):
        raise ValueError("Unsafe documentation path")
    return path


def git(repo, *args):
    return subprocess.run(
        ["git", "-c", "core.quotePath=false", "-C", str(repo), *args],
        check=True, capture_output=True, text=True, encoding="utf-8",
    ).stdout


def added_lines(diff):
    result, path, number, in_hunk = {}, None, 0, False
    for line in diff.splitlines():
        if line.startswith("diff --git "):
            path, in_hunk = None, False
        elif not in_hunk and line.startswith("+++ b/"):
            path = safe_path(line[6:])
        elif hunk := HUNK.match(line):
            number, in_hunk = int(hunk.group(1)), True
        elif in_hunk and path:
            if line.startswith("+"):
                result.setdefault(path, []).append(number)
                number += 1
            elif line.startswith(" "):
                number += 1
    return result


def diff_input(repo, base, head):
    if not SHA.fullmatch(base) or not SHA.fullmatch(head):
        raise ValueError("Expected full commit SHAs")
    if git(repo, "rev-parse", "HEAD").strip() != head:
        raise ValueError("Data checkout does not match expected head")
    merge_base = git(repo, "merge-base", base, head).strip()
    scope = (merge_base, head, "--", "docs/")
    options = ("--no-ext-diff", "--no-textconv", "--no-renames", "--no-color")
    # Reject ambiguous quoted names instead of trying to interpret git C escapes.
    names = git(repo, "diff", "--name-only", "-z", *options, *scope)
    for path in names.split("\0"):
        if path:
            safe_path(path)
    diff = git(repo, "diff", "--unified=0", *options, *scope)
    lines = added_lines(diff)
    # Symlink targets are not documentation text eligible for suggestions.
    regular = set()
    for entry in git(repo, "ls-tree", "-r", "-z", head, "--", "docs/").split("\0"):
        if entry:
            meta, path = entry.split("\t", 1)
            if meta.split()[0] in ("100644", "100755"):
                regular.add(path)
    lines = {p: nums for p, nums in lines.items() if p in regular}
    return merge_base, git(repo, "diff", *options, *scope), names, lines


def load_json(path):
    if Path(path).stat().st_size > 250_000:
        raise ValueError("JSON input too large")
    def unique(pairs):
        obj = {}
        for key, value in pairs:
            if key in obj:
                raise ValueError("Duplicate JSON key")
            obj[key] = value
        return obj
    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=unique,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError("Invalid JSON constant")))


def validate_review(review):
    def text(value, limit, nonempty=False):
        if (not isinstance(value, str) or len(value) > limit or (nonempty and not value.strip())
                or any(ord(c) < 32 and c not in "\n\t\r" for c in value)):
            raise ValueError("Invalid review string")
    if not isinstance(review, dict) or set(review) != {"summary", "findings"}:
        raise ValueError("Invalid review object")
    text(review["summary"], 4000, True)
    findings = review["findings"]
    if not isinstance(findings, list) or len(findings) > 30:
        raise ValueError("Expected at most 30 findings")
    fields = {"path", "line", "severity", "category", "problem", "suggestion", "replacement_line"}
    for f in findings:
        if not isinstance(f, dict) or set(f) != fields:
            raise ValueError("Invalid finding object")
        safe_path(f["path"])
        if type(f["line"]) is not int or not 1 <= f["line"] <= 2_147_483_647:
            raise ValueError("Invalid line number")
        if not isinstance(f["severity"], str) or f["severity"] not in {"high", "medium", "low"}:
            raise ValueError("Invalid severity")
        if not isinstance(f["category"], str) or f["category"] not in CATEGORIES:
            raise ValueError("Invalid category")
        text(f["problem"], 2000, True)
        text(f["suggestion"], 2000)
        text(f["replacement_line"], 2000)
        if "\n" in f["replacement_line"] or "\r" in f["replacement_line"] or "```" in f["replacement_line"]:
            raise ValueError("Replacement must be a single line without fences")
    return review


def cmd_prepare(args):
    merge_base, diff, names, lines = diff_input(args.repo, args.base, args.head)
    event = load_json(args.event)["pull_request"]
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    metadata = {"number": event["number"], "title": event["title"],
                "description": event.get("body") or "", "author": event["user"]["login"],
                "base_commit": merge_base, "head_commit": args.head}
    for name, content in {"pr.diff": diff, "changed-files.txt": names.replace("\0", "\n"),
                          "added-lines.json": json.dumps(lines, indent=2),
                          "pr.json": json.dumps(metadata, indent=2)}.items():
        (out / name).write_text(content, encoding="utf-8")
    return 0


def comment_body(f):
    body = f"**{f['severity']} · {f['category']}**: {f['problem']}"
    if f["suggestion"]:
        body += "\n\n" + f["suggestion"]
    if f["replacement_line"]:
        body += f"\n\n```suggestion\n{f['replacement_line']}\n```"
    return body + "\n\n" + MARKER


def cmd_publish(args):
    if type(args.pr) is not int or args.pr <= 0:
        raise ValueError("Invalid PR number")
    _, _, names, lines = diff_input(args.repo, args.base, args.head)
    changed_paths = set(names.split("\0")) - {""}
    review = None
    if args.result == "success":
        review = validate_review(load_json(args.review))
    findings = review["findings"] if review else []
    if any(f["path"] not in changed_paths for f in findings):
        raise ValueError("Finding refers to a file outside the documentation diff")
    inline = [f for f in findings if f["line"] in lines.get(f["path"], ())]
    summary = (f"{SUMMARY_MARKER}\n## Codex review\n\n"
               + (review["summary"] if review else "The review did not finish. See the workflow run.")
               + f"\n\nCommit `{args.head}` · Report-only; does not block merging.")
    # Outside-diff findings are data, never suggestions on unrelated lines.
    for f in findings:
        if f not in inline:
            summary += f"\n\n{f['path']}:{f['line']} — {f['severity']}: {f['problem']}\n\n{f['suggestion']}"
    if len(summary) > 60000:
        raise ValueError("Summary exceeds GitHub comment limit")
    comments = [{"path": f["path"], "line": f["line"], "side": "RIGHT", "body": comment_body(f)} for f in inline]
    if args.dry_run:
        print(summary)
        print(json.dumps(comments, ensure_ascii=False, indent=2))
        return 0
    github = GitHub(os.environ["GITHUB_REPOSITORY"], os.environ["GITHUB_TOKEN"])

    def current():
        pr = github.request("GET", f"pulls/{args.pr}")
        if (pr["head"]["sha"] != args.head or pr["head"]["repo"]["full_name"] != github.repository
                or pr["state"] != "open" or pr["draft"] or pr["base"]["ref"] != "master"):
            raise ValueError("PR is stale or no longer eligible")

    current()
    existing = next((c for c in github.paged(f"issues/{args.pr}/comments")
                     if SUMMARY_MARKER in c["body"] and c["user"]["login"] == "github-actions[bot]"), None)
    if comments:
        current()
        github.request("POST", f"pulls/{args.pr}/reviews", {
            "commit_id": args.head, "event": "COMMENT", "body": MARKER, "comments": comments})
    current()
    if existing:
        github.request("PATCH", f"issues/comments/{int(existing['id'])}", {"body": summary})
    else:
        github.request("POST", f"issues/{args.pr}/comments", {"body": summary})
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("prepare", "publish"):
        sub = commands.add_parser(command)
        sub.add_argument("--repo", required=True, help="data-only PR checkout")
        sub.add_argument("--base", required=True, help="trusted base SHA")
        sub.add_argument("--head", required=True, help="expected PR head SHA")
        if command == "prepare":
            sub.add_argument("--event", required=True)
            sub.add_argument("--out", required=True)
        else:
            sub.add_argument("--review", required=True)
            sub.add_argument("--pr", required=True, type=int)
            sub.add_argument("--result", default="success", choices=("success", "failure", "cancelled"))
            sub.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        return cmd_prepare(args) if args.command == "prepare" else cmd_publish(args)
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        print(f"Review rejected: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
