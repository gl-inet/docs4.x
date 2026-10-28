#!/usr/bin/env python3
"""Content checks for the lines a pull request adds to the documentation.

Usage:
  python scripts/pr_check.py --base origin/master [--languagetool URL]

Only added or changed lines are checked, so old problems in a page do not
block an unrelated change. Errors fail the check; warnings are only reported.

  spelling   (error)    typos in English pages, found by codespell; words that
                        are not typos go into scripts/codespell_ignore.txt
  images     (error)    image URLs that return 404, in every language
  grammar    (warning)  grammar problems in English pages, found by a
                        LanguageTool server; skipped without --languagetool
  heading-id (warning)  English heading IDs that a page no longer has; links,
                        bookmarks and localized pages still use them

Structure checks (heading IDs, anchors, localized pages) are run by
``python scripts/precommit.py --base origin/master``.

Inside GitHub Actions, findings are written as annotations on the pull request
and as a table in the job summary.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from bisect import bisect_right
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import anchors  # noqa: E402
import i18n_check  # noqa: E402

REPO_ROOT = anchors.REPO_ROOT
PAGE_RE = re.compile(r"^docs/(?P<lang>[a-z]{2})/docs/.+\.md$")
HUNK_RE = re.compile(r"^@@ -\S+ \+(\d+)(?:,(\d+))? @@")
CODESPELL_RE = re.compile(r"^(?P<path>.+?):(?P<line>\d+): (?P<word>.+?) ==> (?P<fix>.+)$")
CODESPELL_IGNORE = Path(__file__).resolve().parent / "codespell_ignore.txt"

# Turns a Markdown line into plain prose for LanguageTool; replacements keep
# the sentence readable.
GRAMMAR_SUBS = (
    (re.compile(r"\{[#.:][^}\n]*\}|\{\s*\w+=[^}\n]*\}"), ""),  # attribute blocks
    (re.compile(r"!\[[^\]]*\]\([^)]*\)"), ""),  # images
    (re.compile(r"\[([^\]]*)\]\([^)]*\)"), r"\1"),  # links keep their text
    (re.compile(r"`[^`\n]+`"), "X"),  # inline code
    (re.compile(r"<[^>]+>"), " "),  # HTML tags
    (re.compile(r"https?://\S+"), "example.com"),
    (re.compile(r"\*\*|__|(?<![\w*])\*(?=\S)|(?<=\S)\*(?![\w*])"), ""),  # emphasis markers
    (re.compile(r"^[ \t]*(?:#{1,6}[ \t]+|(?:!!!|\?\?\?\+?|===\+?)[ \t]*\w*[ \t]*|[-*+][ \t]+|\d+\.[ \t]+)"), ""),
    (re.compile(r"^[ \t]*>[ \t]?"), ""),  # block quotes
)
# Rules that do not fit Markdown fragments, or that codespell covers.
GRAMMAR_DISABLED_RULES = (
    "MORFOLOGIK_RULE_EN_US",
    "UPPERCASE_SENTENCE_START",
    "PUNCTUATION_PARAGRAPH_END",
    "WHITESPACE_RULE",
    "COMMA_PARENTHESIS_WHITESPACE",
    "EN_UNPAIRED_BRACKETS",
    "EN_UNPAIRED_QUOTES",
    "DASH_RULE",
    "ARROWS",
    "COMMA_COMPOUND_SENTENCE",
)
GRAMMAR_DISABLED_CATEGORIES = ("TYPOGRAPHY", "CASING", "STYLE", "REDUNDANCY", "PLAIN_ENGLISH")
GRAMMAR_CHUNK = 15000  # characters per request; the public API accepts 20 KB


@dataclass
class Finding:
    level: str  # "error" or "warning"
    check: str
    path: str
    line: int
    message: str


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True, encoding="utf-8", cwd=REPO_ROOT,
    ).stdout


def added_lines(base: str) -> dict[str, set[int]]:
    """Return {page path: added line numbers} for pages added, changed or renamed since ``base``."""
    diff = git("diff", f"{base}...HEAD", "--unified=0", "--no-color", "--find-renames",
               "--diff-filter=AMR", "--", "docs/")
    result: dict[str, set[int]] = {}
    path = None
    for line in diff.splitlines():
        if line.startswith("+++ "):
            name = line[4:]
            path = name[2:] if name.startswith("b/") and PAGE_RE.match(name[2:]) else None
            if path:
                result.setdefault(path, set())
        elif path and (hunk := HUNK_RE.match(line)):
            start, count = int(hunk.group(1)), int(hunk.group(2) or 1)
            result[path].update(range(start, start + count))
    return {path: lines for path, lines in result.items() if lines}


def page_lines(path: str) -> list[str]:
    return (REPO_ROOT / path).read_bytes().decode("utf-8").splitlines()


def prose_lines(lines: list[str]):
    """Yield (line number, line) for lines outside front matter, code fences and table rules."""
    fence: str | None = None
    for index in range(anchors.front_matter_end(lines), len(lines)):
        raw = lines[index]
        fence_match = anchors.FENCE_RE.match(raw)
        if fence is not None:
            if fence_match and fence_match.group(1)[0] == fence[0] and len(fence_match.group(1)) >= len(fence):
                fence = None
            continue
        if fence_match:
            fence = fence_match.group(1)
            continue
        if not raw.strip() or i18n_check.TABLE_RULE_RE.match(raw):
            continue
        yield index + 1, raw


def check_spelling(pages: dict[str, set[int]]) -> list[Finding]:
    paths = [path for path in pages if path.startswith("docs/en/")]
    if not paths:
        return []
    command = [sys.executable, "-m", "codespell_lib", "--uri-ignore-words-list", "*",
               "--ignore-words", str(CODESPELL_IGNORE), *paths]
    try:
        output = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", cwd=REPO_ROOT)
    except OSError as error:
        return [Finding("warning", "spelling", paths[0], 1, f"codespell did not run: {error}")]
    if output.returncode not in (0, 65):  # 65: typos found
        print(output.stderr.strip() or "codespell failed; install it with pip install codespell", file=sys.stderr)
        return [Finding("error", "spelling", paths[0], 1, "codespell did not run; see the log")]
    findings = []
    for line in output.stdout.splitlines():
        match = CODESPELL_RE.match(line)
        if not match:
            continue
        path = match.group("path").replace("\\", "/")
        number = int(match.group("line"))
        if number in pages.get(path, ()):
            findings.append(Finding(
                "error", "spelling", path, number,
                f'"{match.group("word")}" may be a typo; did you mean: {match.group("fix")}? '
                f"If the word is correct, add it to scripts/codespell_ignore.txt.",
            ))
    return findings


def url_status(url: str) -> int | str:
    """Return the HTTP status of ``url``, or an error message."""
    headers = {"User-Agent": "docs4.x-pr-check"}
    for method in ("HEAD", "GET"):
        request = urllib.request.Request(url, method=method, headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                return response.status
        except urllib.error.HTTPError as error:
            if method == "HEAD" and error.code in (403, 405):
                continue  # some servers refuse HEAD
            return error.code
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            return str(getattr(error, "reason", error))
    return "no response"


def check_images(pages: dict[str, set[int]]) -> list[Finding]:
    uses: list[tuple[str, int, str]] = []
    for path, numbers in pages.items():
        for number, raw in prose_lines(page_lines(path)):
            if number not in numbers:
                continue
            for regex in i18n_check.IMAGE_RES:
                uses.extend((path, number, url) for url in regex.findall(raw) if url.startswith(("http://", "https://")))
    urls = sorted({url for _, _, url in uses})
    with ThreadPoolExecutor(max_workers=16) as pool:
        statuses = dict(zip(urls, pool.map(url_status, urls)))
    findings = []
    for path, number, url in uses:
        status = statuses[url]
        if status == 404 or status == 410:
            findings.append(Finding("error", "images", path, number, f"image not found (HTTP {status}): {url}"))
        elif status != 200:
            findings.append(Finding("warning", "images", path, number, f"image could not be checked ({status}): {url}"))
    return findings


def grammar_text(raw: str) -> str:
    text = raw
    for regex, replacement in GRAMMAR_SUBS:
        text = regex.sub(replacement, text)
    # A table row is a set of separate cells.
    if raw.lstrip().startswith("|"):
        text = "\n\n".join(cell.strip() for cell in text.strip().strip("|").split("|"))
    return re.sub(r"[ \t]+", " ", text).strip()


def languagetool(url: str, text: str) -> list[dict]:
    data = urllib.parse.urlencode({
        "text": text,
        "language": "en-US",
        "disabledRules": ",".join(GRAMMAR_DISABLED_RULES),
        "disabledCategories": ",".join(GRAMMAR_DISABLED_CATEGORIES),
    }).encode()
    request = urllib.request.Request(f"{url.rstrip('/')}/v2/check", data=data,
                                     headers={"User-Agent": "docs4.x-pr-check"})
    with urllib.request.urlopen(request, timeout=120) as response:
        return json.load(response)["matches"]


def check_grammar(pages: dict[str, set[int]], url: str) -> list[Finding]:
    findings = []
    for path, numbers in pages.items():
        if not path.startswith("docs/en/"):
            continue
        # Each line is sent as its own paragraph; chunks hold whole lines.
        chunks: list[tuple[str, list[int], list[int]]] = []
        text, starts, line_numbers = "", [], []
        for number, raw in prose_lines(page_lines(path)):
            if number not in numbers or not (prose := grammar_text(raw)):
                continue
            if text and len(text) + len(prose) > GRAMMAR_CHUNK:
                chunks.append((text, starts, line_numbers))
                text, starts, line_numbers = "", [], []
            starts.append(len(text))
            line_numbers.append(number)
            text += prose + "\n\n"
        if text:
            chunks.append((text, starts, line_numbers))
        for text, starts, line_numbers in chunks:
            try:
                matches = languagetool(url, text)
            except (urllib.error.URLError, TimeoutError, OSError, ValueError) as error:
                findings.append(Finding("warning", "grammar", path, line_numbers[0],
                                        f"grammar check failed: {getattr(error, 'reason', error)}"))
                continue
            for match in matches:
                position = bisect_right(starts, match["offset"]) - 1
                context = match["context"]
                excerpt = context["text"][context["offset"]:context["offset"] + context["length"]]
                suggestions = ", ".join(r["value"] for r in match.get("replacements", [])[:3])
                message = f'{match["message"]} "{excerpt}"'
                if suggestions:
                    message += f" -> {suggestions}"
                findings.append(Finding("warning", "grammar", path, line_numbers[position],
                                        f'{message} [{match["rule"]["id"]}]'))
    return findings


def explicit_ids(lines: list[str]) -> set[str]:
    return {h.explicit_id for h in anchors.parse_headings(lines) if h.explicit_id}


def check_heading_ids(base: str) -> list[Finding]:
    changed = git("diff", f"{base}...HEAD", "--name-status", "--find-renames", "--diff-filter=MR", "--", "docs/en/docs/")
    merge_base = git("merge-base", base, "HEAD").strip()
    findings = []
    for line in changed.splitlines():
        parts = line.split("\t")
        old, new = parts[1], parts[-1]
        before = explicit_ids(git("show", f"{merge_base}:{old}").splitlines(keepends=True))
        after = explicit_ids([f"{text}\n" for text in page_lines(new)])
        removed = sorted(before - after)
        if removed:
            findings.append(Finding(
                "warning", "heading-id", new, 1,
                f"heading IDs removed: {', '.join(removed)}. Keep existing IDs when headings are reworded; "
                "if an ID must change, update it in every language and every link that uses it.",
            ))
    return findings


def escape(value: str, property_value: bool = False) -> str:
    value = value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    return value.replace(":", "%3A").replace(",", "%2C") if property_value else value


def report(findings: list[Finding]) -> None:
    in_actions = os.environ.get("GITHUB_ACTIONS") == "true"
    for f in findings:
        if in_actions:
            print(f"::{f.level} file={escape(f.path, True)},line={f.line},title={escape(f.check, True)}::{escape(f.message)}")
        else:
            print(f"{f.level.upper()} [{f.check}] {f.path}:{f.line}: {f.message}")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as out:
            out.write("## Documentation content checks\n\n")
            if not findings:
                out.write("No problems found on the changed lines.\n")
                return
            out.write("| Level | Check | Location | Message |\n|---|---|---|---|\n")
            for f in findings:
                message = f.message.replace("|", "\\|")
                out.write(f"| {f.level} | {f.check} | `{f.path}:{f.line}` | {message} |\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check the lines a pull request adds to the docs.")
    parser.add_argument("--base", required=True, help="compare with this ref, e.g. origin/master")
    parser.add_argument("--languagetool", metavar="URL", help="LanguageTool server for the grammar check")
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    pages = added_lines(args.base)
    findings = check_spelling(pages) + check_images(pages)
    if args.languagetool:
        findings += check_grammar(pages, args.languagetool)
    else:
        print("grammar: skipped, no --languagetool server given")
    findings += check_heading_ids(args.base)
    findings.sort(key=lambda f: (f.path, f.line, f.check))

    report(findings)
    errors = sum(f.level == "error" for f in findings)
    warnings = len(findings) - errors
    print(f"{len(pages)} changed page(s): {errors} error(s), {warnings} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
