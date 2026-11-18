# Common Translation Rules

This repository contains localized GL.iNet router documentation. When translating documentation from English into another language, follow the rules below.

## Scope

- These instructions apply to translation work across localized docs in this repository.
- Treat `docs/en/` as the English source root, including `mkdocs.yml`, homepage overrides, and page content under `docs/en/docs/`.
- Prefer updating the matching localized file instead of creating a different structure unless the English source introduces a new page.
- Keep the translated document functionally equivalent to the English source.

## Primary Goal

- Produce publishable technical documentation, not literal sentence-by-sentence translation.
- Preserve the original meaning, user workflow, warnings, and technical accuracy.
- Remove machine-translation artifacts completely. Do not leave mixed source-language fragments in the target-language prose unless they are intentional product or protocol names.

## Writing Style

- Write in natural, professional documentation style for the target language.
- Use clear instructional wording for setup steps and UI guidance.
- Prefer concise, neutral phrasing over conversational or marketing-heavy language.
- Keep tone consistent across the whole page.
- Avoid overly literal translations that sound unnatural in the target language.

## Product Names and Technical Terms

- Keep product names, model names, protocol names, brand names, and standards unchanged unless the target language has a well-established official localized form.
- Preserve exact technical values such as model numbers, firmware versions, IP addresses, URLs, port numbers, file names, and protocol names.
- Be consistent with core networking terminology within one file and across nearby localized pages.
- If a technical term should remain in English for usability or product consistency, keep it unchanged.

## UI Labels and Navigation

- Preserve actual product UI labels when they appear in screenshots or navigation paths.
- Keep left-navigation paths aligned with the English source, for example: `**VPN** -> **VPN Dashboard**`.
- If a button or menu label is visibly English in the UI, it is acceptable to keep the label in English.
- Do not invent localized UI labels that are not shown in the product.
- Distinguish between explanatory translated text and literal UI labels.

## Markdown and Structure

- Preserve the original Markdown structure unless there is a strong reason to change it.
- Keep headings, callouts, numbered steps, bullet lists, tables, image references, links, and separators aligned with the English source.
- Do not drop sections from the English source.
- Do not add new product claims, troubleshooting advice, or unsupported explanations.
- Preserve admonition blocks such as `!!! Note` and keep their content complete.
- Keep image URLs unchanged.
- Keep relative links unchanged unless the localized file name or target path is intentionally different.

## Internal Links and Anchors

Heading IDs follow the current English title in lowercase ASCII kebab-case,
unique within the page. A title-driven ID change is normal sync work and needs
no separate approval or migration list. The cache is a translation baseline,
not an authority for restoring old IDs. An ID difference from the cache alone
is not a blocking source issue.

Repeated subheadings may include the current English parent section as an ID
prefix. Under AmneziaWG V2.0, `Parameters` and `Overview` may use
`amneziawg-v20-parameters` and `amneziawg-v20-overview`; under V3.1 they may use
`amneziawg-v31-parameters` and `amneziawg-v31-overview`. These IDs follow the
current title plus its section context and are valid without lengthening the
visible headings. Do not treat the context prefix as a title/ID mismatch or
strip it merely to match a title-only slug. Update affected scoped IDs and
references when the English title or parent context changes. Localized headings
still copy the complete English ID, including its context prefix.

Match old/current sections using full pages and surrounding content. Copy the
current English ID to localized headings and update inbound anchor links and
redirects to the affected page in every language, including files outside the
initial cache delta. Do not replace the same ID on unrelated pages. Do not keep
old IDs or add aliases solely for external bookmarks; unchanged headings need
no bulk rewrite. Protected localized-only legal sections keep their wording,
placement and IDs. If the section mapping is ambiguous, the English ID does
not follow its changed title and section context, or an English link needs correction outside the
task's scope, report that specific source issue instead of silently changing
English. Unresolved broken links still prevent completion.


