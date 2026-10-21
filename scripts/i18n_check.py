#!/usr/bin/env python3
"""Check that localized pages keep the structure of the English pages.

Usage:
  python scripts/i18n_check.py [--show-allowed] [pages ...] [--lang de ja ...]

Structure checks compare each localized page with its English page, section by
section (a section is the content between two headings, matched by heading ID):

  section-order    English heading IDs appear in a different order
  missing-section  an English section is missing
  extra-section    a section has an ID that is not in the English page
  images           image URLs differ (the language segment is ignored)
  admonitions      !!! / ??? / === blocks differ in number or type
  code             fenced code blocks differ
  tables           table count or row counts differ
  links            link targets differ (order within a section is ignored)
  values           IP addresses or version numbers differ

File checks:

  orphan           a localized page has no English page
  missing-page     an English page has no localized page
  redirect-shadowed  a redirect_maps source path is a real page
  redirect-target  a redirect_maps target page or anchor does not exist
  redirect-mismatch  redirect_maps differs from the English mkdocs.yml

English-only trailing sections (Regulatory Statements) and localized-only legal
sections (Declaration of Conformity, safety information) are not compared.
Intentional differences go in scripts/i18n_allowlist.yml with a reason.
"""

from __future__ import annotations

import argparse
import posixpath
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from anchors import (
    DOCS_ROOT,
    FENCE_RE,
    LANG_SEGMENT_RE,
    LANGS,
    SOURCE_LANG,
    Page,
    front_matter_end,
    load_lang,
    resolve_target,
    translated_headings,
)

ALLOWLIST_PATH = Path(__file__).resolve().parent / "i18n_allowlist.yml"
EXCLUDED_PAGES = {"downloads/index.md"}
# Legal sections that exist only in localized pages, together with their subsections.
LOCALIZED_ONLY_IDS = {"declaration-of-conformity", "safety-information"}

IMAGE_RES = (
    re.compile(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)"),
    re.compile(r"<img\b[^>]*?\bsrc=\"([^\"]+)\""),
)
# Markdown links that are not images; reference-style links are not used in these docs.
LINK_RES = (
    re.compile(r"(?<!!)\[(?:[^\]\[]|\[[^\]]*\])*\]\(\s*<?([^)\s>]+)"),
    re.compile(r"<a\b[^>]*?\bhref=\"([^\"]+)\""),
)
ADMONITION_RE = re.compile(r"^[ \t]*(!!!|\?\?\?\+?|===\+?)[ \t]*(\S*)")
TABLE_SEPARATOR_RE = re.compile(r"^\|?[ \t]*:?-{3,}:?[ \t]*(\|[ \t]*:?-{3,}:?[ \t]*)*\|?$")
HTML_ROW_RE = re.compile(r"<tr\b", re.I)
# ASCII boundaries, because Japanese text has no spaces around numbers.
# Decimal numbers like 2.4 GHz are written 2,4 in several languages, so only
# values that never change in translation are compared.
VALUE_RES = (
    re.compile(r"(?<![A-Za-z0-9_.])\d{1,3}(?:\.\d{1,3}){3}(?:/\d{1,2})?(?::\d+)?(?![A-Za-z0-9_]|\.[A-Za-z0-9])"),
    re.compile(r"(?<![A-Za-z0-9_.])[vV]?\d+\.\d+\.\d+(?:\.\d+)?(?![A-Za-z0-9_]|\.[A-Za-z0-9])"),
    re.compile(r"(?<![A-Za-z0-9_.])[vV]\d+\.\d+(?:\.[xX\d]+)?(?![A-Za-z0-9_]|\.[A-Za-z0-9])"),
)
# Full-line comments in code blocks may be translated.
COMMENT_RE = re.compile(r"^\s*(#|//)(?!!)")
# Docs URLs after normalize_url() removed the language segment.
DOCS_URL_RE = re.compile(r"^https?://docs\.gl-inet\.com/router/4/([^#?]*)(#.*)?$")
LOCALE_RE = re.compile(r"(?<=/)[a-z]{2}-[a-z]{2}(?=/)|(?<=[?&]hl=)[a-zA-Z-]+")
# Removed from prose before looking for values.
URL_RE = re.compile(r"\]\([^)]*\)|https?://\S+|<[a-zA-Z][^>]*>")


@dataclass
class Section:
    id: str  # "" for content above the first heading
    line: int  # 1-based line of the heading
    images: list[str] = field(default_factory=list)
    admonitions: list[str] = field(default_factory=list)
    code: list[str] = field(default_factory=list)
    tables: list[str] = field(default_factory=list)
    links: list[str] = field(default_factory=list)
    values: list[str] = field(default_factory=list)
    prose: list[str] = field(default_factory=list)  # text outside code blocks, without URLs


