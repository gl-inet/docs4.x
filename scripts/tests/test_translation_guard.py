"""Offline tests for the trusted router translation patch boundary."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import translation_guard as guard


class TranslationGuardTests(unittest.TestCase):
    def test_scope(self):
        for path in ('docs/de/docs/new.md', 'docs/ja/mkdocs.yml', 'docs/uk/mkdocs.yml',
                     '.translation-cache.json', 'docs/de/docs/regulatory_statement.md',
                     'docs/fr/docs/fcc_ic_compliance_statements.md'):
            self.assertTrue(guard.allowed_path(path), path)
        for path in ('docs/en/docs/new.md', 'scripts/anchors.py', '../docs/de/a.md',
                     '/docs/de/a.md', 'docs/de/../../scripts/a.py',
                     'docs/de/site/index.html', 'docs/de/a\nb.md',
                     'docs\\de\\docs\\a.md', '.github/workflows/translate.yml',
                     'requirements.txt', 'scripts/i18n_allowlist.yml'):
            self.assertFalse(guard.allowed_path(path), path)
        for lang in guard.LANGS:
            self.assertFalse(guard.allowed_path(f'docs/{lang}/docs/downloads/index.md'))

    def test_protected_sections(self):
        text = '# Page {#page}\n\n## Safety {#safety-information}\nApproved.\n\n## Setup {#setup}\nNormal.\n'
        self.assertEqual(guard.protected_sections(text), ['## Safety {#safety-information}\nApproved.\n\n'])
        self.assertEqual(guard.protected_sections('## Setup {#setup}\nText.\n'), [])

    def test_protected_wording_and_deletion(self):
        for section_id in guard.PROTECTED_IDS:
            legal = f'## Legal {{#{section_id}}}\nApproved.\n\n'
            before = '# Page {#page}\n\n' + legal
            guard.check_content('docs/de/docs/page.md', before, before)
            for after in (before.replace('Approved.', 'Altered.'), '# Page {#page}\n\n'):
                with self.subTest(section_id=section_id, after=after):
                    with self.assertRaisesRegex(ValueError, 'approved legal'):
                        guard.check_content('docs/de/docs/page.md', before, after)

    def test_protected_section_may_not_move(self):
        legal = '## Safety {#safety-information}\nApproved.\n\n'
        setup = '## Setup {#setup}\nInstructions.\n\n'
        before = '# Page {#page}\n\n' + legal + setup
        after = '# Page {#page}\n\n' + setup + legal
        self.assertEqual(guard.protected_sections(before), guard.protected_sections(after))
        with self.assertRaisesRegex(ValueError, 'placement'):
            guard.check_content('docs/de/docs/page.md', before, after)

    def test_title_driven_neighbor_ids_may_change(self):
        legal = '## Safety {#safety-information}\nApproved.\n\n'
        before = '# Old title {#old-title}\n\n' + legal + '## Setup {#setup}\nInstructions.\n'
        for after in (before.replace('Old title {#old-title}', 'New title {#new-title}'),
                      before.replace('Old title {#old-title}', 'New title {#new-title}')
                            .replace('Setup {#setup}', 'Installation {#installation}')):
            with self.subTest(after=after):
                guard.check_content('docs/de/docs/page.md', before, after)

    def test_reordered_stable_neighbors_are_not_hidden_by_same_ordinal(self):
        legal = '## Safety {#safety-information}\nApproved.\n\n'
        a = '## A {#a}\nA.\n\n'
        b = '## B {#b}\nB.\n\n'
        before = '# Page {#page}\n\n' + a + legal + b
        after = '# Page {#page}\n\n' + b + legal + a
        with self.assertRaisesRegex(ValueError, 'placement'):
            guard.check_content('docs/de/docs/page.md', before, after)

    def test_neighbor_rename_does_not_hide_crossing_another_heading(self):
        legal = '## Safety {#safety-information}\nApproved.\n\n'
        before = '# Page {#page}\n\n' + legal + '## Setup {#setup}\nInstructions.\n'
        after = '# New page {#new-page}\n\n## Setup {#setup}\nInstructions.\n\n' + legal
        with self.assertRaisesRegex(ValueError, 'placement'):
            guard.check_content('docs/de/docs/page.md', before, after)
        inserted = before.replace(legal, '## Extra {#extra}\nText.\n\n' + legal)
        with self.assertRaisesRegex(ValueError, 'placement'):
            guard.check_content('docs/de/docs/page.md', before, inserted)

    def test_report(self):
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / 'report.json'
            for status, passed, accepted in (('completed', True, True), ('blocked', True, False),
                                              ('completed', False, False), ('no_changes', True, False),
                                              ('completed', 'true', False), ('completed', None, False)):
                with self.subTest(status=status, passed=passed):
                    report.write_text(json.dumps({'status': status, 'validation': {'passed': passed}}))
                    if accepted:
                        guard.validate_report(report)
                    else:
                        with self.assertRaises(ValueError):
                            guard.validate_report(report)
            for blocking in (False, True):
                report.write_text(json.dumps({'status': 'completed', 'validation': {'passed': True},
                                              'source_issues': [{'blocking': blocking}]}))
                if blocking:
                    with self.assertRaisesRegex(ValueError, 'blocking source issue'):
                        guard.validate_report(report)
                else:
                    guard.validate_report(report)
            report.write_text('{}')
            with self.assertRaises(ValueError):
                guard.validate_report(report)
            report.write_text(json.dumps({'status': 'completed'}))
            with self.assertRaises(ValueError):
                guard.validate_report(report)

    def test_staged_patch_and_legal_protection(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def git(*args):
                return subprocess.check_output(['git', *args], cwd=root, stderr=subprocess.DEVNULL)
            git('init')
            git('config', 'user.email', 'test@example.com')
            git('config', 'user.name', 'Test')
            page = root / 'docs/de/docs/test.md'
            page.parent.mkdir(parents=True)
            original = '# Page {#page}\nText.\n\n## Safety {#safety-information}\nApproved.\n'
            page.write_text(original, encoding='utf-8')
            git('add', '.')
            git('commit', '-m', 'initial')
            previous = Path.cwd()
            try:
                os.chdir(root)
                with self.assertRaisesRegex(ValueError, 'empty'):
                    guard.check_patch()
                page.write_text(original.replace('Text.', 'Updated.'), encoding='utf-8')
                git('add', '.')
                self.assertEqual(guard.check_patch(), ['docs/de/docs/test.md'])
                for content in (original.replace('Approved.', 'Altered.'), '# Page {#page}\nText.\n'):
                    page.write_text(content, encoding='utf-8')
                    git('add', '.')
                    with self.assertRaisesRegex(ValueError, 'approved legal'):
                        guard.check_patch()
                page.unlink()
                git('add', '.')
                with self.assertRaisesRegex(ValueError, 'approved legal'):
                    guard.check_patch()
                git('reset', '--hard', 'HEAD')
                for relative in ('docs/en/docs/new.md', 'scripts/evil.py',
                                 '.github/workflows/translate.yml', 'requirements.txt',
                                 'scripts/i18n_allowlist.yml', 'docs/uk/docs/downloads/index.md',
                                 'docs/uk/docs/new.md', '.translation-cache.json'):
                    with self.subTest(path=relative):
                        target = root / relative
                        target.parent.mkdir(parents=True, exist_ok=True)
                        target.write_text('new content\n', encoding='utf-8')
                        git('add', '--', relative)
                        if relative in ('docs/uk/docs/new.md', '.translation-cache.json'):
                            self.assertEqual(guard.check_patch(), [relative])
                        else:
                            with self.assertRaisesRegex(ValueError, 'forbidden path'):
                                guard.check_patch()
                        git('reset', '--hard', 'HEAD')
            finally:
                os.chdir(previous)

    def test_non_regular_modes_are_rejected(self):
        for mode in ('120000', '100755', '160000'):
            responses = [b'docs/de/docs/a.md\0', f'{mode} abc 0\tdocs/de/docs/a.md\n'.encode()]
            with self.subTest(mode=mode), patch.object(guard, 'git', side_effect=responses):
                with self.assertRaisesRegex(ValueError, 'non-regular'):
                    guard.check_patch()

    def test_trusted_cli_rejects_attempted_script_modification(self):
        with tempfile.TemporaryDirectory() as directory:
            outside = Path(directory)
            root = outside / 'repo'
            root.mkdir()
            trusted = outside / 'trusted_translation_guard.py'
            trusted.write_text(Path(guard.__file__).read_text(encoding='utf-8'), encoding='utf-8')
            report = outside / 'report.json'
            report.write_text(json.dumps({'status': 'completed', 'validation': {'passed': True}}))
            def git(*args):
                return subprocess.check_output(['git', *args], cwd=root, stderr=subprocess.DEVNULL)
            git('init')
            git('config', 'user.email', 'test@example.com')
            git('config', 'user.name', 'Test')
            script = root / 'scripts/translation_guard.py'
            script.parent.mkdir()
            script.write_text(trusted.read_text(encoding='utf-8'), encoding='utf-8')
            git('add', '.')
            git('commit', '-m', 'initial')
            script.write_text('raise SystemExit(0)\n', encoding='utf-8')
            git('add', '.')
            result = subprocess.run([sys.executable, str(trusted), '--report', str(report)],
                                    cwd=root, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn('forbidden path: scripts/translation_guard.py', result.stdout)


if __name__ == '__main__':
    unittest.main()
