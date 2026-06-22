---
name: glinet-docs-translation
description: Translate, sync, or review GL.iNet router documentation between English source files and localized docs. Use when Codex is asked to translate English docs into German, Spanish, French, Italian, Japanese, or Polish; update localized docs after changes under docs/en/**; improve machine-translated localized pages; or check localized terminology, UI labels, Markdown structure, links, and technical accuracy.
---

# GL.iNet Docs Translation

Use this skill for translation-specific work only. For ordinary documentation edits that do not translate, sync, or review localized content, follow the repository `AGENTS.md` instead.

## References

Always read `references/common.md` before translating or reviewing localized docs.

Read the target-language reference before editing that language:

- German: `references/german.md`
- Spanish: `references/spanish.md`
- French: `references/french.md`
- Italian: `references/italian.md`
- Japanese: `references/japanese.md`
- Polish: `references/polish.md`

If a task touches multiple languages, read `references/common.md` once and then read each relevant language reference.

## Workflow

1. Identify the English source file and the target localized file.
2. Read the full English source before translating or syncing.
3. Read the existing localized file when it exists, including nearby sections that establish terminology.
4. Preserve the English source structure unless the localized docs intentionally differ.
5. Translate or update the localized prose with natural, professional target-language wording.
6. Preserve UI labels, product names, technical values, links, images, tables, admonitions, and custom anchors.
7. Remove machine-translation artifacts and unintended source-language fragments.
8. Check that technical behavior, warnings, limits, routing logic, security notes, and default states still match the English source.

## Path Conventions

- English source docs live under the language root `docs/en/`, including `mkdocs.yml`, homepage overrides, and page content under `docs/en/docs/`.
- Localized docs live under the language roots `docs/de/`, `docs/es/`, `docs/fr/`, `docs/it/`, `docs/jp/`, and `docs/pl/`.
- For page content, prefer updating the matching localized path under the target language's `docs/` subdirectory. Create a new localized page only when the English source introduces a page that does not yet exist.
- For language-level files such as `mkdocs.yml` or homepage overrides, update the matching file under the target language root when it exists.

## Final Check

Before finishing a translation task, verify:

- The target-language text reads naturally from start to finish.
- No unintended source-language artifacts remain in prose.
- UI labels, links, images, Markdown formatting, and admonitions are preserved correctly.
- Technical behavior and security notes still match the English source.
- Terminology is consistent within the file and with nearby localized docs.
