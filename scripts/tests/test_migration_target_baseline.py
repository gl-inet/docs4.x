"""Legacy migration only seeds target hashes from committed translations."""
from contextlib import redirect_stdout
import io
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import translation_delta as delta

SOURCE = "docs/en/docs/page.md"
TARGET = "docs/de/docs/page.md"
ORIGINAL = b"# Seite {#page}\n\nApproved translation.\n"


class MigrationTargetBaselineTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        old = Path.cwd()
        os.chdir(temp.name)
        self.addCleanup(os.chdir, old)
        self.git("init", "-q")
        for key, value in (("user.name", "Test"), ("user.email", "test@example.invalid"),
                           ("core.autocrlf", "false"), ("core.hooksPath", ".disabled-hooks"),
                           ("commit.gpgsign", "false")):
            self.git("config", key, value)
        self.put(SOURCE, b"# Page {#page}\n\nOriginal.\n")
        self.put(TARGET, ORIGINAL)
        self.git("add", ".")
        self.git("commit", "-qm", "committed baseline")
        source = Path(SOURCE)
        self.legacy = delta.source_hashes(source, source.read_bytes())[0]
        self.cache = {SOURCE: {"source_hash": self.legacy,
                               "targets": {"de": {"model": "old", "updated_at": 123}}}}

    def git(self, *args):
        return subprocess.check_output(["git", *args], stderr=subprocess.STDOUT)

    def put(self, name, data):
        path = Path(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def migrate(self):
        delta.write_json(Path(delta.CACHE_FILE), self.cache)
        with redirect_stdout(io.StringIO()):
            self.assertEqual(delta.cmd_migrate([]), 0)
        return delta.read_json(Path(delta.CACHE_FILE))[SOURCE]["targets"]["de"]

    def test_unchanged_committed_translation_seeds_target_hash(self):
        record = self.migrate()
        self.assertEqual(record["target_hash"], delta.target_hash(Path(TARGET)))
        self.assertEqual(record["model"], "old")
        self.assertEqual(record["updated_at"], 123)

    def test_unstaged_translation_edit_does_not_seed_target_hash(self):
        self.put(TARGET, b"Changed but not reviewed.\n")
        record = self.migrate()
        self.assertNotIn("target_hash", record)
        self.assertEqual(record["source_hash"], self.legacy)

    def test_staged_translation_edit_does_not_seed_target_hash(self):
        self.put(TARGET, b"Staged but not reviewed.\n")
        self.git("add", TARGET)
        before = self.git("show", ":" + TARGET)
        self.assertNotIn("target_hash", self.migrate())
        self.assertEqual(self.git("show", ":" + TARGET), before)

    def test_untracked_translation_has_no_committed_baseline(self):
        self.git("rm", TARGET)
        self.git("commit", "-qm", "remove translation")
        self.put(TARGET, ORIGINAL)
        self.assertNotIn("target_hash", self.migrate())

    def test_line_ending_only_checkout_change_still_matches(self):
        self.put(TARGET, ORIGINAL.replace(b"\n", b"\r\n"))
        self.assertEqual(self.migrate()["target_hash"], delta.hash_bytes(Path(TARGET), ORIGINAL))

    def test_existing_target_hash_is_preserved(self):
        self.cache[SOURCE]["targets"]["de"]["target_hash"] = "existing-baseline"
        self.put(TARGET, b"Unreviewed edit.\n")
        self.assertEqual(self.migrate()["target_hash"], "existing-baseline")


if __name__ == "__main__":
    unittest.main()
