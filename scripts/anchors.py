#!/usr/bin/env python3
"""Check and add the explicit heading IDs shared by all language docs.

Every heading carries an explicit ``{#id}``. English pages define the IDs and
localized pages reuse the ID of the matching English heading, so an anchor link
such as ``vpn_dashboard.md#tunnel-options`` works the same way in every
language.

Usage:
  python scripts/anchors.py check [--lang de ja ...] [--verbose]
  python scripts/anchors.py add --lang en [--dry-run] [pages ...]
  python scripts/anchors.py add --lang de [--dry-run] [pages ...]

``check`` reports headings without an explicit ID, invalid or duplicate IDs,
English IDs missing from a localized page, and anchor links that do not resolve.

``add --lang en`` turns the IDs that Python-Markdown currently generates into
explicit IDs, so rendered URLs do not change. ``add`` for a localized language
copies the IDs from the matching English headings, rewrites anchor links that
used the old localized IDs, and removes ``<a id>`` / ``<span id>`` placeholders
that belong to a heading or that no link uses. Headings it cannot match are
listed for review and need an English-derived ID by hand.
"""

from __future__ import annotations

import argparse
import posixpath
import re
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

import markdown
from markdown.extensions.toc import slugify

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_ROOT = REPO_ROOT / "docs"
SOURCE_LANG = "en"
LANGS = ("en", "de", "es", "fr", "it", "ja", "nl", "pl", "sv", "uk")

# Keep in sync with markdown_extensions in docs/<lang>/mkdocs.yml.
MD_EXTENSIONS = [
    "attr_list",
    "md_in_html",
    "pymdownx.superfences",
    "pymdownx.tabbed",
    "pymdownx.details",
    "toc",
    "admonition",
]
MD_EXTENSION_CONFIGS = {"pymdownx.tabbed": {"alternate_style": True}}

ID_RE = re.compile(r"^[a-z0-9]+(?:[-_][a-z0-9]+)*$")
FENCE_RE = re.compile(r"^[ \t]*(`{3,}|~{3,})")
# A leading BOM is allowed; MkDocs reads pages as utf-8-sig.
HEADING_RE = re.compile(r"^(?P<prefix>\ufeff?[ \t]*#{1,6}[ \t]+)(?P<body>.*?)(?P<trail>[ \t]*)$")
ATTR_RE = re.compile(r"[ \t]*\{:?(?P<attrs>[^}\n]*)\}$")
ATTR_ID_RE = re.compile(r"(?:^|\s)#([^\s}]+)")
LINK_RE = re.compile(r"(\]\()([^)\s#]*)#([^)\s\"]+)")
PLACEHOLDER_RE = re.compile(r'^[ \t]*<(a|span)\s+(?:id|name)="([^"]+)"\s*>\s*</\1>[ \t]*$')
WORD_RE = re.compile(r"[a-z0-9][a-z0-9.+-]*[a-z0-9]|[0-9]")
# Section content that usually stays the same across languages: image and link
# targets, inline code, and bold UI labels.
SECTION_TOKEN_RES = (
    re.compile(r"\]\(([^)\s]+)"),
    re.compile(r'src="([^"]+)"'),
    re.compile(r"`([^`\n]+)`"),
    re.compile(r"\*\*([^*\n]+)\*\*"),
)
# Image URLs contain the language, e.g. /docs/router/de/4/.
LANG_SEGMENT_RE = re.compile(r"/(?:" + "|".join(LANGS) + r")/")
# English-only trailing sections, see EXCLUDED_TRAILING_MARKDOWN_SECTIONS in translation_delta.py.
UNTRANSLATED_TRAILING_IDS = {"regulatory-statements"}


@dataclass
class Heading:
    index: int  # line index in the page
    level: int
    text: str  # heading text without the attribute block
    explicit_id: str | None
    rendered_id: str = ""
    tokens: frozenset[str] = frozenset()  # section content fingerprint


