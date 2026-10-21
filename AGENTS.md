# Agent Instructions for GL.iNet Documentation

This repository contains GL.iNet router documentation built with MkDocs. These rules apply to general documentation editing, whether the change is for English source docs, localized docs, navigation, images, or supporting scripts.

## Repository Expectations

- Produce publishable technical support documentation.
- Keep product behavior, security notes, warnings, limits, and setup workflows technically accurate.
- Do not add product claims, troubleshooting advice, compatibility statements, or behavioral explanations unless they are supported by the source material or nearby documentation.
- Prefer concise, neutral, instructional wording over conversational or marketing-heavy language.
- Preserve exact product names, model names, firmware versions, IP addresses, URLs, port numbers, file names, protocol names, and option values.

## Markdown and Structure

- Preserve Markdown structure unless the requested change requires otherwise.
- Keep headings, callouts, numbered steps, bullet lists, tables, image references, links, and separators coherent with nearby pages.
- Preserve admonition blocks such as `!!! Note` and keep their content complete.
- Keep image URLs and relative links unchanged unless the target file or path intentionally changes.

## Heading IDs and Anchor Links

- Every Markdown heading in every language, including English, carries an explicit ID, for example `## Port Forwards {#port-forwards}`. Always include the `#`; `{port-forwards}` without `#` does not set an ID.
- English is the source of heading IDs. A localized heading uses the same ID as the matching English heading: translate the heading text, never the ID.
- IDs are lowercase ASCII kebab-case and unique within the page. For a new heading, derive the ID from the English heading text. For a heading that exists only in a localized page, derive the ID from an English rendering of that heading.
- Do not change an existing ID when heading wording changes, because links and bookmarks depend on it. If an ID must change, update it in every language and update every link that uses it.
- Anchor links use the shared ID in every language, for example `[Tunnel-Optionen](vpn_dashboard.md#tunnel-options)`. Do not add `<a id>` or `<span id>` placeholders for headings.
- After adding or editing headings or anchor links, run `python scripts/anchors.py check`.

## UI Labels and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- Keep left-navigation paths aligned with the product UI, for example: `**VPN** -> **VPN Dashboard**`.
- If a button or menu label is visibly English in the UI, it is acceptable to keep the label in English in localized docs.
- Do not invent localized UI labels that are not shown in the product.
- Distinguish between explanatory prose and literal UI labels.

## Editing Workflow

- Read enough surrounding context before editing a page.
- Prefer updating the existing matching page instead of creating a different structure unless a new page is required.
- Keep related localized and English documentation structures compatible when the change naturally affects multiple languages.
- When editing shared scripts or automation, update hard-coded documentation paths that depend on moved files.
- Before finishing, scan for broken links, malformed Markdown, missing images, and accidental mixed-language fragments when those risks are relevant.

## Translation Work

Use the `glinet-docs-translation` skill for translation-specific tasks, including translating English docs into localized docs, syncing English changes into localized files, or reviewing localized translation quality. Keep detailed translation workflow and language terminology rules in that skill, not in this default repository guidance.

After adding, renaming, or deleting pages, editing `redirect_maps`, or changing localized pages, run `python scripts/i18n_check.py`. It compares each localized page with the English page section by section (images, admonitions, code blocks, tables, links, IP addresses, and version numbers) and reports orphan pages and broken redirects. Fix the translation; add an entry to `scripts/i18n_allowlist.yml` only for intentional differences, with a reason.