- Every heading carries an explicit ID copied from the matching English heading, for example `## Перенаправлення портів {#port-forwards}`. Translate the heading text; never translate, drop, or reword the `{#id}`.
- Anchor links in localized pages use the same English IDs as the English page. Do not rewrite them to localized slugs.
- A heading that exists only in the localized page gets a lowercase ASCII kebab-case ID derived from an English rendering of the heading, unique within the page.
- Do not add `<a id>` or `<span id>` placeholders for headings.
- Keep cross-page links valid within the localized docs tree.
- Run `python scripts/anchors.py check --lang <lang>` before finishing. It reports headings without IDs, IDs that differ from English, and anchor links that do not resolve.

## Tables, Lists, and Data

- Preserve model lists, feature matrices, firmware versions, option names, and port ranges exactly.
- Do not reorder data unless the English source changed order for a reason.
- Do not translate values that should remain exact.

## Technical Accuracy Rules

- Do not simplify away conditions, limits, or safety implications.
- Preserve wording about security behavior, failover behavior, routing logic, and access restrictions accurately.
- Be precise with words like `all`, `only`, `must`, `default`, `enabled`, `disabled`, `fail over`, and `does not`.
- When the English source describes routing logic or policy priority, translate it with extra care so the behavior remains unambiguous.

## Translation Workflow

- Read the full English source before translating.
- Review nearby localized pages for terminology consistency.
- Translate the whole section with context, not isolated sentences.
- If the existing localized page is low quality, do not mimic its mistakes. Use the English source and better target-language prose instead.
- After editing, scan for mixed-language leftovers, broken links, and terminology drift.

## Downloads Partial Sync

- This rule applies only to `de`, `es`, `fr`, `pl`, `it`, and `ja`, using `docs/en/docs/downloads/index.md` as the source and `docs/<lang>/docs/downloads/index.md` as the target. It overrides whole-page structure alignment, translation, and cleanup rules for this page. Apply it to the requested languages within this set, not to unrelated languages outside the task. `nl`, `sv`, and `uk` retain their whole-page Downloads exclusion and existing language-specific rules.
- Sync the `User Manual` heading, the two opening explanatory paragraphs (manual availability and download instructions), and the firmware-change/warranty disclaimer before the model download list. Preserve the shared heading ID and existing YAML front matter.
- The boundary is the first top-level unordered model-download link after the front matter, currently `- [GL-...](...)`. The boundary itself and everything following it are manually maintained in each locale. Preserve that entire suffix byte-for-byte, including model names, list entries, ordering, labels, all download URLs, locale-specific paths and PDF filenames, attributes such as `target`, spacing, and line endings. Do not translate or rewrite list text, copy English list additions/deletions/reordering, replace localized URLs with English URLs, or correct apparent list typos without a separate user request.
- On every translation sync, read the current English introduction and each requested locale's introduction and compare their meaning independently of `translation_delta.py`. Update only outdated introductory text; leave an equivalent existing translation unchanged. Changes confined to the English model list require no localized update. If either list boundary is missing or ambiguous, or a localized page is absent, report the issue for that locale instead of regenerating a list or guessing the editable region; continue independent work for the other requested locales.
- Before writing, retain each target's list suffix as raw bytes. After editing, verify that it is identical and inspect the diff to ensure changes are confined to the heading and introductory prose. Review those changes for natural target-language wording and fidelity to English; the scripts' whole-page exclusion does not validate the translation.
- Do not run `translation_delta.py mark` for Downloads or add a Downloads cache record: it remains excluded by the scripts. Report each requested locale's introduction as updated, already equivalent, or unavailable for the stated reason, separately from cached files. Do not report list differences as translation backlog or change navigation/homepage links solely for this introduction sync.

## Language-Specific Rules

- Follow the relevant language reference in this skill when it applies to the target language.
- Keep language-specific terminology, style, and localization rules in language reference files instead of duplicating them here.