@dataclass
class Issue:
    lang: str
    page: str
    check: str
    message: str
    section: str | None = None
    line: int | None = None

    def __str__(self) -> str:
        where = f"{self.lang}/{self.page}"
        if self.line:
            where += f":{self.line}"
        if self.section:
            where += f" #{self.section}"
        return f"{where}: [{self.check}] {self.message}"


# --------------------------------------------------------------------------
# allowlist


@dataclass
class AllowEntry:
    langs: set[str]
    page: str
    check: str
    section: str | None
    reason: str
    used: bool = False

    def matches(self, issue: Issue) -> bool:
        return (
            (issue.lang in self.langs or "*" in self.langs)
            and self.page == issue.page
            and self.check == issue.check
            and (self.section is None or self.section == issue.section)
        )


def load_allowlist(path: Path) -> list[AllowEntry]:
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    entries = []
    for number, item in enumerate(data, 1):
        if not item.get("reason"):
            raise SystemExit(f"{path.name}: entry {number} has no reason")
        langs = item["lang"]
        entries.append(
            AllowEntry(
                langs=set(langs if isinstance(langs, list) else [langs]),
                page=item["page"],
                check=item["check"],
                section=item.get("section"),
                reason=item["reason"],
            )
        )
    return entries


# --------------------------------------------------------------------------
# structure


def normalize_url(url: str) -> str:
    url = LANG_SEGMENT_RE.sub("/", url.strip().replace("&amp;", "&"))
    # Localized links to external help pages often use the reader's locale.
    return LOCALE_RE.sub("*", url)


def normalize_link(page_rel: str, url: str) -> str:
    """Return docs links as page paths, so relative, absolute and redirected links compare equal."""
    url = normalize_url(url)
    redirects = english_redirects()
    match = DOCS_URL_RE.match(url)
    if match:
        path = match.group(1).strip("/")
        rel = f"{path}.md" if path else "index.md"
        if not (DOCS_ROOT / SOURCE_LANG / "docs" / rel).exists() and rel not in redirects:
            rel = posixpath.join(path, "index.md")
        fragment = match.group(2) or ""
    else:
        target, _, fragment = url.partition("#")
        rel = resolve_target(page_rel, target)
        if rel is None:
            return url
        fragment = "#" + fragment if fragment else ""
    if rel in redirects:
        redirected, _, redirected_fragment = redirects[rel].partition("#")
        rel = redirected
        fragment = fragment or ("#" + redirected_fragment if redirected_fragment else "")
    return rel + fragment


_english_redirects: dict[str, str] | None = None


def english_redirects() -> dict[str, str]:
    global _english_redirects
    if _english_redirects is None:
        _english_redirects = redirect_map(SOURCE_LANG)
    return _english_redirects


def dedent(lines: list[str]) -> str:
    body = [line.rstrip() for line in lines if not COMMENT_RE.match(line)]
    indent = min((len(line) - len(line.lstrip()) for line in body if line.strip()), default=0)
    return "\n".join(line[indent:] for line in body).strip("\n")


def sections_of(page: Page, en_ids: set[str] | None) -> list[Section]:
    """Split a page into sections and collect the structure of each one.

    For English pages pass ``en_ids=None``; trailing English-only sections are
    dropped. For localized pages, localized-only legal sections are dropped.
    """
    headings = page.headings
    if en_ids is None:
        kept = translated_headings(page)
        cut = headings[len(kept)].index if len(kept) < len(headings) else len(page.lines)
        headings = kept
    else:
        cut = len(page.lines)

    starts = [(front_matter_end(page.lines), "", 0)]
    boundaries = {cut}
    skip_level = None
    for heading in headings:
        boundaries.add(heading.index)
        if skip_level is not None and heading.level > skip_level:
            continue
        skip_level = None
        if en_ids is not None and heading.explicit_id in LOCALIZED_ONLY_IDS:
            skip_level = heading.level
            continue
        starts.append((heading.index, heading.explicit_id or "", heading.index + 1))

    sections = []
    for start, section_id, line in starts:
        # A section ends at the next heading, including skipped legal sections.
        body_start = start + 1 if section_id else start
        end = min(b for b in boundaries if b >= body_start)
        sections.append(collect(page.rel, section_id, line, page.lines[body_start:end]))
    return sections


