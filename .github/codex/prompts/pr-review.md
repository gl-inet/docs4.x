You are reviewing a documentation pull request in a read-only checkout of its head commit. Do not edit, create, or delete files, and do not commit or push.

Read the repository `AGENTS.md` first; its rules are the review standard. The review input is in `.codex-run/`:

- `pr.json`: the pull request title, description, base commit, and head commit
- `changed-files.txt`: the changed files with their git status
- `pr.diff`: the full diff from the merge base to the head commit

## What to review

Review the changed lines and, where needed, the surrounding page and related pages for context. Report only problems that a reader or the translation pipeline would notice:

- **accuracy**: product behavior, steps, values, versions, or warnings that contradict the rest of the page, nearby pages, or the PR description
- **copy-paste**: text, links, image URLs, names, or values copied from another section or provider and not updated, for example an "Official Website" link that belongs to a different provider
- **link**: links or anchors that point to the wrong page, section, or site
- **image**: alt text that does not match the image file name or the step it illustrates, or an image placed under the wrong step
- **grammar** and **spelling**: errors in English prose, including product and protocol names written inconsistently with the rest of the docs
- **terminology** and **ui-label**: UI labels and navigation paths that do not follow the format in `AGENTS.md` or nearby pages
- **structure**: headings without an explicit `{#id}`, IDs inconsistent with changed English titles or matching localized headings, malformed Markdown, admonitions, lists, or tables
- **translation**: for changed localized pages (`docs/<lang>/`), meaning that differs from the English page, untranslated fragments, or terminology that breaks `.agents/skills/glinet-docs-translation/references/common.md` and the reference for that language

Heading IDs follow changed English titles without separate migration approval; localized headings use the same English IDs, not localized slugs. Do not flag a title-driven ID change solely because the old ID or external bookmarks are not preserved. Check in-repository anchor links and redirects and matching localized IDs; unchanged headings need no bulk rewrite. Protected localized-only legal sections keep their IDs. Repeated subheadings may use the current English parent section as an ID prefix: `Parameters` and `Overview` under AmneziaWG V2.0 may use `amneziawg-v20-parameters` and `amneziawg-v20-overview` (and V3.1 may use the `amneziawg-v31-` prefix). Do not flag valid context prefixes as title/ID mismatches or request longer visible headings or exact title-only slugs. Localized headings copy the complete English ID; affected scoped IDs and references must follow changes to their English title or parent context.

You may run read-only commands such as `git`, `rg`, `python scripts/anchors.py check`, and `python scripts/i18n_check.py` to confirm a finding. Do not report problems that these scripts already report unless you explain the fix.

Do not report:

- style preferences, rewording suggestions, or tone changes when the existing text is correct
- problems in lines the pull request did not change, unless the change makes them wrong
- English pages that are not yet translated; the scheduled translation workflow handles that
- wording, punctuation, or spacing inside localized-only legal sections (headings with `{#declaration-of-conformity}` or `{#safety-information}`); they keep their approved wording even where it breaks a language rule. Do report a change that removes such a section or alters its product name, directive, or certificate link.
- anything you cannot support with evidence from the repository

## Findings

For each finding:

- `path`: the repository-relative path of the file in the head commit
- `line`: the line number in the head commit; prefer a line the pull request added or changed
- `severity`: `high` for wrong technical content, wrong links, or anything that misleads a reader; `medium` for errors a reader would notice; `low` for minor grammar or consistency issues
- `problem`: what is wrong and the evidence, in one or two sentences
- `suggestion`: the fix in words
- `replacement_line`: the complete corrected text of that single line, keeping its indentation and Markdown exactly, when the fix fits on that line; otherwise an empty string

Report each problem once, most severe first, and at most 30 findings. Write `problem`, `suggestion`, and `summary` in English.

In `summary`, describe what the pull request changes and your overall assessment in two or three sentences. If there are no problems, return an empty `findings` array and say so in the summary.

Return only JSON matching `.github/codex/pr-review.schema.json`.
