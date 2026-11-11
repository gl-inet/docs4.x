"""Offline regression coverage for reporting blocked syncs without checkout."""
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]


class TranslationWorkflowTests(unittest.TestCase):
    def workflow(self):
        return yaml.load(
            (ROOT / '.github/workflows/translation.yml').read_text(encoding='utf-8'),
            Loader=yaml.BaseLoader,
        )

    def test_all_translation_stages_use_the_prepared_revision(self):
        jobs = self.workflow()['jobs']
        self.assertEqual(jobs['prepare']['outputs']['source_sha'], '${{ steps.source.outputs.sha }}')
        source = next(s for s in jobs['prepare']['steps'] if s.get('id') == 'source')
        self.assertIn('echo "sha=$(git rev-parse HEAD)" >> "$GITHUB_OUTPUT"', source['run'])
        self.assertLess(source['run'].index('test -z'), source['run'].index('echo "sha='))
        for name in ('translate', 'validate', 'publish'):
            with self.subTest(job=name):
                self.assertIn('prepare', jobs[name]['needs'])
                checkout = next(s for s in jobs[name]['steps']
                                if s.get('uses', '').startswith('actions/checkout@'))
                self.assertEqual(checkout['with']['ref'], '${{ needs.prepare.outputs.source_sha }}')
                self.assertEqual(checkout['with']['fetch-depth'], '0')
        steps = jobs['translate']['steps']
        restore = next(i for i, s in enumerate(steps) if s.get('run') == 'git switch -C master')
        codex = next(i for i, s in enumerate(steps) if s.get('uses', '').startswith('openai/codex-action@'))
        self.assertLess(restore, codex)
        self.assertNotIn('origin/master', steps[restore]['run'])

    def test_publish_checks_master_before_applying_or_writing(self):
        publish = self.workflow()['jobs']['publish']
        step = next(s for s in publish['steps'] if s.get('id') == 'pull_request')
        self.assertEqual(step['env']['SOURCE_SHA'], '${{ needs.prepare.outputs.source_sha }}')
        command = step['run']
        fetch = command.index('git fetch origin master')
        compare = command.index('test "$(git rev-parse origin/master)" = "$SOURCE_SHA"')
        stop = command.index('exit 1;', compare)
        self.assertLess(fetch, compare)
        self.assertLess(compare, stop)
        for operation in ('git apply --index', 'git switch -c', 'core.hooksPath=/dev/null commit', 'git push', 'gh pr create'):
            self.assertLess(stop, command.index(operation))
        self.assertIn('Run the workflow again.', command)
        self.assertNotIn('gh pr merge', command)

    def test_original_guard_runs_before_validation_or_publication(self):
        jobs = self.workflow()['jobs']
        copy = 'cp scripts/translation_guard.py "$RUNNER_TEMP/translation_guard.py"'
        apply = 'git apply --index "$RUNNER_TEMP/translation/codex.patch"'
        report = '--report "$RUNNER_TEMP/translation/codex-output.json"'
        for name in ('validate', 'publish'):
            with self.subTest(job=name):
                steps = jobs[name]['steps']
                guard = next(s for s in steps if copy in s.get('run', ''))
                command = guard['run']
                self.assertLess(command.index(copy), command.index(apply))
                self.assertLess(command.index(apply), command.index(report))
                self.assertIn('-I "$RUNNER_TEMP/translation_guard.py"', command)
                downloads = {s['with']['name']: s['with']['path'] for s in steps
                             if s.get('uses', '').startswith('actions/download-artifact@')}
                for artifact in ('codex-patch', 'codex-report'):
                    self.assertEqual(downloads[artifact], '${{ runner.temp }}/translation')
                if name == 'validate':
                    install = next(s for s in steps if 'pip install' in s.get('run', ''))
                    self.assertLess(steps.index(guard), steps.index(install))
                else:
                    for operation in ('git switch -c', 'core.hooksPath=/dev/null commit',
                                      'git push', 'gh pr create'):
                        self.assertLess(command.index(report), command.index(operation))
                    self.assertNotIn('git commit -m', command)

    def test_publish_report_consumers_use_temporary_artifacts(self):
        steps = self.workflow()['jobs']['publish']['steps']
        for name in ('Create translation PR', 'Create issue for English source problems',
                     'Fail when Codex did not complete the sync'):
            command = next(s['run'] for s in steps if s.get('name') == name)
            for line in command.splitlines():
                if 'codex-output.json' in line:
                    self.assertIn('"$RUNNER_TEMP/translation/codex-output.json"', line)

    def test_schedule_languages_and_reporting_are_preserved(self):
        workflow = self.workflow()
        self.assertEqual(workflow['on']['schedule'],
                         [{'cron': '23 7 * * 1-5', 'timezone': 'Asia/Shanghai'}])
        self.assertIn('workflow_dispatch', workflow['on'])
        jobs = workflow['jobs']
        validate = '\n'.join(s.get('run', '') for s in jobs['validate']['steps'])
        self.assertIn('for lang in de es fr it ja nl pl sv uk;', validate)
        for check in ('--strict', 'i18n_check.py --base HEAD', 'anchors.py check', '--fail-on-delta --json'):
            self.assertIn(check, validate)
        reporter_checkout = jobs['report']['steps'][0]
        self.assertEqual(reporter_checkout['with']['ref'], '${{ github.sha }}')
        self.assertEqual(jobs['report']['needs'], ['prepare', 'translate', 'validate', 'publish'])
        self.assertEqual(jobs['translate']['outputs']['has_changes'], '${{ steps.diff.outputs.has_changes }}')

    def test_prompt_keeps_translation_on_the_prepared_revision(self):
        prompt = (ROOT / '.github/codex/prompts/translation.md').read_text(encoding='utf-8')
        self.assertIn('prepared source SHA', prompt)
        self.assertIn('do not fetch, pull, switch to another revision', prompt)
        self.assertNotIn('latest `origin/master`', prompt)

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
