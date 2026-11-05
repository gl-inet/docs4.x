# Automated translation sync

The `translation.yml` workflow runs the repository translation sync Monday through
Friday at 07:23 in `Asia/Shanghai` and can also be started with `workflow_dispatch`.

Configure these repository secrets before enabling the schedule:

- `OPENAI_API_KEY`: the API key used by Codex.
- `CODEX_RESPONSES_API_ENDPOINT`: the full Responses API endpoint, including
  `/v1/responses` when required by the provider.

The workflow checks the cache delta, gives the repository and the translation
skill to Codex, captures a patch and structured report, and then validates all
nine localized MkDocs sites in a separate job. When changes exist and validation
passes, it opens a PR with the commit message `translation, from en to other`.
English source issues are included in the PR report; when no PR can be opened,
the workflow creates a GitHub issue with the same report.

The final read-only `report` job generates `translation-run.json` and uploads
it as `ai-agent-stats-translation-attempt-<run_attempt>`, retained for 30 days.
The production stats server pulls and validates this data artifact; this
workflow makes no request to the stats service and needs neither
`AI_AGENT_STATS_URL` nor `AI_AGENT_STATS_TOKEN`. Remove the obsolete stats
secret after the first production import is verified. No self-hosted runner
is needed.

The JSON contains only product (`router` / `4`), repository, run ID/attempt/link,
trigger and a coarse result: `no_delta`, `success`, `no_changes`,
`validation_failed`, `failed` or `cancelled`. Here `success` means changes
were captured and validation and publishing succeeded, not that the PR was
merged. Other failures, including Codex returning `blocked`, are grouped as
`failed`. Existing translation artifacts are not parsed; page text, tokens,
timing and per-language counts are not collected.

Artifact generation/upload failures do not fail the translation workflow,
but are visible in the report job. Cancellation reporting is best-effort:
GitHub may stop the report job before it can upload. Re-running only failed
jobs can reuse successful jobs from an earlier attempt; these are
workflow-attempt results, not a count of fresh Codex calls. The production
collector polls every 12 hours by default and can only import retained
artifacts; runs predating this change are not automatically backfilled.

Reporter tests: `python3 -m unittest discover -s scripts/tests -p 'test_report_translation_stats.py'`.

# Pull request review

The `pr-review.yml` workflow runs Codex on pull requests to `master` that
change `docs/**`. It runs when a PR is opened, reopened, or marked ready for
review, and again on every push to the PR branch; a new push cancels a running
review. Draft PRs and PRs from forks are skipped, because fork PRs get no
secrets. It uses the same `OpenAI` environment secrets as the translation sync,
so that environment must allow all branches.

`scripts/codex_review.py prepare` writes the diff and PR metadata to
`.codex-run/`. Codex reviews them with `prompts/pr-review.md` in a read-only
sandbox and returns JSON matching `pr-review.schema.json`. A separate job with
`pull-requests: write` runs `scripts/codex_review.py publish`: findings on added
lines become inline comments (with a one-click suggestion when Codex gives a
replacement line), other findings go into one summary comment that is updated on
each run, and inline comments from earlier runs are hidden as outdated.

The review is report-only and does not block merging.