def collect(page_rel: str, section_id: str, line: int, lines: list[str]) -> Section:
    section = Section(section_id, line)
    fence: str | None = None
    code: list[str] = []
    table_rows = 0
    for raw in lines + [""]:
        text = raw.rstrip("\r\n")
        fence_match = FENCE_RE.match(text)
        if fence is not None:
            if fence_match and fence_match.group(1)[0] == fence[0] and len(fence_match.group(1)) >= len(fence):
                section.code.append(dedent(code))
                fence, code = None, []
            else:
                code.append(text)
            continue
        if fence_match:
            fence, code = fence_match.group(1), []
            continue

        stripped = text.strip()
        if stripped.startswith("|"):
            if not TABLE_SEPARATOR_RE.match(stripped):
                table_rows += 1
        elif table_rows:
            section.tables.append(f"{table_rows} rows")
            table_rows = 0

        admonition = ADMONITION_RE.match(text)
        if admonition:
            marker, word = admonition.groups()
            kind = marker.rstrip("+")
            if marker.startswith("!") or marker.startswith("?"):
                if word and not word.startswith('"'):
                    kind += " " + word.lower()
            section.admonitions.append(kind)

        for regex in IMAGE_RES:
            section.images.extend(normalize_url(url) for url in regex.findall(text))
        for regex in LINK_RES:
            section.links.extend(normalize_link(page_rel, url) for url in regex.findall(text))
        prose = URL_RE.sub(" ", text)
        section.prose.append(prose)
        for regex in VALUE_RES:
            section.values.extend(value.lower().lstrip("v") for value in regex.findall(prose))
    html_rows = sum(len(HTML_ROW_RE.findall(raw)) for raw in lines)
    if html_rows:
        section.tables.append(f"{html_rows} HTML rows")
    return section


def short(item: str, width: int = 70) -> str:
    item = item.replace("\n", "\\n")
    item = re.sub(r"^https?://", "", item)
    return item if len(item) <= width else "…" + item[-(width - 1):]


def describe(en: list, loc: list, ordered: bool = True) -> str | None:
    if en == loc or (not ordered and Counter(en) == Counter(loc)):
        return None
    missing = list((Counter(en) - Counter(loc)).elements())
    extra = list((Counter(loc) - Counter(en)).elements())
    if not missing and not extra:
        for position, (a, b) in enumerate(zip(en, loc)):
            if a != b:
                return f"order differs at #{position + 1}: English {short(str(a))}, localized {short(str(b))}"
    parts = [f"English {len(en)}, localized {len(loc)}"]
    if missing:
        parts.append("missing " + ", ".join(short(str(i)) for i in missing[:4]) + (" …" if len(missing) > 4 else ""))
    if extra:
        parts.append("extra " + ", ".join(short(str(i)) for i in extra[:4]) + (" …" if len(extra) > 4 else ""))
    return "; ".join(parts)


def check_structure(lang: str, page: Page, en_page: Page, issues: list[Issue]) -> None:
    en_sections = sections_of(en_page, None)
    en_ids = {s.id for s in en_sections}
    loc_sections = sections_of(page, en_ids)
    loc_by_id = {s.id: s for s in loc_sections}

    def add(check: str, message: str, section: Section | None = None) -> None:
        issues.append(
            Issue(lang, page.rel, check, message, section.id if section else None, section.line if section else None)
        )

    for section in loc_sections:
        if section.id not in en_ids:
            add("extra-section", "section is not in the English page", section)
    missing = [s.id for s in en_sections if s.id not in loc_by_id]
    if missing:
        add("missing-section", ", ".join(missing))
    en_order = [s.id for s in en_sections if s.id in loc_by_id]
    loc_order = [s.id for s in loc_sections if s.id in en_ids]
    if en_order != loc_order:
        add("section-order", describe(en_order, loc_order) or "")

    for en_section in en_sections:
        section = loc_by_id.get(en_section.id)
        if section is None:
            continue
        for check, ordered in (
            ("images", True),
            ("admonitions", True),
            ("tables", True),
            ("links", False),
        ):
            message = describe(getattr(en_section, check), getattr(section, check), ordered)
            if message:
                add(check, message, section)
        if len(en_section.code) != len(section.code):
            add("code", f"English {len(en_section.code)} block(s), localized {len(section.code)}", section)
        else:
            for position, (en_code, code) in enumerate(zip(en_section.code, section.code), 1):
                if en_code != code:
                    first = next(
                        (a, b) for a, b in zip(en_code.splitlines() + [""], code.splitlines() + [""]) if a != b
                    )
                    add("code", f"block {position} differs: English {short(first[0])!r}, localized {short(first[1])!r}", section)
        # Translations may drop the "v" of "v4.2" ("versión 4.2"), so look for
        # the bare number in the other text instead of comparing matches.
        missing = sorted({v for v in en_section.values if not mentions(section, v)})
        extra = sorted({v for v in section.values if not mentions(en_section, v)})
        if missing or extra:
            parts = (["missing " + ", ".join(missing)] if missing else []) + (["extra " + ", ".join(extra)] if extra else [])
            add("values", "; ".join(parts), section)


