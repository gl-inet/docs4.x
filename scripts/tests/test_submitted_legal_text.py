"""Submitted legal wording is protected across partial staging and file moves."""
from contextlib import redirect_stdout
import io
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import i18n_check as checker
import precommit
import test_pr_structure_snapshot as fixtures

LEGAL = "docs/de/docs/safety.md"
APPROVED = "# Sicherheit {#safety-information}\n\nApproved wording.\n"


class ProtectedTextTests(unittest.TestCase):
    def test_standalone_delete_edit_and_id_removal(self):
        for after in (None, "", APPROVED.replace("Approved", "Changed"),
                      APPROVED.replace("{#safety-information}", ""),
                      APPROVED.replace("{#safety-information}", "{#other}")):
            with self.subTest(after=after):
                issues = checker.check_protected_text("de", "safety.md", APPROVED, after)
                self.assertTrue(issues)
                self.assertEqual(issues[0].check, "protected-section")

    def test_unchanged_and_new_legal_text(self):
        self.assertEqual(checker.check_protected_text("de", "safety.md", APPROVED, APPROVED), [])
        self.assertEqual(checker.check_protected_text("de", "safety.md", None, APPROVED), [])
        self.assertEqual(checker.check_protected_text("en", "safety.md", APPROVED, None), [])

    def test_embedded_sections_but_not_unrelated_prose_are_protected(self):
        before = "# Page {#page}\n\nIntroduction.\n\n" + APPROVED.replace("# Sicherheit", "## Sicherheit")
        self.assertTrue(checker.check_protected_text("de", "page.md", before,
                                                   before.replace("Approved", "Changed")))
        self.assertEqual(checker.check_protected_text("de", "page.md", before,
                                                     before.replace("Introduction", "Updated")), [])


class SubmittedLegalTests(unittest.TestCase):
    # Reuse the isolated Git fixture, without inheriting unrelated test cases.
    setUp = fixtures.StructureSnapshotTests.setUp
    git = fixtures.StructureSnapshotTests.git
    put = fixtures.StructureSnapshotTests.put
    commit = fixtures.StructureSnapshotTests.commit
    record = fixtures.StructureSnapshotTests.record
    run_check = fixtures.StructureSnapshotTests.run_check

    def approve(self):
        self.put(LEGAL, APPROVED)
        self.commit("approved standalone legal page")
        self.base = self.git("rev-parse", "HEAD").strip()

    def local_check(self):
        output = io.StringIO()
        with redirect_stdout(output):
            code = precommit.main([])
        return code, output.getvalue()

    def test_staged_edit_cannot_be_hidden_by_unstaged_restoration(self):
        self.approve()
        self.put(LEGAL, APPROVED.replace("Approved", "Changed"))
        self.git("add", LEGAL)
        self.put(LEGAL, APPROVED)
        code, output = self.local_check()
        self.assertEqual(code, 1, output)
        self.assertIn("protected-section", output)

    def test_unstaged_legal_edit_does_not_block_valid_staged_text(self):
        path = fixtures.TARGET
        before = Path(path).read_text(encoding="utf-8") + "\n" + APPROVED.replace("# Sicherheit", "## Sicherheit")
        self.put(path, before)
        self.record()
        self.commit("approved embedded legal text")
        self.put(path, before.replace("Text.", "Anderer Text."))
        self.record()
        self.git("add", path, ".translation-cache.json")
        self.put(path, before.replace("Approved", "Unstaged change"))
        # Isolate legal protection from the existing worktree-based prose checks.
        self.assertEqual(precommit.protected_errors(), [])

    def test_deleted_page_is_blocked_without_english_counterpart(self):
        self.approve()
        self.git("rm", LEGAL)
        code, output = self.local_check()
        self.assertEqual(code, 1, output)
        self.assertIn("protected-section", output)
        self.commit("delete legal page")
        self.put(LEGAL, APPROVED)
        code, output = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertIn("protected-section", output)

    def test_rename_preserves_baseline_but_does_not_hide_edits(self):
        self.approve()
        new = "docs/de/docs/Sicherheitsübersicht.md"
        self.git("mv", LEGAL, new)
        self.assertEqual(precommit.protected_errors(), [])
        self.put(new, APPROVED.replace("Approved", "Changed"))
        self.git("add", new)
        self.assertTrue(precommit.protected_errors())

    def test_move_out_of_localized_markdown_is_removal(self):
        self.approve()
        self.git("mv", LEGAL, "approved.txt")
        self.assertTrue(precommit.protected_errors())


if __name__ == "__main__":
    unittest.main()
