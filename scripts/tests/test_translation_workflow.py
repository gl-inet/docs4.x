"""Offline regression coverage for reporting blocked syncs without checkout."""
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]


class TranslationWorkflowTests(unittest.TestCase):
    def test_source_issue_report_selects_repository_without_checkout(self):
        workflow = yaml.load(
            (ROOT / '.github/workflows/translation.yml').read_text(encoding='utf-8'),
            Loader=yaml.BaseLoader,
        )
        publish = workflow['jobs']['publish']
        checkout = next(s for s in publish['steps'] if s.get('uses', '').startswith('actions/checkout@'))
        # Blocked/no-patch results skip checkout but must still report source issues.
        self.assertIn("needs.validate.result == 'success'", checkout['if'])
        issue = next(s for s in publish['steps'] if s.get('name') == 'Create issue for English source problems')
        self.assertIn("steps.pull_request.outputs.created != 'true'", issue['if'])
        self.assertEqual(issue['env']['GH_TOKEN'], '${{ github.token }}')
        self.assertIn('(.source_issues // []) | length > 0', issue['run'])
        self.assertIn('gh issue create --repo "$GITHUB_REPOSITORY"', issue['run'])
        self.assertIn('--body-file "$RUNNER_TEMP/english-source-issues.md"', issue['run'])
        # Reporting must not convert a blocked model result to success.
        final = next(s for s in publish['steps'] if s.get('name') == 'Fail when Codex did not complete the sync')
        self.assertIn('"$status" = "blocked"', final['run'])
        self.assertIn('exit 1', final['run'])


if __name__ == '__main__':
    unittest.main()
