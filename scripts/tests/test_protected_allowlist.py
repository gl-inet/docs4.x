"""Approved legal text must not be exempted by translation allowlists."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import i18n_check as checker

REL = "example.md"
BEFORE = (
    "# Seite {#page}\n\nText.\n\n"
    "## Sicherheit {#safety-information}\n\nApproved wording.\n"
)


class ProtectedAllowlistTests(unittest.TestCase):
    def entry(self, check="protected-section", section=None):
        return checker.AllowEntry({"de"}, REL, check, section, "Test exception")

    def test_protected_errors_cannot_be_allowlisted(self):
        for section in (None, "safety-information", "declaration-of-conformity"):
            issue = checker.Issue("de", REL, "protected-section", "legal text changed",
                                  section or "safety-information", 5)
            entry = self.entry(section=section)
            with self.subTest(section=section):
                errors, allowed = checker.split_allowed([issue], [entry])
                self.assertEqual(errors, [issue])
                self.assertEqual(allowed, [])
                self.assertFalse(entry.used)

    def test_normal_translation_exceptions_are_unchanged(self):
        issue = checker.Issue("de", REL, "images", "intentional difference")
        entry = self.entry(check="images")
        errors, allowed = checker.split_allowed([issue], [entry])
        self.assertEqual(errors, [])
        self.assertEqual(allowed, [(issue, entry)])
        self.assertTrue(entry.used)

    def test_page_check_preserves_modified_and_removed_legal_errors(self):
        path = checker.DOCS_ROOT / "de" / "docs" / REL
        source = checker.load_page("en", checker.DOCS_ROOT / "en" / "docs" / REL,
                                   "# Page {#page}\n\nOriginal.\n")
        for section in ("safety-information", "declaration-of-conformity"):
            before = BEFORE.replace("safety-information", section)
            for after in (before.replace("Approved wording.", "Changed wording."),
                          "# Seite {#page}\n\nText.\n"):
                page = checker.load_page("de", path, after)
                entry = self.entry(section=section)
                with self.subTest(section=section, after=after), \
                        patch.object(Path, "exists", return_value=True), \
                        patch.object(checker, "load_page", side_effect=[page, source,
                                     checker.load_page("de", path, before)]), \
                        patch.object(checker, "text_at", return_value=before), \
                        patch.object(checker, "resolve_base", return_value="base-sha"), \
                        patch.object(checker, "load_allowlist", return_value=[entry]):
                    issues = checker.check_page("de", REL, base="HEAD")
                self.assertTrue(any(issue.check == "protected-section" for issue in issues))
                self.assertFalse(entry.used)


if __name__ == "__main__":
    unittest.main()
