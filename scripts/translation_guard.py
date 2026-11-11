#!/usr/bin/env python3
"""Validate an automated router translation patch before building or publishing it.

Run from a clean checkout after ``git apply --index``. Only localized files and
.translation-cache.json may change. This is an independent workflow check, not
an instruction that the translation model can opt out of.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path, PurePosixPath

LANGS = ('de', 'es', 'fr', 'it', 'ja', 'nl', 'pl', 'sv', 'uk')
PROTECTED_IDS = {'safety-information', 'declaration-of-conformity'}
HEADING = re.compile(r'^(#{1,6})\s+.*?\{#([^}]+)\}\s*$')


def git(*args: str) -> bytes:
    return subprocess.check_output(['git', *args])


def allowed_path(value: str) -> bool:
    path = PurePosixPath(value)
    if value == '.translation-cache.json':
        return True
    return (
        not path.is_absolute() and '\\' not in value
        and all(part not in ('.', '..') for part in path.parts)
        and len(path.parts) >= 3 and path.parts[0] == 'docs'
        and path.parts[1] in LANGS
        and path.parts[2:] != ('docs', 'downloads', 'index.md')
        and not any(ord(char) < 32 for char in value)
        and 'site' not in path.parts
    )


def protected_sections(text: str) -> list[str]:
    """Keep approved sections byte-for-byte (after universal newline decoding)."""
    lines = text.splitlines(keepends=True)
    sections = []
    for index, line in enumerate(lines):
        match = HEADING.match(line.rstrip('\r\n'))
        if not match or match[2] not in PROTECTED_IDS:
            continue
        level = len(match[1])
        end = index + 1
        while end < len(lines):
            heading = re.match(r'^(#{1,6})\s+', lines[end])
            if heading and len(heading[1]) <= level:
                break
            end += 1
        sections.append(''.join(lines[index:end]))
    return sections


def heading_ids(text: str) -> list[str]:
    return [match[2] for line in text.splitlines() if (match := HEADING.match(line))]


def protected_placements(text: str, stable_ids: set[str]) -> list[tuple[str, int, str, str]]:
    headings = heading_ids(text)
    return [
        (heading, sum(h not in PROTECTED_IDS for h in headings[:index]),
         next((h for h in reversed(headings[:index]) if h in stable_ids), ''),
         next((h for h in headings[index + 1:] if h in stable_ids), ''))
        for index, heading in enumerate(headings) if heading in PROTECTED_IDS
    ]


def check_content(path: str, before: str, after: str) -> None:
    # Neighbor IDs can legitimately change with English titles. Compare heading
    # positions plus surviving neighbors, not the old spelling of renamed IDs.
    stable_ids = (set(heading_ids(before)) & set(heading_ids(after))) - PROTECTED_IDS
    if path.endswith('.md') and (
        protected_sections(before) != protected_sections(after)
        or protected_placements(before, stable_ids) != protected_placements(after, stable_ids)
    ):
        raise ValueError(f'Translation changed approved legal wording or placement: {path}')


def validate_report(path: Path) -> None:
    report = json.loads(path.read_text(encoding='utf-8-sig'))
    if report.get('status') != 'completed':
        raise ValueError('Only a completed translation may be published.')
    if report.get('validation', {}).get('passed') is not True:
        raise ValueError('Translation report did not pass validation.')
    if any(issue.get('blocking') for issue in report.get('source_issues', [])):
        raise ValueError('Translation report contains a blocking source issue.')


def check_patch() -> list[str]:
    paths = git('diff', '--cached', '--name-only', '-z', '--no-renames').decode('utf-8').split('\0')
    changed = [path for path in paths if path]
    for path in changed:
        if not allowed_path(path):
            raise ValueError(f'Translation changed a forbidden path: {path}')
        staged = git('ls-files', '--stage', '--', path).decode('utf-8')
        if staged and not staged.startswith('100644 '):
            raise ValueError(f'Translation introduced a non-regular file: {path}')
        if Path(path).suffix in ('.md', '.yml', '.yaml', '.html'):
            old = subprocess.run(['git', 'show', f'HEAD:{path}'], capture_output=True)
            before = old.stdout.decode('utf-8').replace('\r\n', '\n') if old.returncode == 0 else ''
            after = Path(path).read_text(encoding='utf-8-sig') if staged else ''
            check_content(path, before, after)
    if not changed:
        raise ValueError('Translation patch is empty.')
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    try:
        validate_report(args.report)
        changed = check_patch()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f'::error::{error}')
        return 1
    print(f'Translation scope and protected wording verified: {len(changed)} file(s).')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
