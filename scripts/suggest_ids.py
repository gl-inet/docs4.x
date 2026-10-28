#!/usr/bin/env python3
"""Suggest missing English heading IDs on a pull request.

Usage:
  python scripts/suggest_ids.py --base origin/master --head <sha> --pr <number> [--dry-run]

For each English heading that a pull request adds without an explicit ID, posts
a review comment with a suggestion that adds the ID MkDocs generates for it,
for example ``## Quick Setup {#quick-setup}``. Contributors apply it with
"Commit suggestion", or add several to a batch and commit them at once.

Suggestions already posted for the same line are not repeated. Needs
GITHUB_TOKEN and GITHUB_REPOSITORY unless --dry-run is given.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import anchors  # noqa: E402
from codex_review import added_lines  # noqa: E402
from github_api import GitHub  # noqa: E402

MARKER = "<!-- heading-id-suggestion -->"


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True, encoding="utf-8", cwd=anchors.REPO_ROOT,
    ).stdout


def suggestions(base: str, head: str) -> list[dict]:
    merge_base = git("merge-base", base, head).strip()
    diff = git("diff", "--unified=0", "--no-color", "--find-renames", merge_base, head, "--", "docs/en/docs/")
    result = []
    for path, numbers in added_lines(diff).items():
        if not path.endswith(".md"):
            continue
        page = anchors.load_page(anchors.SOURCE_LANG, anchors.REPO_ROOT / path, git("show", f"{head}:{path}"))
        for heading, fixed in anchors.missing_id_fixes(page):
            line = heading.index + 1
            if line not in numbers:
                continue
            suggested = fixed.rstrip("\r\n")
            body = (
                f"This heading needs an explicit ID. Commit this suggestion to add `{{#{heading.rendered_id}}}`, "
                f"the ID MkDocs generates for it.\n\n```suggestion\n{suggested}\n```\n\n{MARKER}"
            )
            result.append({"path": path, "line": line, "side": "RIGHT", "body": body})
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Suggest missing English heading IDs on a pull request.")
    parser.add_argument("--base", required=True, help="base branch ref, e.g. origin/master")
    parser.add_argument("--head", required=True, help="head commit SHA of the pull request")
    parser.add_argument("--pr", type=int, help="pull request number")
    parser.add_argument("--dry-run", action="store_true", help="print the suggestions instead of posting them")
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    comments = suggestions(args.base, args.head)
    if args.dry_run or not comments:
        print(json.dumps(comments, indent=2, ensure_ascii=False) if comments else "No heading IDs to suggest.")
        return 0
    if args.pr is None:
        parser.error("--pr is required unless --dry-run is given")

    github = GitHub(os.environ["GITHUB_REPOSITORY"], os.environ["GITHUB_TOKEN"])
    posted = {
        (c["path"], c["line"], c["body"])
        for c in github.paged(f"pulls/{args.pr}/comments")
        if MARKER in c["body"] and c.get("line") is not None
    }
    new = [c for c in comments if (c["path"], c["line"], c["body"]) not in posted]
    if new:
        github.request("POST", f"pulls/{args.pr}/reviews", {
            "commit_id": args.head,
            "event": "COMMENT",
            "body": "Some new headings have no explicit ID. Commit the suggestions below, "
                    "or add them to a batch and commit them at once.",
            "comments": new,
        })
    print(f"Posted {len(new)} heading ID suggestion(s); {len(comments) - len(new)} already posted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
