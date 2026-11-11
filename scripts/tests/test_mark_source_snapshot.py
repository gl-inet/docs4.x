"""Mark stores only HEAD-reachable English snapshots, never dangling blobs."""
from contextlib import redirect_stdout
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import translation_delta as delta
import test_migration_target_baseline as fixtures

SOURCE, TARGET = fixtures.SOURCE, fixtures.TARGET


class MarkSourceSnapshotTests(unittest.TestCase):
    setUp = fixtures.MigrationTargetBaselineTests.setUp
    git = fixtures.MigrationTargetBaselineTests.git
    put = fixtures.MigrationTargetBaselineTests.put

    def mark(self):
        output = io.StringIO()
        with patch.object(delta, "check_target", return_value=[]), redirect_stdout(output):
            code = delta.cmd_mark([SOURCE, "--lang", "de"])
        self.assertEqual(code, 0, output.getvalue())
        return delta.read_json(Path(delta.CACHE_FILE))[SOURCE]["targets"]["de"], output.getvalue()

    def prepare(self):
        delta.write_json(Path(delta.CACHE_FILE), self.cache)
        self.put(TARGET, b"# Seite {#page}\n\nUpdated translation.\n")

    def test_committed_snapshot_survives_fresh_clone(self):
        raw = Path(SOURCE).read_bytes()
        oid = self.git("rev-parse", "HEAD:" + SOURCE).decode().strip()
        self.prepare()
        record, output = self.mark()
        self.assertEqual(record["source_blob"], oid)
        self.assertNotIn("no reachable snapshot", output)
        self.git("add", ".")
        self.git("commit", "-qm", "record translation")
        with tempfile.TemporaryDirectory() as clone:
            self.git("clone", "-q", "--no-local", str(Path.cwd()), clone)
            cloned = delta.read_json(Path(clone) / delta.CACHE_FILE)[SOURCE]["targets"]["de"]
            self.assertEqual(subprocess.check_output(
                ["git", "-C", clone, "cat-file", "blob", cloned["source_blob"]]), raw)

    def test_uncommitted_source_marks_without_snapshot_or_object_write(self):
        self.prepare()
        self.put(SOURCE, b"Uncommitted English.\n")
        oid = self.git("hash-object", "--", SOURCE).decode().strip()
        record, output = self.mark()
        self.assertNotIn("source_blob", record)
        self.assertIn("no reachable snapshot", output)
        self.assertEqual(record["source_hash"], delta.source_hashes(Path(SOURCE), Path(SOURCE).read_bytes())[0])
        self.assertEqual(record["target_hash"], delta.target_hash(Path(TARGET)))
        self.assertNotEqual(subprocess.run(["git", "cat-file", "-e", oid], capture_output=True).returncode, 0)
        with redirect_stdout(io.StringIO()):
            self.assertEqual(delta.cmd_diff([SOURCE, "--lang", "de"]), 1)

    def test_staged_source_is_not_yet_a_reachable_snapshot(self):
        self.prepare()
        self.put(SOURCE, b"Staged English.\n")
        self.git("add", SOURCE)
        before = self.git("show", ":" + SOURCE)
        record, _ = self.mark()
        self.assertNotIn("source_blob", record)
        self.assertEqual(self.git("show", ":" + SOURCE), before)

    def test_new_record_clears_stale_blob_without_changing_other_language(self):
        old_blob = self.git("rev-parse", "HEAD:" + SOURCE).decode().strip()
        self.cache[SOURCE]["targets"]["de"]["source_blob"] = old_blob
        other = {"source_hash": self.legacy, "source_blob": old_blob, "model": "keep"}
        self.cache[SOURCE]["targets"]["ja"] = other.copy()
        self.prepare()
        self.put(SOURCE, b"New uncommitted English.\n")
        record, _ = self.mark()
        self.assertNotIn("source_blob", record)
        self.assertEqual(delta.read_json(Path(delta.CACHE_FILE))[SOURCE]["targets"]["ja"], other)

    def test_crlf_checkout_can_use_committed_normalized_snapshot(self):
        raw = Path(SOURCE).read_bytes()
        oid = self.git("rev-parse", "HEAD:" + SOURCE).decode().strip()
        self.prepare()
        self.put(SOURCE, raw.replace(b"\n", b"\r\n"))
        self.assertEqual(self.mark()[0]["source_blob"], oid)

    def test_matching_historical_source_can_be_reused(self):
        original = Path(SOURCE).read_bytes()
        oid = self.git("rev-parse", "HEAD:" + SOURCE).decode().strip()
        self.put(SOURCE, b"Later committed English.\n")
        self.git("add", SOURCE)
        self.git("commit", "-qm", "later source")
        self.prepare()
        self.put(SOURCE, original)
        self.assertEqual(self.mark()[0]["source_blob"], oid)

    def test_noop_does_not_rewrite_cache(self):
        self.prepare()
        self.mark()
        before = Path(delta.CACHE_FILE).read_bytes()
        self.mark()
        self.assertEqual(Path(delta.CACHE_FILE).read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
