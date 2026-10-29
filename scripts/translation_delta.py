#!/usr/bin/env python3
"""Report English documentation files that need translation sync, per language.

Usage:
  python scripts/translation_delta.py [--json] [--fail-on-delta]
  python scripts/translation_delta.py mark <en-file> ... --lang de ja ... [--no-target-change]
  python scripts/translation_delta.py diff <en-file> --lang de
  python scripts/translation_delta.py migrate

.translation-cache.json records, for every English source file and every
language, the English version the translation was last synced with:

  "docs/en/docs/page.md": {
    "targets": {
      "de": {
        "source_hash": "...",   sha256 of the English text that is translated
        "source_blob": "...",   git blob ID of the English file, for ``diff``
        "target_hash": "...",   sha256 of the localized file after the sync
        "model": "...",
        "updated_at": 1790000000
      }
    }
  }

Only ``mark`` writes the cache. It refuses to record a language when
scripts/i18n_check.py reports errors for that page (including a localized-only
legal section removed or changed since HEAD), or when the English text
changed but the localized file did not (unless --no-target-change is given for
that language explicitly). ``diff`` shows what English changed since a
language was last synced. ``migrate`` converts the old format, which had one
``source_hash`` for all languages.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import subprocess
import sys
import time
from dataclasses import dataclass, field
from typing import Iterable


DEFAULT_LANGS = ("de", "es", "fr", "it", "ja", "nl", "pl", "sv", "uk")
DEFAULT_EXTENSIONS = (".md", ".yml", ".yaml", ".html", ".js", ".css")
DEFAULT_EXCLUDE_DIRS = {"site", ".git", "__pycache__"}
EXCLUDED_SOURCE_PATHS = {"docs/en/docs/downloads/index.md"}
EXCLUDED_TRAILING_MARKDOWN_SECTIONS = {"Regulatory Statements"}
CACHE_FILE = ".translation-cache.json"
NO_TARGET_CHANGE_MODEL = "reviewed-no-target-change"


@dataclass
class SourceStatus:
    path: str
    current_hash: str
    cache_missing: list[str] = field(default_factory=list)
    hash_mismatch: list[str] = field(default_factory=list)
    missing_targets: list[str] = field(default_factory=list)


def repo_path(path: pathlib.Path) -> str:
    return path.as_posix()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def markdown_heading(line: str) -> tuple[int, str] | None:
    stripped = line.strip()
    if not stripped.startswith("#"):
        return None
    level = len(stripped) - len(stripped.lstrip("#"))
    if level == 0 or level > 6:
        return None
    if len(stripped) <= level or stripped[level] != " ":
        return None
    return level, stripped[level + 1 :].strip()


def heading_title(text: str) -> str:
    """Drop an attribute block such as {#regulatory-statements}."""
    if text.endswith("}") and "{" in text:
        return text[: text.rindex("{")].strip()
    return text


def translation_sync_texts(path: pathlib.Path, text: str) -> list[str]:
    if path.suffix.lower() != ".md":
        return [text]

    output: list[str] = []
    lines = text.splitlines(keepends=True)
    index = 0
    while index < len(lines):
        heading = markdown_heading(lines[index])
        if heading and heading_title(heading[1]) in EXCLUDED_TRAILING_MARKDOWN_SECTIONS:
            break

        output.append(lines[index])
        index += 1

    sync_text = "".join(output)
    variants = [sync_text]
    if sync_text != text and sync_text.endswith("\n"):
        variants.append(sync_text[:-1])
    return variants


def sync_hashes(path: pathlib.Path, text: str) -> list[str]:
    return [sha256_text(value) for value in translation_sync_texts(path, text)]


def read_json(path: pathlib.Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: pathlib.Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def parse_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def run_git(args: list[str], input_text: str | None = None) -> tuple[int, str]:
    try:
        proc = subprocess.run(
            ["git", *args],
            check=False,
            input=input_text,
            text=True,
            encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
    except FileNotFoundError:
        return 127, "git not found"
    return proc.returncode, proc.stdout.strip()


def collect_preflight() -> dict[str, object]:
    branch_code, branch = run_git(["branch", "--show-current"])
    status_code, status = run_git(["status", "--short"])
    upstream_code, upstream = run_git(["rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"])
    ahead = None
    behind = None
    if upstream_code == 0 and upstream:
        divergence_code, divergence = run_git(["rev-list", "--left-right", "--count", f"HEAD...{upstream}"])
        if divergence_code == 0 and divergence:
            parts = divergence.split()
            if len(parts) == 2:
                ahead = int(parts[0])
                behind = int(parts[1])

    status_lines = status.splitlines() if status_code == 0 and status else []
    current_branch = branch if branch_code == 0 else ""
    warnings: list[str] = []
    if current_branch and current_branch != "master":
        warnings.append(f"branch is {current_branch}, not master")
    if behind:
        warnings.append(f"branch is behind {upstream} by {behind} commit(s)")
    if status_lines:
        warnings.append("working tree is not clean")

    return {
        "branch": current_branch,
        "status": status.splitlines() if status_code == 0 and status else [],
        "upstream": upstream if upstream_code == 0 else "",
        "ahead": ahead,
        "behind": behind,
        "warnings": warnings,
    }


def iter_source_files(
    en_root: pathlib.Path,
    extensions: set[str],
    exclude_dirs: set[str],
) -> Iterable[pathlib.Path]:
    if not en_root.exists():
        raise FileNotFoundError(f"English source root not found: {en_root}")

    for path in sorted(en_root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in exclude_dirs for part in path.parts):
            continue
        relative_path = repo_path(path)
        if relative_path in EXCLUDED_SOURCE_PATHS:
            continue
        if path.suffix.lower() in extensions:
            yield path


def target_path_for_lang(source_path: str, lang: str) -> pathlib.Path:
    if source_path.startswith("docs/en/docs/"):
        return pathlib.Path(source_path.replace("docs/en/docs/", f"docs/{lang}/docs/", 1))
    if source_path.startswith("docs/en/"):
        return pathlib.Path(source_path.replace("docs/en/", f"docs/{lang}/", 1))
    raise ValueError(f"Unexpected English source path: {source_path}")


def target_record(cache: dict, source: str, lang: str) -> dict:
    entry = cache.get(source)
    if not isinstance(entry, dict):
        return {}
    record = dict((entry.get("targets") or {}).get(lang) or {})
    # Old format: one source_hash shared by all languages.
    if "source_hash" not in record and entry.get("source_hash"):
        record["source_hash"] = entry["source_hash"]
    return record


def analyze_sources(
    source_files: Iterable[pathlib.Path],
    cache: dict,
    langs: list[str],
) -> list[SourceStatus]:
    results: list[SourceStatus] = []
    for path in source_files:
        source_rel = repo_path(path)
        current_hashes = sync_hashes(path, path.read_text(encoding="utf-8"))
        status = SourceStatus(path=source_rel, current_hash=current_hashes[0])
        for lang in langs:
            if not target_path_for_lang(source_rel, lang).exists():
                status.missing_targets.append(lang)
                continue
            cached_hash = target_record(cache, source_rel, lang).get("source_hash", "")
            if not cached_hash:
                status.cache_missing.append(lang)
            elif cached_hash not in current_hashes:
                status.hash_mismatch.append(lang)
        results.append(status)
    return results


def stale_cache_keys(cache: dict) -> list[str]:
    stale: list[str] = []
    for key in sorted(cache):
        if key.startswith("docs/en/") and not pathlib.Path(key).exists():
            stale.append(key)
    return stale


def print_section(title: str, rows: list[str]) -> None:
    print(f"\n{title} ({len(rows)})")
    if not rows:
        print("  none")
        return
    for row in rows:
        print(f"  {row}")


def format_report(preflight: dict[str, object], statuses: list[SourceStatus], stale: list[str]) -> None:
    print("Preflight")
    print(f"  branch: {preflight.get('branch') or '(unknown)'}")
    print(f"  upstream: {preflight.get('upstream') or '(none)'}")
    ahead = preflight.get("ahead")
    behind = preflight.get("behind")
    if ahead is None or behind is None:
        print("  divergence: (not checked)")
    else:
        print(f"  divergence: ahead {ahead}, behind {behind}")
    warnings = preflight.get("warnings") or []
    if warnings:
        print("  warnings:")
        for warning in warnings:
            print(f"    {warning}")
    status_lines = preflight.get("status") or []
    if status_lines:
        print("  working tree:")
        for line in status_lines:
            print(f"    {line}")
    else:
        print("  working tree: clean")

    def rows(attr: str) -> list[str]:
        return [f"{item.path} -> {','.join(getattr(item, attr))}" for item in statuses if getattr(item, attr)]

    print_section("Cache missing", rows("cache_missing"))
    print_section("Hash mismatch", rows("hash_mismatch"))
    print_section("Target missing", [row.replace("->", "-> missing", 1) for row in rows("missing_targets")])
    print_section("Stale cache keys", stale)
    if any(item.hash_mismatch for item in statuses):
        print("\nShow the English changes since a language was synced:")
        print("  python scripts/translation_delta.py diff <en-file> --lang <lang>")


def build_json(preflight: dict[str, object], statuses: list[SourceStatus], stale: list[str]) -> dict:
    return {
        "preflight": preflight,
        "cache_missing": [
            {"path": item.path, "langs": item.cache_missing} for item in statuses if item.cache_missing
        ],
        "hash_mismatch": [
            {"path": item.path, "langs": item.hash_mismatch} for item in statuses if item.hash_mismatch
        ],
        "target_missing": [
            {"path": item.path, "missing_targets": item.missing_targets}
            for item in statuses
            if item.missing_targets
        ],
        "stale_cache_keys": stale,
    }


def cmd_report(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cache-file", default=CACHE_FILE)
    parser.add_argument("--en-root", default="docs/en")
    parser.add_argument("--langs", default=",".join(DEFAULT_LANGS))
    parser.add_argument("--extensions", default=",".join(DEFAULT_EXTENSIONS))
    parser.add_argument("--exclude-dirs", default=",".join(sorted(DEFAULT_EXCLUDE_DIRS)))
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument(
        "--fail-on-delta",
        action="store_true",
        help="Exit with status 1 when cache/hash/target/stale deltas are found.",
    )
    args = parser.parse_args(argv)

    langs = parse_csv(args.langs)
    extensions = {ext if ext.startswith(".") else f".{ext}" for ext in parse_csv(args.extensions)}
    exclude_dirs = set(parse_csv(args.exclude_dirs))
    cache = read_json(pathlib.Path(args.cache_file))
    preflight = collect_preflight()
    statuses = analyze_sources(
        iter_source_files(pathlib.Path(args.en_root), extensions, exclude_dirs),
        cache,
        langs,
    )
    stale = stale_cache_keys(cache)
    report = build_json(preflight, statuses, stale)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        format_report(preflight, statuses, stale)

    has_delta = any(report[key] for key in ("cache_missing", "hash_mismatch", "target_missing", "stale_cache_keys"))
    return 1 if args.fail_on_delta and has_delta else 0


# --------------------------------------------------------------------------
# mark, diff, migrate


def source_arg(value: str) -> str:
    path = pathlib.Path(value).resolve()
    try:
        rel = repo_path(path.relative_to(pathlib.Path.cwd().resolve()))
    except ValueError:
        raise SystemExit(f"{value}: run from the repository root and pass a path inside it")
    if not rel.startswith("docs/en/"):
        raise SystemExit(f"{value}: not an English source file under docs/en/")
    if rel in EXCLUDED_SOURCE_PATHS:
        raise SystemExit(f"{value}: excluded from translation sync")
    if not path.is_file():
        raise SystemExit(f"{value}: file not found")
    return rel


def git_blob(path: str | pathlib.Path, write: bool = True) -> str:
    """Return the git blob ID of a working tree file; with write, store the blob so diff can read it later."""
    code, output = run_git(["hash-object", *(["-w"] if write else []), "--", str(path)])
    if code != 0 and write:
        # A sandbox may not allow writing to .git; committed files are in history anyway.
        code, output = run_git(["hash-object", "--", str(path)])
    if code != 0:
        raise SystemExit(f"git hash-object failed for {path}: {output}")
    return output


def target_hash(path: pathlib.Path) -> str:
    return sha256_text(path.read_text(encoding="utf-8"))


def upgrade_entry(entry: dict, langs: Iterable[str]) -> None:
    """Move an old shared source_hash into every language record."""
    legacy = entry.pop("source_hash", None)
    if legacy:
        for lang in langs:
            entry.setdefault("targets", {}).setdefault(lang, {}).setdefault("source_hash", legacy)


def check_target(source: str, lang: str, file_checks: dict[str, list]) -> list[str]:
    """Run scripts/i18n_check.py for one synced file and return its errors."""
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import i18n_check

    if source.startswith("docs/en/docs/") and source.endswith(".md"):
        # Syncs are marked before they are committed, so HEAD has the legal sections to keep.
        issues = i18n_check.check_page(lang, source[len("docs/en/docs/"):], base="HEAD")
    elif source == "docs/en/mkdocs.yml":
        if lang not in file_checks:
            file_checks[lang] = i18n_check.check_language_files(lang)
        issues = file_checks[lang]
    else:
        issues = []
    return [str(issue) for issue in issues]


def cmd_mark(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="translation_delta.py mark",
        description="Record that localized files are synced with the current English files.",
    )
    parser.add_argument("sources", nargs="+", help="English files, e.g. docs/en/docs/interface_guide/vpn.md")
    parser.add_argument("--lang", nargs="+", required=True, help="languages, or 'all'")
    parser.add_argument(
        "--no-target-change",
        action="store_true",
        help="the English change needs no translation change (typo or grammar fixes only); list each language explicitly",
    )
    parser.add_argument("--model", default="manual-sync", help="who synced the translation, stored in the cache")
    parser.add_argument("--cache-file", default=CACHE_FILE)
    args = parser.parse_args(argv)

    if args.lang == ["all"]:
        if args.no_target_change:
            raise SystemExit("--no-target-change needs the languages listed explicitly, not 'all'")
        langs = list(DEFAULT_LANGS)
    else:
        unknown = [lang for lang in args.lang if lang not in DEFAULT_LANGS]
        if unknown:
            raise SystemExit(f"unknown language(s): {', '.join(unknown)}")
        langs = args.lang

    cache_path = pathlib.Path(args.cache_file)
    cache = read_json(cache_path)
    file_checks: dict[str, list] = {}
    failures = 0
    marked = 0
    now = int(time.time())
    for source in dict.fromkeys(source_arg(value) for value in args.sources):
        source_path = pathlib.Path(source)
        current_hashes = sync_hashes(source_path, source_path.read_text(encoding="utf-8"))
        blob = git_blob(source_path)
        for lang in langs:
            where = f"{lang}: {source}"
            target = target_path_for_lang(source, lang)
            if not target.exists():
                print(f"FAIL {where}: {target.as_posix()} does not exist")
                failures += 1
                continue
            errors = check_target(source, lang, file_checks)
            if errors:
                print(f"FAIL {where}: i18n_check reports {len(errors)} error(s)")
                for error in errors:
                    print(f"  {error}")
                failures += 1
                continue

            record = target_record(cache, source, lang)
            new_target_hash = target_hash(target)
            english_changed = record.get("source_hash") not in current_hashes
            if not english_changed and record.get("target_hash") == new_target_hash:
                print(f"OK   {where} (already synced, unchanged)")
                continue
            if english_changed and not args.no_target_change and record.get("target_hash") == new_target_hash:
                print(
                    f"FAIL {where}: English changed since the last sync but {target.as_posix()} did not; "
                    "update the translation, or pass --no-target-change for this language if no change is needed"
                )
                failures += 1
                continue

            entry = cache.setdefault(source, {})
            upgrade_entry(entry, DEFAULT_LANGS)
            entry.setdefault("targets", {})[lang] = {
                "source_hash": current_hashes[0],
                "source_blob": blob,
                "target_hash": new_target_hash,
                "model": NO_TARGET_CHANGE_MODEL if args.no_target_change else args.model,
                "updated_at": now,
            }
            marked += 1
            print(f"OK   {where}" + ("" if english_changed else " (already synced)"))

    if marked:
        write_json(cache_path, cache)
    print(f"marked {marked}, failed {failures}")
    return 1 if failures else 0


def cmd_diff(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="translation_delta.py diff",
        description="Show the English changes since a language was last synced.",
    )
    parser.add_argument("source", help="English file")
    parser.add_argument("--lang", required=True, choices=DEFAULT_LANGS)
    parser.add_argument("--cache-file", default=CACHE_FILE)
    args = parser.parse_args(argv)

    source = source_arg(args.source)
    record = target_record(read_json(pathlib.Path(args.cache_file)), source, args.lang)
    old_blob = record.get("source_blob")
    if not old_blob or run_git(["cat-file", "-e", f"{old_blob}^{{blob}}"])[0] != 0:
        print(f"No stored English version for {args.lang}; compare the whole page with {source}.")
        return 1
    new_blob = git_blob(source)
    if old_blob == new_blob:
        print(f"{source} has not changed since {args.lang} was synced.")
        return 0
    return subprocess.call(["git", "--no-pager", "diff", old_blob, new_blob])


def legacy_hashes(path: pathlib.Path, text: str) -> list[str]:
    """Hashes the old format may hold for text.

    After explicit heading IDs were added, "## Regulatory Statements {#...}"
    no longer matched the exclusion, so old entries may hash the whole file.
    """
    return sync_hashes(path, text) + [sha256_text(text)]


def find_source_blob(source: str, source_hash: str) -> str | None:
    """Find the committed English version that source_hash was computed from."""
    path = pathlib.Path(source)
    if source_hash in legacy_hashes(path, path.read_text(encoding="utf-8")):
        return git_blob(path)
    code, commits = run_git(["log", "--format=%H", "-n", "100", "--", source])
    if code != 0:
        return None
    for commit in commits.split():
        code, blob = run_git(["rev-parse", f"{commit}:{source}"])
        if code != 0:
            continue
        code, text = run_git(["cat-file", "blob", blob])
        # run_git strips the trailing newline.
        if code == 0 and source_hash in legacy_hashes(path, text + "\n") + legacy_hashes(path, text):
            return blob
    return None


def cmd_migrate(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        prog="translation_delta.py migrate",
        description="Convert the cache to per-language records (one-time).",
    )
    parser.add_argument("--cache-file", default=CACHE_FILE)
    args = parser.parse_args(argv)

    cache_path = pathlib.Path(args.cache_file)
    cache = read_json(cache_path)
    converted = unknown_blob = 0
    for source, entry in sorted(cache.items()):
        if not isinstance(entry, dict) or "source_hash" not in entry or not pathlib.Path(source).exists():
            continue
        legacy = entry["source_hash"]
        path = pathlib.Path(source)
        text = path.read_text(encoding="utf-8")
        synced = legacy in legacy_hashes(path, text)
        blob = find_source_blob(source, legacy)
        unknown_blob += blob is None
        upgrade_entry(entry, DEFAULT_LANGS)
        for lang, record in entry["targets"].items():
            if blob:
                record.setdefault("source_blob", blob)
            target = target_path_for_lang(source, lang)
            # The translation matches the recorded English version only if
            # English has not changed since; otherwise its old state is unknown.
            if synced and record.get("source_hash") == legacy:
                record["source_hash"] = sync_hashes(path, text)[0]
                if target.exists():
                    record.setdefault("target_hash", target_hash(target))
        converted += 1
    write_json(cache_path, cache)
    print(f"converted {converted} entries; {unknown_blob} without a stored English version")
    return 0


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    argv = sys.argv[1:]
    commands = {"mark": cmd_mark, "diff": cmd_diff, "migrate": cmd_migrate}
    if argv and argv[0] in commands:
        return commands[argv[0]](argv[1:])
    return cmd_report(argv)


if __name__ == "__main__":
    sys.exit(main())
