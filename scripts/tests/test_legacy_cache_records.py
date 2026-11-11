"""Legacy migration preserves real records without inventing synced languages."""
from contextlib import redirect_stdout
import copy
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import translation_delta as delta

SOURCE = "docs/en/docs/page.md"


class LegacyRecordTests(unittest.TestCase):
    def test_missing_language_does_not_inherit_shared_hash(self):
        entry = {"source_hash": "legacy", "targets": {"de": {"model": "old"}}}
        before = copy.deepcopy(entry)
        self.assertEqual(delta.target_record({SOURCE: entry}, SOURCE, "ja"), {})
        self.assertEqual(delta.target_record({SOURCE: entry}, SOURCE, "de"),
                         {"model": "old", "source_hash": "legacy"})
        self.assertEqual(entry, before)

    def test_invalid_record_is_not_a_baseline(self):
        for record in (None, "old"):
            with self.subTest(record=record):
                self.assertEqual(delta.target_record({SOURCE: {
                    "source_hash": "legacy", "targets": {"de": record}}}, SOURCE, "de"), {})

    def test_upgrade_keeps_only_existing_records_and_metadata(self):
        entry = {"source_hash": "legacy", "targets": {
            "de": {"model": "old", "updated_at": 123},
            "fr": {"source_hash": "newer", "source_blob": "newer-blob", "target_hash": "target"},
        }}
        delta.upgrade_entry(entry)
        self.assertNotIn("source_hash", entry)
        self.assertEqual(set(entry["targets"]), {"de", "fr"})
        self.assertEqual(entry["targets"]["de"], {"model": "old", "updated_at": 123,
                                                 "source_hash": "legacy"})
        self.assertEqual(entry["targets"]["fr"], {"source_hash": "newer", "source_blob": "newer-blob",
                                                 "target_hash": "target"})

    def test_empty_targets_do_not_create_language_records(self):
        for entry in ({"source_hash": "legacy"}, {"source_hash": "legacy", "targets": {}}):
            delta.upgrade_entry(entry)
            self.assertFalse(entry.get("targets"))

    def test_migrate_preserves_missing_languages_and_newer_baselines(self):
        with tempfile.TemporaryDirectory() as temp:
            old = Path.cwd()
            os.chdir(temp)
            try:
                source = Path(SOURCE)
                source.parent.mkdir(parents=True)
                source.write_text("Original.\n", encoding="utf-8")
                legacy = delta.sync_hashes(source, source.read_text(encoding="utf-8"))[0]
                for lang in ("de", "ja"):
                    target = delta.target_path_for_lang(SOURCE, lang)
                    target.parent.mkdir(parents=True)
                    target.write_text("Translation.\n", encoding="utf-8")
                cache = {SOURCE: {"source_hash": legacy, "targets": {
                    "de": {"model": "old", "updated_at": 123},
                    "fr": {"source_hash": "newer", "source_blob": "newer-blob"},
                }}}
                delta.write_json(Path(delta.CACHE_FILE), cache)
                with patch.object(delta, "find_source_blob", return_value="legacy-blob"), \
                        redirect_stdout(io.StringIO()):
                    self.assertEqual(delta.cmd_migrate([]), 0)
                result = json.loads(Path(delta.CACHE_FILE).read_text(encoding="utf-8"))[SOURCE]
                self.assertEqual(set(result["targets"]), {"de", "fr"})
                self.assertEqual(result["targets"]["de"]["model"], "old")
                self.assertEqual(result["targets"]["fr"], {"source_hash": "newer", "source_blob": "newer-blob"})
                status = delta.analyze_sources([source], {SOURCE: result}, ["de", "ja"])[0]
                self.assertEqual(status.cache_missing, ["ja"])
            finally:
                os.chdir(old)


if __name__ == "__main__":
    unittest.main()
