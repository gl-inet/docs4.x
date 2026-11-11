"""Regression tests for spelling only the added English prose, as in docs-kvm."""
import importlib.util
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pr_check as pc

PAGE = "docs/en/docs/page.md"


class SpellingTests(unittest.TestCase):
    def test_only_added_english_prose_with_original_line_numbers(self):
        lines = ["---", "title: teh", "---", "old teh", "```", "teh", "```", "new teh"]
        output = Mock(returncode=65, stdout="8: teh ==> the\n", stderr="")
        with patch.object(pc, "page_lines", return_value=lines), \
                patch.object(pc.subprocess, "run", return_value=output) as run:
            findings = pc.check_spelling({PAGE: {2, 6, 8}, "docs/de/docs/page.md": {1}})
        self.assertEqual([(f.path, f.level, f.line) for f in findings], [(PAGE, "error", 8)])
        self.assertEqual(run.call_count, 1)
        self.assertEqual(run.call_args.kwargs["input"], "\n" * 7 + "new teh")
        self.assertIn("--stdin-single-line", run.call_args.args[0])

    def test_fences_close_only_without_trailing_text(self):
        lines = ["    ````python", "teh", "    ```", "still code",
                 "    ```` trailing", "still code", "    ````", "prose"]
        self.assertEqual(list(pc.prose_lines(lines)), [(8, "prose")])

    def test_tool_failure_is_error(self):
        for failure in (OSError("missing"), Mock(returncode=1, stdout="", stderr="failed")):
            with self.subTest(failure=failure), patch.object(pc, "page_lines", return_value=["text"]), \
                    patch.object(pc.subprocess, "run") as run:
                if isinstance(failure, OSError):
                    run.side_effect = failure
                else:
                    run.return_value = failure
                self.assertEqual(pc.check_spelling({PAGE: {1}})[0].level, "error")

    @unittest.skipUnless(importlib.util.find_spec("codespell_lib"), "optional codespell dependency not installed")
    def test_real_codespell_ignores_literals_and_reports_prose(self):
        lines = ["---", "title: teh", "---", "old teh", "~~~", "teh", "~~~",
                 'Use `teh` and ``teh `literal` teh`` {#teh} <span title="teh">text</span>.',
                 "This is teh typo."]
        with patch.object(pc, "page_lines", return_value=lines):
            findings = pc.check_spelling({PAGE: {2, 6, 8, 9}})
        self.assertEqual([(f.level, f.line) for f in findings], [("error", 9)])
        self.assertIn('"teh"', findings[0].message)


if __name__ == "__main__":
    unittest.main()
