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

## Incremental Sync Workflow

Use this workflow when syncing English changes into localized docs, especially when the user asks to translate changes after a commit.

0. Preflight before building the change set:
   - Run `python scripts/translation_delta.py` first when the script exists, and use its cache-delta report as the primary input for the source-change set.
   - Report the current branch and working tree status.
   - If the branch is not `master`, or the branch appears behind its upstream, report that before continuing.
   - Do not run `git pull` automatically unless the user explicitly requests it. If the user asks to update from `master`, pull only when the working tree is clean; otherwise stop and report the local changes first.
1. Establish the source-change set before translating:
   - Prefer `.translation-cache.json` to identify English source files whose current hash differs from the cached `source_hash`.
   - If the user gives a commit, diff `commit..HEAD` and use it as the explicit source-change set.
   - If no commit is given and cache is insufficient, use the most recent commit whose message is `translation, from en to others.` as the fallback lower bound, then diff that commit..HEAD.
2. Build an English change list first. Include modified, added, deleted, and renamed files under `docs/en/`, plus changes to `docs/en/mkdocs.yml`, redirects, nav, and path references.
3. Handle structure before prose:
   - Mirror English renames in `docs/de/`, `docs/es/`, `docs/fr/`, `docs/it/`, `docs/jp/`, and `docs/pl/`.
   - Create matching localized pages when English adds pages.
   - Sync localized `mkdocs.yml` changes when English changes nav, redirects, plugins, or path references.
4. Translate only the changed English portions. Do not retranslate whole pages unless the English page is new or the localized page is unusable and the user agrees.
5. Work by topic or small batches for large change sets, for example eSIM, VPN, antennas, or interface pages. Avoid one huge patch across unrelated topics.
6. Update `.translation-cache.json` for every English source file whose localized targets were synced. Set the current English source hash and refresh the touched target language metadata.
7. Before finishing, inspect diffs for unrelated translation churn, accidental mixed-language fragments, broken anchors, malformed Markdown, and missing matching localized files.

## Single-File Translation Workflow

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

## Commit Baseline Guidance

- Do not hard-code a specific commit hash in the skill. It becomes stale immediately after the next translation run.
- Prefer `.translation-cache.json` as the durable source of truth for incremental translation state because it records per-source hashes and per-language target state.
- Use the commit message `translation, from en to others.` only as a fallback discovery mechanism when the user does not provide a commit and the cache does not clearly identify what changed.
- If both cache and commit diff disagree, trust the explicit user-provided commit for the current task, but update the cache after the sync.

## Validation

Use the parent virtual environment for MkDocs in this repository. Do not install `requirements.txt` unless the virtual environment is missing or lacks required dependencies.

```powershell
# Run from repository root: docs4.x
$mkdocs="..\Scripts\mkdocs.exe"
$langs=@('de','es','fr','it','jp','pl')
foreach($lang in $langs){
  Write-Host "BUILD $lang"
  & $mkdocs build -f "docs/$lang/mkdocs.yml" --strict
  if($LASTEXITCODE -ne 0){ exit $LASTEXITCODE }
}
```

If `git-revision-date-localized` fails on Windows with multiprocessing `Access is denied`, rerun the same build outside the sandbox rather than changing docs content or plugin config.

After successful builds, delete generated `docs/<lang>/site` directories. Verify resolved paths stay inside the workspace before deletion. If deletion fails with `Access denied`, set generated file attributes to `Normal` and rerun cleanup with approval.

MkDocs may report existing pages not included in nav and plugin deprecation notices. Treat these as informational unless they are new errors or `--strict` fails.

## Final Check

Before finishing a translation task, verify:

- The target-language text reads naturally from start to finish.
- No unintended source-language artifacts remain in prose.
- UI labels, links, images, Markdown formatting, and admonitions are preserved correctly.
- Technical behavior and security notes still match the English source.
- Terminology is consistent within the file and with nearby localized docs.
- Build output succeeds and generated `site` directories have been removed.
