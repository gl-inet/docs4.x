You are running the repository's scheduled translation sync in a clean checkout of the latest `master` branch.

Use the `$glinet-docs-translation` skill and follow its Incremental Sync Workflow exactly. Read the repository `AGENTS.md`, the complete `.translation-cache.json` delta report at `.codex-run/translation-delta.json`, `.agents/skills/glinet-docs-translation/references/common.md`, and the target-language references before editing localized files.

## Preconditions

- Confirm the current branch is `master` and the working tree is clean. The workflow already checked out the latest `origin/master`; do not create a different branch and do not pull another branch.
- If the branch or working tree precondition fails, stop without editing and return `status: blocked`.
- Treat the cache delta report as the source set. Translate every changed or cache-missing English source reported there; do not infer the set only from recent commits.
- Skip the excluded Downloads page and trailing `## Regulatory Statements` sections as required by the skill.

## Translation

- First produce the English change list in your result, including added, modified, deleted, and renamed source files where applicable.
- Sync `de`, `es`, `fr`, `it`, `ja`, and `pl`. Preserve Markdown structure, links, images, anchors, UI labels, technical values, warnings, and protected localized declarations.
- Translate only changed portions of existing pages. Read the full English and localized pages and nearby terminology before editing. Use at most two subagents for independent language or topic batches if useful.
- Update `.translation-cache.json` for every source file whose localized targets were synced.
- Do not modify English source files in this run. If an English source has an obvious issue, report it with a path, location, problem, suggested correction, and whether it blocks translation.
- Do not commit or push. Leave the translated files and cache changes in the working tree for the workflow to validate and submit.

## Validation

Run strict MkDocs builds for all six localized languages using their normal `mkdocs.yml` files. Remove generated `docs/<lang>/site` directories after the builds. Inspect the final diff for unrelated churn, mixed-language fragments, broken links or anchors, malformed Markdown, missing localized pages, and stale cache entries.

Return only JSON matching `.github/codex/translation-output.schema.json`. Set `status` to `completed` when the sync and builds finish, `no_changes` when no edits were needed, `blocked` when a precondition or a blocking source issue prevents a safe sync, and `failed` when an unexpected operation fails.