@dataclass
class Page:
    lang: str
    rel: str  # path relative to docs/<lang>/docs, POSIX style
    path: Path
    lines: list[str]
    headings: list[Heading]
    rendered_ids: set[str]
    render_mismatch: bool = False
    changed: bool = False

    @property
    def text(self) -> str:
        return "".join(self.lines)


@dataclass
class Report:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


class _IdCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.heading_ids: list[tuple[int, str]] = []

    def handle_starttag(self, tag, attrs):
        attr_map = dict(attrs)
        if "id" in attr_map:
            self.ids.append(attr_map["id"])
            if re.fullmatch(r"h[1-6]", tag):
                self.heading_ids.append((int(tag[1]), attr_map["id"]))


def front_matter_end(lines: list[str]) -> int:
    """Return the index of the first line after YAML front matter."""
    if not lines or lines[0].strip() != "---":
        return 0
    for index in range(1, len(lines)):
        if lines[index].strip() in ("---", "..."):
            return index + 1
    return 0


def parse_headings(lines: list[str]) -> list[Heading]:
    headings: list[Heading] = []
    fence: str | None = None
    for index in range(front_matter_end(lines), len(lines)):
        line = lines[index].rstrip("\r\n")
        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is not None:
            continue
        match = HEADING_RE.match(line)
        if not match:
            continue
        level = match.group("prefix").strip().count("#")
        body = match.group("body")
        explicit_id = None
        attr_match = ATTR_RE.search(body)
        if attr_match:
            id_match = ATTR_ID_RE.search(attr_match.group("attrs"))
            explicit_id = id_match.group(1) if id_match else None
            body = body[: attr_match.start()]
        headings.append(Heading(index, level, body.strip(), explicit_id))

    for position, heading in enumerate(headings):
        end = headings[position + 1].index if position + 1 < len(headings) else len(lines)
        section = "".join(lines[heading.index + 1 : end])
        heading.tokens = frozenset(
            LANG_SEGMENT_RE.sub("/", token.strip())
            for regex in SECTION_TOKEN_RES
            for token in regex.findall(section)
        )
    return headings


def render_ids(lines: list[str]) -> _IdCollector:
    source = "".join(lines[front_matter_end(lines):]).lstrip("\ufeff")
    html = markdown.markdown(
        source, extensions=MD_EXTENSIONS, extension_configs=MD_EXTENSION_CONFIGS
    )
    collector = _IdCollector()
    collector.feed(html)
    return collector


def load_page(lang: str, path: Path, text: str | None = None) -> Page:
    """Load a page from ``path``, or from ``text`` such as the page in another commit."""
    if text is None:
        text = path.read_bytes().decode("utf-8")
    lines = text.splitlines(keepends=True)
    rel = path.relative_to(DOCS_ROOT / lang / "docs").as_posix()
    headings = parse_headings(lines)
    rendered = render_ids(lines)
    page = Page(lang, rel, path, lines, headings, set(rendered.ids))
    if [h.level for h in headings] == [level for level, _ in rendered.heading_ids]:
        for heading, (_, rendered_id) in zip(headings, rendered.heading_ids):
            heading.rendered_id = rendered_id
    else:
        page.render_mismatch = True
    return page


def translated_headings(en_page: Page) -> list[Heading]:
    """English headings expected in localized pages (drops untranslated trailing sections)."""
    for position, heading in enumerate(en_page.headings):
        if heading.explicit_id in UNTRANSLATED_TRAILING_IDS:
            return en_page.headings[:position]
    return en_page.headings


def load_lang(lang: str, only: set[str] | None = None) -> dict[str, Page]:
    base = DOCS_ROOT / lang / "docs"
    pages = {}
    for path in sorted(base.rglob("*.md")):
        page = load_page(lang, path)
        if only is None or page.rel in only:
            pages[page.rel] = page
    return pages


def resolve_target(page_rel: str, target: str) -> str | None:
    if target == "":
        return page_rel
    if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("/"):
        return None
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(page_rel), target))
    if target.endswith("/") or not resolved.endswith(".md"):
        resolved = posixpath.join(resolved, "index.md")
    return resolved


