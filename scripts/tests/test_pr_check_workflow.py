"""Offline regression tests for PR-check coverage and language selection."""
from pathlib import Path
import os
import subprocess
import unittest
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[2]


class WorkflowCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        text = (ROOT / ".github/workflows/pr-check.yml").read_text(encoding="utf-8")
        # Preserve the GitHub Actions `on` key rather than parsing it as boolean.
        cls.workflow = yaml.load(text, Loader=yaml.BaseLoader)

    def test_trigger_paths_match_kvm(self):
        trigger = self.workflow["on"]["pull_request"]
        self.assertEqual(trigger["branches"], ["master"])
        self.assertEqual(set(trigger["paths"]), {
            "docs/**", "scripts/**", ".translation-cache.json", "requirements*.txt",
            ".githooks/**", "**/AGENTS.md", "CLAUDE.md", ".agents/**", ".claude/**",
            ".github/workflows/pr-check.yml",
        })

    def test_existing_regression_suite_runs_before_structure_check(self):
        steps = self.workflow["jobs"]["structure"]["steps"]
        tests = next(i for i, step in enumerate(steps)
                     if step.get("run") == "python -m unittest discover -s scripts/tests")
        install = next(i for i, step in enumerate(steps)
                       if step.get("run") == "python -m pip install -r requirements.txt")
        structure = next(i for i, step in enumerate(steps)
                         if step.get("run", "").startswith("python scripts/precommit.py --base"))
        self.assertLess(install, tests)
        self.assertLess(tests, structure)
        self.assertNotIn("continue-on-error", steps[tests])

    def build_code(self):
        run = next(step["run"] for step in self.workflow["jobs"]["build"]["steps"]
                   if step.get("name") == "Build changed languages strictly")
        return run.split("python - <<'PY'\n", 1)[1].rsplit("\nPY", 1)[0]

    def test_changed_languages_and_english_fallback(self):
        cases = [
            ("docs/de/docs/page.md\0docs/fr/docs/中 文.md\0docs/de/mkdocs.yml\0", ["de", "fr"]),
            ("", ["en"]),
            ("docs/README.md\0", ["en"]),
            ("docs/unknown/docs/page.md\0", ["en"]),
            ("docs/README.md\0docs/uk/docs/page.md\0", ["uk"]),
        ]
        for changed, expected in cases:
            with self.subTest(changed=changed), \
                    patch("subprocess.check_output", return_value=changed.encode("utf-8")) as diff, \
                    patch("subprocess.run") as build, \
                    patch.object(Path, "is_file", autospec=True,
                                 side_effect=lambda p: p.parts[-2] in ("en", "de", "fr", "uk")), \
                    patch.dict(os.environ, {"RUNNER_TEMP": "temporary"}):
                exec(compile(self.build_code(), "workflow-build", "exec"), {})
                self.assertEqual(diff.call_args.args[0], [
                    "git", "diff", "--name-only", "-z", "origin/master...HEAD", "--", "docs/",
                ])
                commands = [call.args[0] for call in build.call_args_list]
                self.assertEqual([command[3] for command in commands],
                                 [f"docs/{lang}/mkdocs.yml" for lang in expected])
                for lang, call in zip(expected, build.call_args_list):
                    self.assertIn("--strict", call.args[0])
                    self.assertEqual(call.args[0][-2:],
                                     ["--site-dir", str(Path("temporary") / f"site-{lang}")])
                    self.assertTrue(call.kwargs["check"])

    def test_failed_build_is_not_ignored(self):
        with patch("subprocess.check_output", return_value=b""), \
                patch("subprocess.run", side_effect=subprocess.CalledProcessError(1, "mkdocs")), \
                patch.dict(os.environ, {"RUNNER_TEMP": "temporary"}):
            with self.assertRaises(subprocess.CalledProcessError):
                exec(compile(self.build_code(), "workflow-build", "exec"), {})


if __name__ == "__main__":
    unittest.main()
