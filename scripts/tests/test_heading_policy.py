"""Offline checks for title-driven heading ID guidance and PR diagnostics."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pr_check

ROOT = Path(__file__).resolve().parents[2]


def normalized(path):
    return ' '.join((ROOT / path).read_text(encoding='utf-8').split())


class HeadingPolicyTests(unittest.TestCase):
    def test_shared_policy_and_translation_guidance(self):
        guidance = normalized('AGENTS.md')
        self.assertIn('Heading IDs follow the current English heading text.', guidance)
        self.assertIn('needs no separate migration approval', guidance)
        self.assertIn('all in-repository anchor links and redirects', guidance)
        self.assertIn('Do not derive shared IDs from localized titles', guidance)
        self.assertNotIn('Do not change an existing ID when heading wording changes', guidance)
        common = normalized('.agents/skills/glinet-docs-translation/references/common.md')
        prompt = normalized('.github/codex/prompts/translation.md')
        for text in (common, prompt):
            self.assertIn('no separate approval or migration list', text)
            self.assertIn('outside the initial cache delta', text)
            self.assertIn('Unresolved broken links', text)
        self.assertIn('never derive shared IDs from localized titles', prompt)
        self.assertIn('not reasons to stop before editing', prompt)
        self.assertIn('final errors still prevent completed status', prompt)
        self.assertIn('Do not modify English source files', prompt)
        self.assertIn('both must report no errors', prompt)
        review = normalized('.github/codex/prompts/pr-review.md')
        self.assertIn('Do not flag a title-driven ID change solely', review)
        self.assertIn('Protected localized-only legal sections keep their IDs.', review)
        self.assertNotIn('changed existing IDs', review)

    @patch('pr_check.page_lines', return_value=['## Appearance {#appearance}'])
    @patch('pr_check.git')
    def test_removed_id_warning_requests_repairs_not_old_id_retention(self, git, pages):
        git.side_effect = [
            'M\tdocs/en/docs/example.md\n',
            'base-sha\n',
            '## Dimension {#dimension}\n',
        ]
        findings = pr_check.check_heading_ids('origin/master')
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].level, 'warning')
        self.assertEqual(findings[0].check, 'heading-id')
        self.assertIn('dimension', findings[0].message)
        self.assertIn('IDs follow the current English title', findings[0].message)
        self.assertIn('in-repository anchor links and redirects', findings[0].message)
        self.assertNotIn('Keep existing IDs', findings[0].message)


if __name__ == '__main__':
    unittest.main()