def iter_links(page: Page):
    """Yield (line index, match) for Markdown anchor links outside code fences."""
    fence: str | None = None
    for index, line in enumerate(page.lines):
        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is None:
            for match in LINK_RE.finditer(line):
                yield index, match


def set_heading_id(page: Page, heading: Heading, new_id: str) -> None:
    page.lines[heading.index] = with_heading_id(page.lines[heading.index], new_id)
    heading.explicit_id = new_id
    page.changed = True


def with_heading_id(raw: str, new_id: str) -> str:
    """Return the heading line ``raw`` with its explicit ID set to ``new_id``."""
    eol = raw[len(raw.rstrip("\r\n")):]
    match = HEADING_RE.match(raw.rstrip("\r\n"))
    body = match.group("body")
    attr_match = ATTR_RE.search(body)
    if attr_match:
        attrs = ATTR_ID_RE.sub("", attr_match.group("attrs")).strip()
        # Bare words such as {custom-anchor} are not IDs; drop them.
        attrs = " ".join(token for token in attrs.split() if token[0] in ".:" or "=" in token)
        attr_block = "{#" + new_id + (" " + attrs if attrs else "") + "}"
        body = body[: attr_match.start()].rstrip() + " " + attr_block
    else:
        body = body.rstrip() + " {#" + new_id + "}"
    return match.group("prefix") + body + eol


def missing_id_fixes(page: Page) -> list[tuple[Heading, str]]:
    """Return (heading, fixed line) for English headings without an explicit ID.

    The fix uses the ID that MkDocs generates for the heading, as ``add --lang en`` does.
    """
    if page.lang != SOURCE_LANG or page.render_mismatch:
        return []
    return [
        (heading, with_heading_id(page.lines[heading.index], heading.rendered_id))
        for heading in page.headings
        if heading.explicit_id is None and heading.rendered_id
    ]


def write_page(page: Page) -> None:
    page.path.write_bytes(page.text.encode("utf-8"))


# --------------------------------------------------------------------------
# check


def check_lang(
    lang: str, pages: dict[str, Page], en_pages: dict[str, Page], report: Report, verbose: bool = False
) -> None:
    for page in pages.values():
        where = f"{lang}/{page.rel}"
        seen: dict[str, int] = {}
        for heading in page.headings:
            line = heading.index + 1
            if heading.explicit_id is None:
                if lang != SOURCE_LANG:
                    hint = "; use the ID of the matching English heading"
                elif heading.rendered_id:
                    hint = f"; add {{#{heading.rendered_id}}}"
                else:
                    hint = ""
                report.errors.append(f"{where}:{line}: heading has no explicit ID: {heading.text}{hint}")
                continue
            if not ID_RE.match(heading.explicit_id):
                report.errors.append(f"{where}:{line}: ID is not lowercase ASCII kebab-case: {heading.explicit_id}")
            if heading.explicit_id in seen:
                report.errors.append(
                    f"{where}:{line}: duplicate ID {heading.explicit_id} (first on line {seen[heading.explicit_id]})"
                )
            seen.setdefault(heading.explicit_id, line)

        if lang != SOURCE_LANG and page.rel in en_pages:
            en_ids = [h.explicit_id for h in translated_headings(en_pages[page.rel]) if h.explicit_id]
            missing = [i for i in en_ids if i not in seen]
            extra = [i for i in seen if i not in en_ids]
            if missing:
                report.errors.append(f"{where}: English IDs missing: {', '.join(missing)}")
            # Localized-only sections legitimately add IDs; list them on request.
            if extra and verbose:
                report.warnings.append(f"{where}: IDs not in English page: {', '.join(extra)}")

        heading_ids = set(seen)
        for index, line in enumerate(page.lines):
            placeholder = PLACEHOLDER_RE.match(line.rstrip("\r\n"))
            if placeholder:
                kind = "duplicates a heading ID" if placeholder.group(2) in heading_ids else "is an HTML placeholder"
                report.warnings.append(f"{where}:{index + 1}: <{placeholder.group(1)} id=\"{placeholder.group(2)}\"> {kind}")

        for index, match in iter_links(page):
            target_rel = resolve_target(page.rel, match.group(2))
            if target_rel is None or target_rel not in pages:
                continue
            fragment = match.group(3)
            if fragment not in pages[target_rel].rendered_ids:
                report.errors.append(f"{where}:{index + 1}: broken anchor link {match.group(2)}#{fragment}")


