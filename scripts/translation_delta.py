#!/usr/bin/env python3
"""Report English documentation files that need translation sync."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import subprocess
import sys
from dataclasses import dataclass
from typing import Iterable


DEFAULT_LANGS = ("de", "es", "fr", "it", "jp", "pl")
DEFAULT_EXTENSIONS = (".md", ".yml", ".yaml", ".html")
DEFAULT_EXCLUDE_DIRS = {"site", ".git", "__pycache__"}


@dataclass(frozen=True)
class SourceStatus:
    path: str
    current_hash: str
    cached_hash: str
    status: str
    missing_targets: list[str]


def repo_path(path: pathlib.Path) -> str:
    return path.as_posix()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_json(path: pathlib.Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def parse_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def run_git(args: list[str]) -> tuple[int, str]:
    try:
        proc = subprocess.run(
            ["git", *args],
            check=False,
            text=True,
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
        if path.suffix.lower() in extensions:
            yield path


def target_path_for_lang(source_path: str, lang: str) -> pathlib.Path:
    if source_path.startswith("docs/en/docs/"):
        return pathlib.Path(source_path.replace("docs/en/docs/", f"docs/{lang}/docs/", 1))
    if source_path.startswith("docs/en/"):
        return pathlib.Path(source_path.replace("docs/en/", f"docs/{lang}/", 1))
    raise ValueError(f"Unexpected English source path: {source_path}")


def analyze_sources(
    source_files: Iterable[pathlib.Path],
    cache: dict,
    langs: list[str],
) -> list[SourceStatus]:
    results: list[SourceStatus] = []
    for path in source_files:
        source_rel = repo_path(path)
        current_hash = sha256_text(path.read_text(encoding="utf-8"))
        cache_entry = cache.get(source_rel, {})
        cached_hash = cache_entry.get("source_hash", "") if isinstance(cache_entry, dict) else ""
        if not cached_hash:
            status = "cache-missing"
        elif cached_hash != current_hash:
            status = "hash-mismatch"
        else:
            status = "synced"

        missing_targets = [
            lang for lang in langs if not target_path_for_lang(source_rel, lang).exists()
        ]
        if missing_targets and status == "synced":
            status = "target-missing"

        results.append(
            SourceStatus(
                path=source_rel,
                current_hash=current_hash,
                cached_hash=cached_hash,
                status=status,
                missing_targets=missing_targets,
            )
        )
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

    cache_missing = [item.path for item in statuses if item.status == "cache-missing"]
    hash_mismatch = [item.path for item in statuses if item.status == "hash-mismatch"]
    target_missing = [
        f"{item.path} -> missing {','.join(item.missing_targets)}"
        for item in statuses
        if item.missing_targets
    ]

    print_section("Cache missing", cache_missing)
    print_section("Hash mismatch", hash_mismatch)
    print_section("Target missing", target_missing)
    print_section("Stale cache keys", stale)


def build_json(preflight: dict[str, object], statuses: list[SourceStatus], stale: list[str]) -> dict:
    return {
        "preflight": preflight,
        "cache_missing": [item.path for item in statuses if item.status == "cache-missing"],
        "hash_mismatch": [item.path for item in statuses if item.status == "hash-mismatch"],
        "target_missing": [
            {"path": item.path, "missing_targets": item.missing_targets}
            for item in statuses
            if item.missing_targets
        ],
        "stale_cache_keys": stale,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache-file", default=".translation-cache.json")
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
    args = parser.parse_args()

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


if __name__ == "__main__":
    sys.exit(main())
