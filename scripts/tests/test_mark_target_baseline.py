"""Mark must not advance unchanged translations when legacy target hashes are absent."""
from contextlib import redirect_stdout
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import translation_delta as delta
import test_migration_target_baseline as fixtures

SOURCE, TARGET = fixtures.SOURCE, fixtures.TARGET


class MarkTargetBaselineTests(unittest.TestCase):
    setUp = fixtures.MigrationTargetBaselineTests.setUp
    git = fixtures.MigrationTargetBaselineTests.git
    put = fixtures.MigrationTargetBaselineTests.put

    def prepare(self):
        delta.write_json(Path(delta.CACHE_FILE), self.cache)
        self.put(SOURCE, b"# Page {#page}\n\nChanged English.\n")

    def mark(self, *extra):
        output = io.StringIO()
        with patch.object(delta, "check_target", return_value=[]), redirect_stdout(output):
            code = delta.cmd_mark([SOURCE, "--lang", "de", *extra])
        return code, output.getvalue()

    def test_missing_target_hash_uses_head_and_leaves_failed_cache_unchanged(self):
        self.prepare()
        before = Path(delta.CACHE_FILE).read_bytes()
        code, output = self.mark()
        self.assertEqual(code, 1, output)
        self.assertIn("English changed", output)
        self.assertIn("--no-target-change", output)
        self.assertEqual(Path(delta.CACHE_FILE).read_bytes(), before)

    def test_no_target_change_requires_explicit_review(self):
        self.prepare()
        code, output = self.mark("--no-target-change")
        self.assertEqual(code, 0, output)
        record = delta.read_json(Path(delta.CACHE_FILE))[SOURCE]["targets"]["de"]
        self.assertEqual(record["model"], delta.NO_TARGET_CHANGE_MODEL)
        self.assertEqual(record["target_hash"], delta.target_hash(Path(TARGET)))

    def test_changed_translation_can_be_marked(self):
        self.prepare()
        self.put(TARGET, b"# Seite {#page}\n\nUpdated translation.\n")
        code, output = self.mark()
        self.assertEqual(code, 0, output)
        self.assertEqual(delta.read_json(Path(delta.CACHE_FILE))[SOURCE]["targets"]["de"]["target_hash"],
                         delta.target_hash(Path(TARGET)))

    def test_crlf_only_translation_change_still_requires_review(self):
        self.prepare()
        self.put(TARGET, fixtures.ORIGINAL.replace(b"\n", b"\r\n"))
        self.assertEqual(self.mark()[0], 1)

    def test_new_translation_without_head_baseline_can_be_marked(self):
        self.git("rm", TARGET)
        self.git("commit", "-qm", "translation not yet present")
        self.prepare()
        self.put(TARGET, b"# Seite {#page}\n\nNew translation.\n")
        code, output = self.mark()
        self.assertEqual(code, 0, output)

    def test_saved_baseline_takes_precedence_over_head(self):
        self.cache[SOURCE]["targets"]["de"]["target_hash"] = "older-translation-hash"
        self.prepare()
        code, output = self.mark()
        self.assertEqual(code, 0, output)

    def test_saved_target_hash_stays_authoritative(self):
        self.cache[SOURCE]["targets"]["de"]["target_hash"] = delta.target_hash(Path(TARGET))
        self.prepare()
        before = Path(delta.CACHE_FILE).read_bytes()
        self.assertEqual(self.mark()[0], 1)
        self.assertEqual(Path(delta.CACHE_FILE).read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