def cmd_check(args) -> int:
    report = Report()
    en_pages = load_lang(SOURCE_LANG)
    for lang in args.lang:
        pages = en_pages if lang == SOURCE_LANG else load_lang(lang)
        check_lang(lang, pages, en_pages, report, args.verbose)
    for warning in report.warnings:
        print(f"WARNING {warning}")
    for error in report.errors:
        print(f"ERROR {error}")
    print(f"{len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    return 1 if report.errors else 0


# --------------------------------------------------------------------------
# add


def words(text: str) -> set[str]:
    return set(WORD_RE.findall(text.lower()))


def similarity(loc: Heading, en: Heading) -> float:
    """Evidence that two headings are the same section, independent of level."""
    shared = loc.tokens & en.tokens
    content = len(shared) / len(loc.tokens | en.tokens) if shared else 0.0
    return 2.0 * len(words(loc.text) & words(en.text)) + 6.0 * content


def align(en_headings: list[Heading], headings: list[Heading]) -> list[tuple[Heading, Heading | None]]:
    """Match localized headings to English headings.

    Same structure: pair them in order. Otherwise run a global alignment that
    prefers headings of the same level, shared ASCII words (product names,
    numbers, protocols), and shared section content (images, links, code, UI
    labels). Afterwards, swap pairs where a localized heading already carries
    the English ID of another heading and the content agrees with that ID.
    """
    if [h.level for h in en_headings] == [h.level for h in headings]:
        pairs: list[tuple[Heading, Heading | None]] = list(zip(headings, en_headings))
    else:
        pairs = _global_align(en_headings, headings)
    return _apply_explicit_swaps(pairs, en_headings)


def _global_align(en_headings: list[Heading], headings: list[Heading]) -> list[tuple[Heading, Heading | None]]:
    n, m = len(headings), len(en_headings)

    def score(loc: Heading, en: Heading) -> float | None:
        if loc.explicit_id and loc.explicit_id == en.explicit_id:
            return 100.0
        evidence = similarity(loc, en)
        if loc.level == en.level:
            return 1.0 + evidence
        # Older translations sometimes nest a section one level differently.
        return evidence - 1.5 if evidence > 1.5 else None

    best = [[0.0] * (m + 1) for _ in range(n + 1)]
    move = [[""] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        move[i][0] = "up"
    for j in range(1, m + 1):
        move[0][j] = "left"
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            options = [(best[i - 1][j], "up"), (best[i][j - 1], "left")]
            pair = score(headings[i - 1], en_headings[j - 1])
            if pair is not None:
                options.append((best[i - 1][j - 1] + pair, "diag"))
            best[i][j], move[i][j] = max(options, key=lambda option: option[0])

    pairs: list[tuple[Heading, Heading | None]] = []
    i, j = n, m
    while i > 0 or j > 0:
        step = move[i][j]
        if step == "diag":
            pairs.append((headings[i - 1], en_headings[j - 1]))
            i, j = i - 1, j - 1
        elif step == "up":
            pairs.append((headings[i - 1], None))
            i -= 1
        else:
            j -= 1
    pairs.reverse()
    return pairs


def _apply_explicit_swaps(
    pairs: list[tuple[Heading, Heading | None]], en_headings: list[Heading]
) -> list[tuple[Heading, Heading | None]]:
    """Honor existing English IDs on reordered localized sections."""
    en_by_id = {h.explicit_id: h for h in en_headings}
    for position, (loc, en) in enumerate(pairs):
        other = en_by_id.get(loc.explicit_id)
        if en is None or other is None or other is en:
            continue
        partner = next((p for p, (_, e) in enumerate(pairs) if e is other), None)
        if partner is None:
            continue
        loc2 = pairs[partner][0]
        if similarity(loc, other) + similarity(loc2, en) > similarity(loc, en) + similarity(loc2, other):
            pairs[position], pairs[partner] = (loc, other), (loc2, en)
    return pairs


def add_english(pages: dict[str, Page], report: Report) -> None:
    for page in pages.values():
        if page.render_mismatch:
            report.errors.append(f"en/{page.rel}: headings in source and HTML do not match; edit by hand")
            continue
        for heading in page.headings:
            if heading.explicit_id is None or heading.explicit_id != heading.rendered_id:
                set_heading_id(page, heading, heading.rendered_id)


def add_localized(
    lang: str, pages: dict[str, Page], all_pages: dict[str, Page], en_pages: dict[str, Page], report: Report
) -> None:
    id_maps: dict[str, dict[str, str]] = {}
    for page in pages.values():
        where = f"{lang}/{page.rel}"
        en_page = en_pages.get(page.rel)
        if en_page is None:
            report.warnings.append(f"{where}: no English page; add English-derived IDs by hand")
            continue
        if page.render_mismatch:
            report.errors.append(f"{where}: headings in source and HTML do not match; edit by hand")
            continue
        missing_en_ids = [h for h in en_page.headings if not h.explicit_id]
        if missing_en_ids:
            report.errors.append(f"{where}: run 'add --lang en' first")
            continue

        en_headings = translated_headings(en_page)
        en_ids = {h.explicit_id for h in en_page.headings}
        pairs = align(en_headings, page.headings)
        same_structure = [h.level for h in page.headings] == [h.level for h in en_headings]
        id_map: dict[str, str] = {}
        removable: set[int] = set()
        for heading, en_heading in pairs:
            old_ids = {heading.rendered_id, heading.explicit_id} - {None, ""}
            for placeholder_index in placeholders_above(page, heading):
                old_ids.add(PLACEHOLDER_RE.match(page.lines[placeholder_index].rstrip("\r\n")).group(2))
                if en_heading is not None:
                    removable.add(placeholder_index)
            if en_heading is None:
                report.warnings.append(
                    f"{where}:{heading.index + 1}: no matching English heading: {heading.text}"
                )
                continue
            if heading.explicit_id in en_ids and heading.explicit_id != en_heading.explicit_id:
                # An existing English ID was set on purpose; never overwrite it.
                report.warnings.append(
                    f"{where}:{heading.index + 1}: kept ID {heading.explicit_id} (alignment suggested {en_heading.explicit_id})"
                )
                continue
            if heading.explicit_id and heading.explicit_id != en_heading.explicit_id:
                report.warnings.append(
                    f"{where}:{heading.index + 1}: replaced ID {heading.explicit_id} with {en_heading.explicit_id}"
                )
            if heading.explicit_id != en_heading.explicit_id:
                set_heading_id(page, heading, en_heading.explicit_id)
            for old_id in old_ids:
                id_map.setdefault(old_id, en_heading.explicit_id)
        if not same_structure:
            matched_en = {id(e) for _, e in pairs if e is not None}
            skipped = [h.explicit_id for h in en_headings if id(h) not in matched_en]
            if skipped:
                report.warnings.append(
                    f"{where}: structure differs from English; English headings not matched: {', '.join(skipped)}"
                )
        id_maps[page.rel] = id_map
        remove_placeholders(page, removable)

    for page in pages.values():
        rewrite_links(page, all_pages, id_maps, report)

    # Placeholders that no link targets any more are dead weight.
    referenced: set[tuple[str, str]] = set()
    for page in all_pages.values():
        for _, match in iter_links(page):
            target_rel = resolve_target(page.rel, match.group(2))
            if target_rel is not None:
                referenced.add((target_rel, match.group(3)))
    for page in pages.values():
        unused = set()
        for index, line in enumerate(page.lines):
            placeholder = PLACEHOLDER_RE.match(line.rstrip("\r\n"))
            if placeholder and (page.rel, placeholder.group(2)) not in referenced:
                unused.add(index)
        remove_placeholders(page, unused)


def placeholders_above(page: Page, heading: Heading) -> list[int]:
    """Return line indexes of placeholders directly above a heading."""
    found: list[int] = []
    index = heading.index - 1
    while index >= 0:
        line = page.lines[index]
        if line.strip() == "":
            index -= 1
            continue
        if PLACEHOLDER_RE.match(line.rstrip("\r\n")):
            found.append(index)
            index -= 1
            continue
        break
    return found


def remove_placeholders(page: Page, removable: set[int]) -> None:
    if not removable:
        return
    keep: list[str] = []
    skip_blank = False
    for index, line in enumerate(page.lines):
        if index in removable:
            # Drop the blank line that separated the placeholder from the heading.
            skip_blank = bool(keep) and keep[-1].strip() == ""
            continue
        if skip_blank and line.strip() == "":
            skip_blank = False
            continue
        skip_blank = False
        keep.append(line)
    page.lines[:] = keep
    page.headings = parse_headings(page.lines)
    page.changed = True


def rewrite_links(page: Page, all_pages: dict[str, Page], id_maps: dict[str, dict[str, str]], report: Report) -> None:
    for index, line in enumerate(page.lines):
        def replace(match: re.Match) -> str:
            target_rel = resolve_target(page.rel, match.group(2))
            fragment = match.group(3)
            if target_rel is None or target_rel not in all_pages:
                return match.group(0)
            target = all_pages[target_rel]
            heading_ids = {h.explicit_id for h in target.headings}
            # Map old IDs first so the link keeps pointing at the section it
            # pointed at before, even if that old ID is now another heading's ID.
            id_map = id_maps.get(target_rel, {})
            new_fragment = fragment
            # Localized links often spell the slug with non-ASCII characters
            # (#verbindung-prüfen) that Python-Markdown never generated.
            for candidate in (fragment, unquote(fragment), slugify(unquote(fragment), "-")):
                if candidate in id_map:
                    new_fragment = id_map[candidate]
                    break
            if new_fragment not in heading_ids | target.rendered_ids:
                report.warnings.append(
                    f"{page.lang}/{page.rel}:{index + 1}: unresolved anchor link {match.group(2)}#{fragment}"
                )
            return match.group(1) + match.group(2) + "#" + new_fragment

        new_line = LINK_RE.sub(replace, line)
        if new_line != line:
            page.lines[index] = new_line
            page.changed = True


def cmd_add(args) -> int:
    report = Report()
    lang = args.lang
    only = {p.replace("\\", "/") for p in args.pages} or None
    all_pages = load_lang(lang)
    pages = {rel: page for rel, page in all_pages.items() if only is None or rel in only}
    if lang == SOURCE_LANG:
        add_english(pages, report)
    else:
        add_localized(lang, pages, all_pages, load_lang(SOURCE_LANG), report)

    changed = [page for page in pages.values() if page.changed]
    if not args.dry_run:
        for page in changed:
            write_page(page)
    for warning in report.warnings:
        print(f"WARNING {warning}")
    for error in report.errors:
        print(f"ERROR {error}")
    action = "would change" if args.dry_run else "changed"
    print(f"{action} {len(changed)} page(s); {len(report.errors)} error(s), {len(report.warnings)} warning(s)")
    return 1 if report.errors else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check", help="report heading ID and anchor link problems")
    check.add_argument("--lang", nargs="+", default=list(LANGS), choices=LANGS)
    check.add_argument("--verbose", action="store_true", help="also list IDs that exist only in a localized page")
    check.set_defaults(func=cmd_check)

    add = sub.add_parser("add", help="add explicit heading IDs")
    add.add_argument("--lang", required=True, choices=LANGS)
    add.add_argument("--dry-run", action="store_true")
    add.add_argument("pages", nargs="*", help="pages relative to docs/<lang>/docs")
    add.set_defaults(func=cmd_add)

    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
