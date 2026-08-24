"""Build page-aware links for the Material language selector.

Material renders ``extra.alternate`` as plain links, so every entry points at
the target language's home page. This hook resolves, for each page, whether the
same source file exists in the sibling language project (``docs/<lang>/docs``)
and, if so, points the link at the equivalent page instead. Entries whose target
language does not have the page keep the original home-page link, so an
untranslated page never produces a 404.

Shared by all language configs via ``hooks: - ../../scripts/alternate_links.py``.
"""

import os
import posixpath


def _lang_dir(link):
    """Return the language directory from a link such as ``/router/jp/4/``.

    The directory name is used instead of ``alt.lang`` because Japanese is
    published under ``jp`` while its language code is ``ja``.
    """
    parts = [part for part in link.split("/") if part]
    return parts[1] if len(parts) > 1 else None


def on_page_context(context, page, config, nav):
    alternates = (config.get("extra") or {}).get("alternate") or []
    if not alternates:
        return context

    # docs/<lang>/docs -> docs/
    langs_root = os.path.dirname(os.path.dirname(os.path.abspath(config["docs_dir"])))
    src_parts = page.file.src_path.replace(os.sep, "/").split("/")

    resolved = []
    for alt in alternates:
        link = alt.get("link", "")
        lang_dir = _lang_dir(link)
        if lang_dir and os.path.isfile(
            os.path.join(langs_root, lang_dir, "docs", *src_parts)
        ):
            # page.url is '' on the home page, 'faq/debrick/' elsewhere.
            link = posixpath.join(link, page.url)
        resolved.append({**alt, "link": link})

    context["alternate_links"] = resolved
    return context