def mentions(section: Section, value: str) -> bool:
    pattern = re.compile(r"(?<![A-Za-z0-9_.])[vV]?" + re.escape(value) + r"(?![A-Za-z0-9_]|\.[A-Za-z0-9])")
    return any(pattern.search(line) for line in section.prose)


# --------------------------------------------------------------------------
# files and redirects


def redirect_map(lang: str) -> dict[str, str]:
    config = yaml.load((DOCS_ROOT / lang / "mkdocs.yml").read_text(encoding="utf-8"), Loader=_Loader)
    for plugin in config.get("plugins", []):
        if isinstance(plugin, dict) and "redirects" in plugin:
            return dict((plugin["redirects"] or {}).get("redirect_maps") or {})
    return {}


class _Loader(yaml.SafeLoader):
    """Safe loader that ignores MkDocs-specific tags such as !ENV."""


_Loader.add_multi_constructor("", lambda loader, suffix, node: None)


def check_files(lang: str, pages: dict[str, Page], en_pages: dict[str, Page], issues: list[Issue]) -> None:
    if lang != SOURCE_LANG:
        for rel in sorted(set(pages) - set(en_pages) - EXCLUDED_PAGES):
            issues.append(Issue(lang, rel, "orphan", "page has no English page; delete it or add a redirect"))
        for rel in sorted(set(en_pages) - set(pages) - EXCLUDED_PAGES):
            issues.append(Issue(lang, rel, "missing-page", "English page has no translation"))

    redirects = redirect_map(lang)
    config = "mkdocs.yml"
    if lang != SOURCE_LANG:
        en_redirects = redirect_map(SOURCE_LANG)
        for source in sorted(set(en_redirects) | set(redirects)):
            if en_redirects.get(source) != redirects.get(source):
                issues.append(
                    Issue(lang, config, "redirect-mismatch",
                          f"{source}: English {en_redirects.get(source)!r}, localized {redirects.get(source)!r}")
                )
    for source, target in sorted(redirects.items()):
        if source in pages:
            issues.append(Issue(lang, config, "redirect-shadowed", f"{source} is a real page; the redirect never applies"))
        if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
            continue
        target_page, _, fragment = target.partition("#")
        target_rel = resolve_target("index.md", target_page)
        if target_rel not in pages:
            issues.append(Issue(lang, config, "redirect-target", f"{source}: target page {target_page} does not exist"))
        elif fragment and fragment not in pages[target_rel].rendered_ids:
            issues.append(Issue(lang, config, "redirect-target", f"{source}: anchor {target} does not exist"))


# --------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--lang", nargs="+", default=list(LANGS), choices=LANGS)
    parser.add_argument("--show-allowed", action="store_true", help="also list allowlisted differences")
    parser.add_argument("pages", nargs="*", help="limit structure checks to these pages (relative to docs/<lang>/docs)")
    args = parser.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    only = {p.replace("\\", "/") for p in args.pages}
    allowlist = load_allowlist(ALLOWLIST_PATH)
    en_pages = load_lang(SOURCE_LANG)
    issues: list[Issue] = []
    for lang in args.lang:
        pages = en_pages if lang == SOURCE_LANG else load_lang(lang)
        if not only:
            check_files(lang, pages, en_pages, issues)
        if lang == SOURCE_LANG:
            continue
        for rel, page in pages.items():
            if rel in EXCLUDED_PAGES or rel not in en_pages or (only and rel not in only):
                continue
            check_structure(lang, page, en_pages[rel], issues)

    errors, allowed = [], []
    for issue in issues:
        entry = next((e for e in allowlist if e.matches(issue)), None)
        if entry:
            entry.used = True
            allowed.append((issue, entry))
        else:
            errors.append(issue)

    if args.show_allowed:
        for issue, entry in allowed:
            print(f"ALLOWED {issue} ({entry.reason})")
    unused = []
    if not only and set(args.lang) >= set(LANGS) - {SOURCE_LANG}:
        unused = [e for e in allowlist if not e.used]
        for entry in unused:
            print(f"WARNING unused allowlist entry: {sorted(entry.langs)} {entry.page} [{entry.check}]")
    for issue in errors:
        print(f"ERROR {issue}")
    print(f"{len(errors)} error(s), {len(allowed)} allowed, {len(unused)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
