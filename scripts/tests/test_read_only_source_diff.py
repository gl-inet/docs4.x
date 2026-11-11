"""English delta display reads snapshots without writing Git objects or cache."""
from contextlib import redirect_stdout
import io
from pathlib import Path
import subprocess
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import translation_delta as delta
import test_migration_target_baseline as fixtures

SOURCE = fixtures.SOURCE


class ReadOnlySourceDiffTests(unittest.TestCase):
    setUp = fixtures.MigrationTargetBaselineTests.setUp
    git = fixtures.MigrationTargetBaselineTests.git
    put = fixtures.MigrationTargetBaselineTests.put

    def baseline(self, source=SOURCE):
        oid = self.git("rev-parse", "HEAD:" + source).decode().strip()
        delta.write_json(Path(delta.CACHE_FILE), {source: {"targets": {"de": {"source_blob": oid}}}})
        return oid

    def diff(self, source=SOURCE):
        before = Path(delta.CACHE_FILE).read_bytes()
        status = self.git("status", "--porcelain")
        output = io.StringIO()
        with redirect_stdout(output):
            code = delta.cmd_diff([source, "--lang", "de"])
        self.assertEqual(Path(delta.CACHE_FILE).read_bytes(), before)
        self.assertEqual(self.git("status", "--porcelain"), status)
        return code, output.getvalue()

    def test_lf_and_crlf_checkout_are_unchanged(self):
        self.baseline()
        raw = Path(SOURCE).read_bytes()
        for data in (raw, raw.replace(b"\n", b"\r\n")):
            self.put(SOURCE, data)
            code, output = self.diff()
            self.assertEqual(code, 0)
            self.assertIn("has not changed", output)

    def test_changed_text_is_displayed_without_writing_a_blob(self):
        self.baseline()
        self.put(SOURCE, b"# Page {#page}\n\nChanged English.\n")
        oid = self.git("hash-object", "--", SOURCE).decode().strip()
        code, output = self.diff()
        self.assertEqual(code, 0)
        self.assertIn("-Original.", output)
        self.assertIn("+Changed English.", output)
        self.assertNotEqual(subprocess.run(["git", "cat-file", "-e", oid], capture_output=True).returncode, 0)

    def test_deleted_text_displays_removals(self):
        self.baseline()
        Path(SOURCE).unlink()
        code, output = self.diff()
        self.assertEqual(code, 0)
        self.assertIn("-Original.", output)

    def test_missing_or_invalid_snapshot_requests_whole_page(self):
        for blob in (None, "not-an-oid", 123, "0" * 40):
            with self.subTest(blob=blob):
                delta.write_json(Path(delta.CACHE_FILE), {SOURCE: {"targets": {"de": {"source_blob": blob}}}})
                code, output = self.diff()
                self.assertEqual(code, 1)
                self.assertIn("compare the whole page", output)

    def test_binary_unchanged_changed_and_deleted(self):
        source = "docs/en/docs/image.png"
        self.put(source, b"\x89PNG\x00\xff")
        self.git("add", source)
        self.git("commit", "-qm", "binary source")
        self.baseline(source)
        self.assertIn("has not changed", self.diff(source)[1])
        self.put(source, b"\x89PNG\x00\xfe")
        code, output = self.diff(source)
        self.assertEqual(code, 0)
        self.assertIn("Binary source changed", output)
        Path(source).unlink()
        self.assertIn("(deleted)", self.diff(source)[1])

    def test_cached_commit_is_not_a_blob(self):
        commit = self.git("rev-parse", "HEAD").decode().strip()
        delta.write_json(Path(delta.CACHE_FILE), {SOURCE: {"targets": {"de": {"source_blob": commit}}}})
        self.assertEqual(self.diff()[0], 1)

    def test_regulatory_text_is_still_visible_in_full_file_diff(self):
        raw = b"Main.\n\n## Regulatory Statements {#regulatory-statements}\nOld legal text.\n"
        self.put(SOURCE, raw)
        self.git("add", SOURCE)
        self.git("commit", "-qm", "regulatory source")
        self.baseline()
        self.put(SOURCE, raw.replace(b"Old legal", b"New legal"))
        code, output = self.diff()
        self.assertEqual(code, 0)
        self.assertIn("-Old legal text.", output)
        self.assertIn("+New legal text.", output)

    def test_mark_still_requires_existing_source(self):
        Path(SOURCE).unlink()
        with self.assertRaises(SystemExit):
            delta.source_arg(SOURCE)
        self.assertEqual(delta.source_arg(SOURCE, absent=True), SOURCE)
        with self.assertRaises(SystemExit):
            delta.source_arg("docs/de/docs/page.md", absent=True)


if __name__ == "__main__":
    unittest.main()
