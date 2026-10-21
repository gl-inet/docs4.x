---
name: glinet-docs-translation
description: Translate, sync, or review GL.iNet router documentation between English source files and localized docs. Use when asked to translate English docs into German, Spanish, French, Italian, Japanese, Polish, or Ukrainian; update localized docs after changes under docs/en/**; improve machine-translated localized pages; or check localized terminology, UI labels, Markdown structure, links, and technical accuracy.
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
- Ukrainian: `references/ukrainian.md`

If a task touches multiple languages, read `references/common.md` once and then read each relevant language reference.

## Incremental Sync Workflow

Use this workflow when syncing English changes into localized docs, especially when the user asks to translate changes after a commit.

0. Preflight before building the change set:
   - Run `python scripts/translation_delta.py` first and use its cache-delta report as the primary input for the source-change set. The report lists, per English file, the languages that are out of date; sync only those languages.
   - Report the current branch and working tree status.
   - If the branch is not `master`, or the branch appears behind its upstream, report that before continuing.
   - Do not run `git pull` automatically unless the user explicitly requests it. If the user asks to update from `master`, pull only when the working tree is clean; otherwise stop and report the local changes first.
1. Establish the source-change set before translating:
   - Prefer `.translation-cache.json`: each language records the English version it was last synced with. Run `python scripts/translation_delta.py diff <en-file> --lang <lang>` to see exactly what English changed since that language was synced.
   - If the user gives a commit, diff `commit..HEAD` and use it as the explicit source-change set.
   - If no commit is given and cache is insufficient, use the most recent commit whose message is `translation, from en to others.` as the fallback lower bound, then diff that commit..HEAD.
2. Build an English change list first. Include modified, added, deleted, and renamed files under `docs/en/`, plus changes to `docs/en/mkdocs.yml`, redirects, nav, and path references.
3. Handle structure before prose:
   - Mirror English renames in `docs/de/`, `docs/es/`, `docs/fr/`, `docs/it/`, `docs/ja/`, `docs/pl/`, and `docs/uk/`.
   - When English renames or deletes a page, delete the old localized files in every language and copy the English `redirect_maps` change into every localized `mkdocs.yml`. `scripts/i18n_check.py` reports localized pages without an English page and redirect maps that differ from English.
   - Create matching localized pages when English adds pages.
   - Sync localized `mkdocs.yml` changes when English changes nav, redirects, plugins, or path references.
4. Translate only the changed English portions. Do not retranslate whole pages unless the English page is new or the localized page is unusable and the user agrees.
5. Work by topic or small batches for large change sets, for example eSIM, VPN, antennas, or interface pages. Avoid one huge patch across unrelated topics.
6. Run `python scripts/i18n_check.py` and fix every error in the synced languages. It compares each localized page with the English page section by section (images, admonitions, code blocks, tables, links, IP addresses, and version numbers) and checks orphan pages and redirects. Add an entry to `scripts/i18n_allowlist.yml` only for an intentional difference, with a reason.
7. Record the sync with `python scripts/translation_delta.py mark <en-file> ... --lang <langs> --model <name>`, listing only the languages you synced (`--lang all` for all seven). `mark` refuses a language when `i18n_check.py` reports errors for that page, or when English changed but the localized file did not.
   - Never edit `.translation-cache.json` by hand or with a custom script, and never refresh hashes for files whose translations you did not update.
   - Use `--no-target-change` only when the English change needs no translation change (typo, grammar, or wording fixes with the same meaning), after reading the English diff and the localized text. Name each language explicitly; `--lang all` is rejected with this flag.
8. Before finishing, inspect diffs for unrelated translation churn, accidental mixed-language fragments, malformed Markdown, and missing matching localized files, and run `python scripts/anchors.py check` for heading IDs and anchor links.
9. If you notice an obvious issue in the English source while syncing, such as a typo, duplicated word, self-contradictory sentence, clearly broken link, or visible copy/paste error, do not silently ignore it. Fix it only when the user requested source fixes or the correction is clearly in scope; otherwise mention it in the final summary with the file path and suggested correction.

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
- Localized docs live under the language roots `docs/de/`, `docs/es/`, `docs/fr/`, `docs/it/`, `docs/ja/`, `docs/pl/`, and `docs/uk/`.
- For page content, prefer updating the matching localized path under the target language's `docs/` subdirectory. Create a new localized page only when the English source introduces a page that does not yet exist.
- For language-level files such as `mkdocs.yml` or homepage overrides, update the matching file under the target language root when it exists.

## Excluded Pages

- Skip `docs/en/docs/downloads/index.md` (the English Downloads / user manual page, `https://docs.gl-inet.com/router/en/4/downloads/`) when building the source-change set or syncing localized docs. Localized docs do not need this page for now.
- Do not create, update, or flag the matching localized `downloads/index.md` files for this page during sync workflows, even if the English version changes.
- Do not report this page's localized copies as out of sync or missing in the final summary while this exclusion is in effect.
- This exclusion is temporary; remove it once the user asks to resume translating this page.

## Excluded Sections

- Skip English trailing `## Regulatory Statements` sections when building the source-change set or syncing localized docs. These regulatory statements are intended to appear only in `docs/en/` pages and do not need localized copies.
- Do not create, update, or flag matching localized content for `## Regulatory Statements`, even when an English commit adds or changes these sections in user guide pages.
- Do not translate, rewrite, or localize the regulatory statement text. It may already contain required English and French legal wording that should remain confined to the English documentation.

## Protected Localized Sections

- Some localized user guides under `docs/de/`, `docs/es/`, `docs/fr/`, `docs/it/`, and `docs/pl/` contain a localized EU Declaration of Conformity even when the matching English page has no equivalent section.
- Preserve any existing Declaration of Conformity section, its product-specific wording, Directive `2014/53/EU` reference, and certificate link during translation syncs, page rewrites, and structure alignment. Do not delete it, replace it with English content, or flag it as extra or stale solely because it is absent from `docs/en/`.
- Treat these localized declarations as distinct from the English-only `## Regulatory Statements` exclusion above. When creating or replacing a localized user guide, inspect the previous localized page and retain its declaration if present.

## Commit Baseline Guidance

- Do not hard-code a specific commit hash in the skill. It becomes stale immediately after the next translation run.
- Prefer `.translation-cache.json` as the durable source of truth for incremental translation state because it records, per language, the English version each translation was synced with.
- Use the commit message `translation, from en to others.` only as a fallback discovery mechanism when the user does not provide a commit and the cache does not clearly identify what changed.
- If both cache and commit diff disagree, trust the explicit user-provided commit for the current task, but record the sync with `translation_delta.py mark` afterwards.

## Validation

Use the parent virtual environment for MkDocs in this repository. Do not install `requirements.txt` unless the virtual environment is missing or lacks required dependencies.

Full seven-language strict builds can take more than 120 seconds on Windows. When running the complete validation loop, use a command timeout of at least 600 seconds.

`mkdocs.fast.yml` is for local preview or quick smoke checks only because it disables plugins. Do not use it as a substitute for final validation.

For small edits, optionally run touched-language builds or fast smoke checks during iteration. Before finishing a translation sync, all seven localized docs must pass `docs/<lang>/mkdocs.yml --strict`.

```powershell
# Run from repository root: docs4.x
$mkdocs="..\Scripts\mkdocs.exe"
$langs=@('de','es','fr','it','ja','pl','uk')
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
- `python scripts/i18n_check.py` and `python scripts/anchors.py check` report no errors, and `python scripts/translation_delta.py` shows no delta for the synced files and languages.
- Build output succeeds and generated `site` directories have been removed.
- Any obvious English-source issues noticed during the sync were either fixed within scope or reported in the final summary with a concrete file path and suggested correction.
