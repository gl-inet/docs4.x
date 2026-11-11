"""Legacy snapshot lookup uses exact bytes from HEAD-reachable history."""
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import translation_delta as delta
import test_migration_target_baseline as fixtures

SOURCE = fixtures.SOURCE


class SourceBlobLookupTests(unittest.TestCase):
    setUp = fixtures.MigrationTargetBaselineTests.setUp
    git = fixtures.MigrationTargetBaselineTests.git
    put = fixtures.MigrationTargetBaselineTests.put

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "source version")

    def legacy_hash(self, raw):
        return delta.legacy_hashes(Path(SOURCE), delta.normalized_text(raw))[0]

    def test_dirty_source_does_not_create_a_dangling_blob(self):
        raw = b"Uncommitted English version.\n"
        self.put(SOURCE, raw)
        oid = self.git("hash-object", "--", SOURCE).decode().strip()
        self.assertIsNone(delta.find_source_blob(SOURCE, self.legacy_hash(raw)))
        self.assertNotEqual(subprocess.run(["git", "cat-file", "-e", oid],
                                          capture_output=True).returncode, 0)

    def test_exact_whitespace_and_newlines_are_not_guessed(self):
        raw = b"  English with trailing spaces.  \n\n\n"
        self.put(SOURCE, raw)
        self.commit()
        oid = self.git("rev-parse", "HEAD:" + SOURCE).decode().strip()
        self.assertEqual(delta.find_source_blob(SOURCE, self.legacy_hash(raw)), oid)
        self.assertIsNone(delta.find_source_blob(SOURCE, self.legacy_hash(raw.strip() + b"\n")))
        self.assertIsNone(delta.find_source_blob(SOURCE, self.legacy_hash(raw.rstrip())))
        self.assertEqual(delta.find_source_blob(SOURCE, self.legacy_hash(raw.replace(b"\n", b"\r\n"))), oid)

    def test_history_beyond_one_hundred_source_changes(self):
        oid = self.git("rev-parse", "HEAD:" + SOURCE).decode().strip()
        for index in range(101):
            self.put(SOURCE, f"New source {index}.\n".encode())
            self.commit()
        self.assertEqual(delta.find_source_blob(SOURCE, self.legacy), oid)

    def test_deleted_working_file_can_still_be_looked_up(self):
        oid = self.git("rev-parse", "HEAD:" + SOURCE).decode().strip()
        self.git("rm", SOURCE)
        self.commit()
        self.assertEqual(delta.find_source_blob(SOURCE, self.legacy), oid)

    def test_sibling_branch_is_not_a_portable_baseline(self):
        head = self.git("rev-parse", "HEAD").decode().strip()
        self.git("checkout", "-qb", "sibling")
        raw = b"English found only on a sibling branch.\n"
        self.put(SOURCE, raw)
        self.commit()
        self.git("checkout", "-q", "--detach", head)
        self.assertIsNone(delta.find_source_blob(SOURCE, self.legacy_hash(raw)))

    def test_router_regulatory_and_legacy_hash_variants_are_preserved(self):
        raw = b"Main content.\n\n## Regulatory Statements {#regulatory-statements}\nLegal text.\n"
        self.put(SOURCE, raw)
        self.commit()
        oid = self.git("rev-parse", "HEAD:" + SOURCE).decode().strip()
        self.put(SOURCE, b"New English.\n")
        for expected in delta.legacy_hashes(Path(SOURCE), raw.decode()):
            with self.subTest(expected=expected):
                self.assertEqual(delta.find_source_blob(SOURCE, expected), oid)

    def test_binary_and_invalid_historical_utf8(self):
        binary = "docs/en/docs/image.png"
        raw = b"\x89PNG\r\n\xff\x00"
        self.put(binary, raw)
        self.put(SOURCE, b"\xffnot valid UTF-8")
        self.commit()
        self.assertEqual(delta.find_source_blob(binary, hashlib.sha256(raw).hexdigest()),
                         self.git("rev-parse", "HEAD:" + binary).decode().strip())
        self.assertIsNone(delta.find_source_blob(SOURCE, "unknown"))

    def test_migrated_snapshot_survives_fresh_clone(self):
        oid = self.git("rev-parse", "HEAD:" + SOURCE).decode().strip()
        original = Path(SOURCE).read_bytes()
        self.put(SOURCE, b"Changed after translation.\n")
        self.commit()
        record = fixtures.MigrationTargetBaselineTests.migrate(self)
        self.assertEqual(record["source_blob"], oid)
        self.assertEqual(record["model"], "old")
        self.assertNotIn("target_hash", record)
        before = Path(delta.CACHE_FILE).read_bytes()
        self.assertEqual(delta.cmd_migrate([]), 0)
        self.assertEqual(Path(delta.CACHE_FILE).read_bytes(), before)
        self.commit()
        with tempfile.TemporaryDirectory() as clone:
            self.git("clone", "-q", "--no-local", str(Path.cwd()), clone)
            cloned = delta.read_json(Path(clone) / delta.CACHE_FILE)[SOURCE]["targets"]["de"]
            self.assertEqual(subprocess.check_output(
                ["git", "-C", clone, "cat-file", "blob", cloned["source_blob"]]), original)

    def test_repeated_blob_is_read_only_once(self):
        original = Path(SOURCE).read_bytes()
        self.put(SOURCE, b"Intermediate.\n")
        self.commit()
        self.put(SOURCE, original)
        self.commit()
        run = subprocess.run
        with patch.object(delta.subprocess, "run", wraps=run) as calls:
            self.assertIsNone(delta.find_source_blob(SOURCE, "unknown"))
        blob_reads = [call for call in calls.call_args_list if call.args[0][1:3] == ["cat-file", "blob"]]
        self.assertEqual(len(blob_reads), 2)


if __name__ == "__main__":
    unittest.main()
