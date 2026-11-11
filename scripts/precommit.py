#!/usr/bin/env python3
"""Checks run by .githooks/pre-commit on the files staged for a commit.

Enable the hook once per clone:
  git config core.hooksPath .githooks

The hook first gives new English headings the ID that MkDocs generates for them
(as ``anchors.py add --lang en`` does) and stages the fix. Pages with unstaged
changes are left alone, so the hook never stages work in progress.

For staged pages, the hook then reports:
- heading ID and anchor problems (scripts/anchors.py); broken anchor links are
  reported for every page of the touched languages;
- for localized pages: structure and text problems (scripts/i18n_check.py),
  legal sections removed or changed since HEAD (or the merge base with
  ``--base``);
- for localized files: .translation-cache.json records matching both source
  and target in the index (or HEAD with ``--base``), never unstaged edits;
- for mkdocs.yml or added, renamed or deleted pages: orphan pages and redirect
  problems.

English-only commits do not require translations in the same commit, but
heading and anchor errors still block the commit.

Bypass in an emergency with ``git commit --no-verify``.

CI runs the same checks on the files a pull request changes:
  python scripts/precommit.py --base origin/master
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import anchors  # noqa: E402
import i18n_check  # noqa: E402
import translation_delta  # noqa: E402

LANGS = anchors.LANGS
PATH_RE = re.compile(r"^docs/(?P<lang>[a-z]{2})/(?P<rest>.+)$")


def staged_files(base: str | None = None) -> list[tuple[str, str]]:
    """Return (status, path) for staged changes, or for changes since ``base``; renames give the new path."""
    scope = [f"{base}...HEAD"] if base else ["--cached"]
    output = git("diff", *scope, "--name-status", "--find-renames", "-z")
    fields = iter(output.split("\0")[:-1])
    files = []
    for status in fields:
        path = next(fields)
        if status[0] == "R":
            files.extend([("R", next(fields)), ("D", path)])
        else:
            files.append((status[0], path))
    return files


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True, encoding="utf-8",
    ).stdout


def add_missing_ids(files: list[tuple[str, str]]) -> None:
    """Give staged English headings without an ID the ID MkDocs generates, and stage the fix."""
    unstaged = set(git("diff", "--name-only", "-z").split("\0"))
    for status, path in files:
        if status == "D" or not path.startswith("docs/en/docs/") or not path.endswith(".md"):
            continue
        page = anchors.load_page(anchors.SOURCE_LANG, anchors.REPO_ROOT / path)
        fixes = anchors.missing_id_fixes(page)
        if not fixes:
            continue
        if path in unstaged:
            print(f"pre-commit: {path} has unstaged changes; add the heading IDs by hand or stage the page")
            continue
        for heading, _ in fixes:
            anchors.set_heading_id(page, heading, heading.rendered_id)
        anchors.write_page(page)
        git("add", "--", path)
        print(f"pre-commit: added heading IDs to {path}: {', '.join(h.rendered_id for h, _ in fixes)}")


def revision_bytes(revision: str, path: str) -> bytes:
    return subprocess.run(
        ["git", "show", f"{revision}:{path}"], check=True, capture_output=True,
    ).stdout


def checked_pages(lang: str, files: list[tuple[str, str]], revision: str = "") -> dict[str, anchors.Page]:
    """Use submitted text for touched pages, so unstaged fixes cannot hide errors."""
    pages = anchors.load_lang(lang)
    prefix = f"docs/{lang}/docs/"
    for status, path in files:
        if not path.startswith(prefix) or not path.endswith(".md"):
            continue
        rel = path[len(prefix):]
        if status == "D":
            pages.pop(rel, None)
        else:
            text = revision_bytes(revision, path).decode("utf-8")
            pages[rel] = anchors.load_page(lang, anchors.REPO_ROOT / path, text)
    return pages


def cache_errors(files: list[tuple[str, str]], base: str | None = None) -> list[str]:
    """Validate only changed translations against the committed/staged snapshot.

    Local commits use the index; PR checks use HEAD, not the dirty index or
    working tree. Other languages and English-only commits may remain pending.
    """
    revision = "HEAD" if base else ""
    listing = git("ls-tree", "-r", "--name-only", "-z", "HEAD") if base else git("ls-files", "-z")
    indexed = set(listing.split("\0"))
    candidates = []
    for status, path in files:
        match = PATH_RE.match(path)
        if status == "D" or not match or match.group("lang") not in translation_delta.DEFAULT_LANGS:
            continue
        lang, rest = match.group("lang"), match.group("rest")
        source = f"docs/en/{rest}"
        if source in indexed and source not in translation_delta.EXCLUDED_SOURCE_PATHS:
            candidates.append((lang, source, path))
    cache_changed = any(path == translation_delta.CACHE_FILE for _, path in files)
    if not candidates and not cache_changed:
        return []
    label = "HEAD" if base else "staged"
    try:
        cache = json.loads(revision_bytes(revision, translation_delta.CACHE_FILE).decode("utf-8-sig"))
        if not isinstance(cache, dict):
            raise ValueError("root must be an object")
    except (ValueError, UnicodeError, subprocess.CalledProcessError) as error:
        return [f"{translation_delta.CACHE_FILE}: invalid {label} .translation-cache.json: {error}; "
                "restore it or run translation_delta.py mark and stage .translation-cache.json"]

    errors = []
    for lang, source, path in candidates:
        entry = cache.get(source)
        targets = entry.get("targets") if isinstance(entry, dict) else None
        record = targets.get(lang) if isinstance(targets, dict) else None
        if not isinstance(record, dict) or "source_hash" in entry:
            errors.append(f"{path}: missing per-language .translation-cache.json record; run "
                          "python scripts/translation_delta.py migrate if using a legacy file, then "
                          f"python scripts/translation_delta.py mark {source} --lang {lang} "
                          "and stage .translation-cache.json")
            continue
        try:
            hashes = translation_delta.source_hashes(pathlib.Path(source), revision_bytes(revision, source))
            target_hash = translation_delta.hash_bytes(pathlib.Path(path), revision_bytes(revision, path))
        except (UnicodeError, subprocess.CalledProcessError) as error:
            errors.append(f"{path}: cannot hash {label} source/translation: {error}")
            continue
        if record.get("source_hash") not in hashes or record.get("target_hash") != target_hash:
            errors.append(f"{path}: .translation-cache.json does not match {label} source/target; run "
                          f"python scripts/translation_delta.py mark {source} --lang {lang} after validation "
                          f"and stage both {path} and .translation-cache.json")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check staged documentation changes.")
    parser.add_argument("--base", help="check the changes since this ref instead of the staged files")
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    errors: list[str] = []
    pages: dict[str, set[str]] = {}  # lang -> staged pages relative to docs/<lang>/docs
    file_check_langs: set[str] = set()
    localized_files: list[tuple[str, pathlib.Path]] = []
    files = staged_files(args.base)
    if not args.base:
        add_missing_ids(files)
    errors.extend(cache_errors(files, args.base))
    for status, path in files:
        match = PATH_RE.match(path)
        if not match or match.group("lang") not in LANGS:
            continue
        lang, rest = match.group("lang"), match.group("rest")
        if rest == "mkdocs.yml" or (rest.startswith("docs/") and rest.endswith(".md") and status in "ADR"):
            file_check_langs.add(lang)
        if status == "D":
            continue
        if rest.startswith("docs/") and rest.endswith(".md"):
            pages.setdefault(lang, set()).add(rest[len("docs/"):])
        if lang != anchors.SOURCE_LANG:
            localized_files.append((lang, pathlib.Path(path)))
    if not pages and not file_check_langs:
        for error in errors:
            print(f"ERROR {error}")
        return int(bool(errors))

    revision = "HEAD" if args.base else ""
    en_pages = checked_pages(anchors.SOURCE_LANG, files, revision)
    for lang in sorted(pages):
        report = anchors.Report()
        lang_pages = en_pages if lang == anchors.SOURCE_LANG else checked_pages(lang, files, revision)
        anchors.check_lang(lang, lang_pages, en_pages, report)
        for error in report.errors:
            rel = error.split(":", 1)[0].split("/", 1)[1]
            # Missing English IDs in pages nobody touched are translation backlog.
            if rel in pages[lang] or "broken anchor link" in error:
                errors.append(f"[anchors] {error}")

    for lang in sorted(file_check_langs):
        errors.extend(str(issue) for issue in i18n_check.check_language_files(lang))

    # Legal sections are compared with the commit the changes started from.
    protected_base = git("merge-base", args.base, "HEAD").strip() if args.base else "HEAD"
    for lang, path in localized_files:
        source = translation_delta.repo_path(path).replace(f"docs/{lang}/", "docs/en/", 1)
        if source in translation_delta.EXCLUDED_SOURCE_PATHS or not pathlib.Path(source).exists():
            continue
        rel = source[len("docs/en/docs/"):] if source.startswith("docs/en/docs/") else None
        if rel and rel.endswith(".md"):
            errors.extend(str(issue) for issue in i18n_check.check_page(lang, rel, base=protected_base))

    for error in dict.fromkeys(errors):
        print(f"ERROR {error}")
    if errors and args.base:
        print(f"{len(errors)} error(s).")
    elif errors:
        print(f"pre-commit: {len(errors)} error(s). Fix them, or bypass with git commit --no-verify.")
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
