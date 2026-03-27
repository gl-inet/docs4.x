# Copilot Instructions for Documentation Translation

This repository contains localized GL.iNet router documentation. When translating documentation from English into another language, follow the rules below.

## Scope

- These instructions apply to translation work across localized docs in this repository.
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

- Check internal links carefully after translation.
- Preserve explicit custom heading anchors and hash IDs exactly as written, such as `{#example-anchor}` or `{custom-anchor}`.
- When translating a heading that has a custom anchor, keep the custom hash ID unchanged so cross-language links remain stable.
- If heading text changes, make sure same-page links still resolve.
- Update anchor links when needed instead of leaving broken English anchor references in a localized page.
- Keep cross-page links valid within the localized docs tree.

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

## Language-Specific Rules

- Follow any file-specific instructions under `.github/instructions/` when they apply to the target language or target folder.
- Keep language-specific terminology, style, and localization rules out of this file. Put them in scoped instruction files instead.

## Final Quality Check

Before considering the translation finished, verify all of the following:

- The target-language text reads naturally from start to finish.
- No unintended source-language artifacts remain in prose.
- UI labels, links, images, and formatting are preserved correctly.
- Security notes and behavioral descriptions still match the English source.
- Terminology is consistent within the file and with nearby localized docs.
