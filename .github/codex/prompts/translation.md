You are running the repository's scheduled translation sync in a clean checkout of the latest `master` branch.

Use the `$glinet-docs-translation` skill and follow its Incremental Sync Workflow exactly. Read the repository `AGENTS.md`, the complete `.translation-cache.json` delta report at `.codex-run/translation-delta.json`, `.agents/skills/glinet-docs-translation/references/common.md`, and the target-language references before editing localized files.

## Preconditions

- Confirm the current branch is `master` and the working tree is clean. The workflow already checked out the latest `origin/master`; do not create a different branch and do not pull another branch.
- If the branch or working tree precondition fails, stop without editing and return `status: blocked`.
- Treat the cache delta report as the source set. Each `hash_mismatch` and `cache_missing` entry lists the languages that are out of date for that English file; sync exactly those languages and do not infer the set only from recent commits.
- For each out-of-date file and language, run `python scripts/translation_delta.py diff <en-file> --lang <lang>` to see what English changed since that language was synced. If it reports no stored English version, compare the whole English and localized pages.
- Skip the excluded Downloads page and trailing `## Regulatory Statements` sections as required by the skill.

## Translation

- First produce the English change list in your result, including added, modified, deleted, and renamed source files where applicable.
- Sync `de`, `es`, `fr`, `it`, `ja`, `pl`, and `uk`. Preserve Markdown structure, links, images, anchors, UI labels, technical values, warnings, and protected localized declarations.
- Translate only changed portions of existing pages. Read the full English and localized pages and nearby terminology before editing. Use at most two subagents for independent language or topic batches if useful.
- Run `python scripts/i18n_check.py --lang de es fr it ja pl uk` and fix every error in the files you synced.
- Record each sync with `python scripts/translation_delta.py mark <en-file> ... --lang <langs> --model codex`. Do not edit `.translation-cache.json` in any other way. If `mark` refuses a language, fix the reported problem; if it cannot be fixed safely, leave that language unmarked and report it.
- Use `--no-target-change` only for English changes that need no translation change, such as typo fixes, and only with the languages listed explicitly.
- Do not modify English source files in this run. If an English source has an obvious issue, report it with a path, location, problem, suggested correction, and whether it blocks translation.
- Do not commit or push. Leave the translated files and cache changes in the working tree for the workflow to validate and submit.

## Validation

Run `python scripts/i18n_check.py` and `python scripts/anchors.py check`; both must report no errors. Run strict MkDocs builds for all seven localized languages using their normal `mkdocs.yml` files. Remove generated `docs/<lang>/site` directories after the builds. Inspect the final diff for unrelated churn, mixed-language fragments, broken links or anchors, malformed Markdown, missing localized pages, and stale cache entries.

Return only JSON matching `.github/codex/translation-output.schema.json`. Set `status` to `completed` when the sync and builds finish, `no_changes` when no edits were needed, `blocked` when a precondition or a blocking source issue prevents a safe sync, and `failed` when an unexpected operation fails.
