# Automated translation sync

The `translation.yml` workflow runs the repository translation sync daily at
08:23 in `Asia/Shanghai` and can also be started with `workflow_dispatch`.

Configure these repository secrets before enabling the schedule:

- `OPENAI_API_KEY`: the API key used by Codex.
- `CODEX_RESPONSES_API_ENDPOINT`: the full Responses API endpoint, including
  `/v1/responses` when required by the provider.

The workflow checks the cache delta, gives the repository and the translation
skill to Codex, captures a patch and structured report, and then validates all
six localized MkDocs sites in a separate job. When changes exist and validation
passes, it opens a PR with the commit message `translation, from en to other`.
English source issues are included in the PR report; when no PR can be opened,
the workflow creates a GitHub issue with the same report.
