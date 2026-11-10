"""Snapshot-authoritative cache checks in disposable, real Git repositories."""
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import anchors
import i18n_check
import precommit
import translation_delta as delta


class PrecommitCacheTests(unittest.TestCase):
    source = "docs/en/docs/page.md"
    target = "docs/de/docs/page.md"
    cache_path = ".translation-cache.json"
    english = b"# English {#page}\n\nOriginal.\n"
    german = b"# Deutsch {#page}\n\nOriginal.\n"
    translated = b"# Deutsch {#page}\n\nGeaendert.\n"

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        old = Path.cwd()
        self.root = Path(temp.name).resolve()
        os.chdir(self.root)
        self.addCleanup(os.chdir, old)
        self.git("init", "-q")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "core.hooksPath", ".disabled-hooks")
        self.git("config", "user.name", "Cache Test")
        self.git("config", "user.email", "cache-test@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.put(self.source, self.english)
        self.put(self.target, self.german)
        self.save_cache(self.record(self.source, self.target, self.english, self.german))
        self.base = self.commit()
        for name, value in (("REPO_ROOT", self.root), ("DOCS_ROOT", self.root / "docs")):
            patcher = patch.object(anchors, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def git(self, *args):
        return subprocess.check_output(
            ["git", *args], stderr=subprocess.STDOUT,
        ).decode("utf-8")

    def commit(self):
        self.git("add", ".")
        self.git("-c", "core.hooksPath=.disabled-hooks", "commit", "-q", "-m", "fixture")
        return self.git("rev-parse", "HEAD").strip()

    def put(self, path, data):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data if isinstance(data, bytes) else data.encode("utf-8"))

    def save_cache(self, cache, stage=True):
        self.put(self.cache_path, json.dumps(cache, ensure_ascii=False))
        if stage:
            self.git("add", "--", self.cache_path)

    @staticmethod
    def digest(data):
        return hashlib.sha256(data).hexdigest()

    def record(self, source, target, english, translated):
        # Independent expected hashes: fixtures here already use normalized LF.
        return {source: {"targets": {target.split("/")[1]: {
            "source_hash": self.digest(english),
            "target_hash": self.digest(translated),
        }}}}

    def errors(self, base=None, files=None):
        if files is None:
            files = precommit.staged_files(base)
        errors = precommit.cache_errors(files, base=base)
        self.assertIsInstance(errors, list)
        self.assertTrue(all(isinstance(error, str) for error in errors))
        return errors

    def stage_translation(self):
        self.put(self.target, self.translated)
        self.git("add", "--", self.target)

    def valid_translation(self):
        self.stage_translation()
        self.save_cache(self.record(self.source, self.target, self.english, self.translated))

    def test_mark_and_check_share_hash_rules_for_text_and_binary_assets(self):
        for rest, english, translated in (
            ("docs/stylesheets/custom.css", b"English\r\n", b"Deutsch\r\n"),
            ("docs/images/logo.svg", b"\xef\xbb\xbf<svg>\r\n", b"\xef\xbb\xbf<svg>Deutsch\r\n"),
            ("docs/images/photo.png", b"\xff\x00\r\n", b"\xff\x01\r\n"),
        ):
            with self.subTest(rest=rest):
                source, target = "docs/en/" + rest, "docs/de/" + rest
                self.put(source, english)
                self.put(target, translated)
                with redirect_stdout(io.StringIO()):
                    result = delta.cmd_mark([source, "--lang", "de", "--model", "regression-test"])
                self.assertEqual(0, result)
                self.git("add", source, target, self.cache_path)
                self.assertEqual([], self.errors())
                self.assertEqual(delta.target_hash(Path(target)),
                                 delta.hash_bytes(Path(target), Path(target).read_bytes()))

    def test_unicode_filename_and_rename_require_new_record(self):
        target = "docs/de/docs/überblick.md"
        source = "docs/en/docs/überblick.md"
        self.git("mv", self.source, source)
        self.git("mv", self.target, target)
        self.assertTrue(self.errors())
        self.save_cache(self.record(source, target, self.english, self.german))
        self.assertEqual([], self.errors())

    def test_added_and_modified_assets_need_matching_records(self):
        assets = (
            "docs/page.md", "mkdocs.yml", "overrides/main.html",
            "docs/stylesheets/custom.css", "docs/images/icon.svg",
            "docs/data/readme.txt", "docs/data/config.json", "docs/images/image.png",
        )
        for rest in assets:
            for added in (True, False):
                with self.subTest(rest=rest, added=added):
                    self.git("reset", "--hard", self.base)
                    self.git("clean", "-fdq")
                    source, target = "docs/en/" + rest, "docs/fr/" + rest
                    binary = rest.endswith(".png")
                    english = b"\x89PNG\r\n\x1a\n\x00\xff" if binary else b"English\n"
                    before = b"\x89PNG\x00\xfe" if binary else b"Ancien\n"
                    after = before + (b"\x00\xfd" if binary else b"Nouveau\n")
                    self.put(source, english)
                    if not added:
                        self.put(target, before)
                    self.commit()
                    self.put(target, after)
                    self.git("add", "--", target)
                    self.save_cache({})
                    self.assertTrue(self.errors(), "missing record must block")
                    self.save_cache(self.record(source, target, english, after))
                    self.assertEqual([], self.errors())

    def test_missing_and_invalid_per_language_hashes_block(self):
        self.stage_translation()
        valid = self.record(self.source, self.target, self.english, self.translated)
        variants = [{}, {self.source: {}}, {self.source: {"targets": {}}}]
        for field in ("source_hash", "target_hash"):
            for value in (None, "", "wrong"):
                cache = json.loads(json.dumps(valid))
                record = cache[self.source]["targets"]["de"]
                if value is None:
                    record.pop(field)
                else:
                    record[field] = value
                variants.append(cache)
        for cache in variants:
            with self.subTest(cache=cache):
                self.save_cache(cache)
                self.assertTrue(self.errors())

    def test_legacy_shared_source_hash_is_rejected(self):
        self.stage_translation()
        cache = self.record(self.source, self.target, self.english, self.translated)
        entry = cache[self.source]
        entry["source_hash"] = entry["targets"]["de"].pop("source_hash")
        self.save_cache(cache)
        self.assertTrue(self.errors())

    def test_unstaged_cache_fix_cannot_hide_stale_index(self):
        self.stage_translation()
        self.save_cache(self.record(self.source, self.target, self.english, self.translated), stage=False)
        self.assertTrue(self.errors())

    def test_index_cache_not_worktree_is_authoritative(self):
        self.valid_translation()
        self.put(self.cache_path, "invalid working-tree JSON")
        self.assertEqual([], self.errors())

    def test_partial_target_staging_uses_index_hash(self):
        self.valid_translation()
        working = self.translated + b"Unstaged text.\n"
        self.put(self.target, working)
        self.assertEqual([], self.errors())
        self.save_cache(self.record(self.source, self.target, self.english, working))
        self.assertTrue(self.errors())

    def test_unstaged_english_cannot_substitute_for_index(self):
        self.stage_translation()
        working = self.english + b"Unstaged English.\n"
        self.put(self.source, working)
        self.save_cache(self.record(self.source, self.target, working, self.translated))
        self.assertTrue(self.errors())
        self.save_cache(self.record(self.source, self.target, self.english, self.translated))
        self.assertEqual([], self.errors())

    def test_staged_source_prose_change_blocks_old_hash(self):
        self.valid_translation()
        changed = self.english + b"New instructions.\n"
        self.put(self.source, changed)
        self.git("add", "--", self.source)
        self.assertTrue(self.errors())
        self.save_cache(self.record(self.source, self.target, changed, self.translated))
        self.assertEqual([], self.errors())

    def test_text_line_endings_normalize_but_bom_is_preserved(self):
        bom = b"\xef\xbb\xbf"
        self.put(self.source, bom + self.english.replace(b"\n", b"\r\n"))
        self.put(self.target, bom + self.translated.replace(b"\n", b"\r"))
        self.git("add", "--", self.source, self.target)
        self.save_cache(self.record(self.source, self.target, bom + self.english, bom + self.translated))
        self.assertEqual([], self.errors())
        self.save_cache(self.record(self.source, self.target, self.english, self.translated))
        self.assertTrue(self.errors(), "BOM must not be discarded from existing hashes")

    def test_binary_hashes_are_raw(self):
        source, target = "docs/en/docs/image.png", "docs/de/docs/image.png"
        raw = b"\xef\xbb\xbfPNG\r\n\x00\xff"
        self.put(source, raw)
        self.put(target, raw)
        self.git("add", "--", source, target)
        self.save_cache(self.record(source, target, raw, raw))
        self.assertEqual([], self.errors())
        self.assertEqual(self.digest(raw), delta.hash_bytes(Path(source), raw))
        self.assertEqual([self.digest(raw)], list(delta.source_hashes(Path(source), raw)))
        for field in ("source_hash", "target_hash"):
            cache = self.record(source, target, raw, raw)
            cache[source]["targets"]["de"][field] = self.digest(b"PNG\n\x00\xff")
            self.save_cache(cache)
            self.assertTrue(self.errors())

    def test_hash_bytes_normalizes_text_without_stripping_bom(self):
        raw = b"\xef\xbb\xbfOne\r\nTwo\rThree\n"
        expected = self.digest(b"\xef\xbb\xbfOne\nTwo\nThree\n")
        self.assertEqual(expected, delta.hash_bytes(Path(self.source), raw))

    def test_regulatory_only_source_changes_accept_both_historical_hashes(self):
        changed = self.english + b"## Regulatory Statements {#regulatory-statements}\n\nNew legal text.\n"
        self.put(self.source, changed)
        self.git("add", "--", self.source)
        self.stage_translation()
        hashes = set(delta.source_hashes(Path(self.source), changed))
        self.assertEqual({self.digest(self.english), self.digest(self.english[:-1])}, hashes)
        for old in (self.english, self.english[:-1]):
            with self.subTest(old=old):
                self.save_cache(self.record(self.source, self.target, old, self.translated))
                self.assertEqual([], self.errors())

    def test_prose_change_before_regulatory_section_still_blocks(self):
        self.valid_translation()
        changed = self.english + b"New prose.\n\n## Regulatory Statements\nLegal text.\n"
        self.put(self.source, changed)
        self.git("add", "--", self.source)
        self.assertTrue(self.errors())

    def test_english_only_change_allows_translation_backlog(self):
        self.put(self.source, self.english + b"New English.\n")
        self.git("add", "--", self.source)
        self.assertEqual([], self.errors())

    def test_unrelated_changes_ignore_invalid_unstaged_cache(self):
        self.put(self.cache_path, "not JSON")
        self.put("README.txt", "unrelated")
        self.git("add", "--", "README.txt")
        self.assertEqual([], self.errors())

    def test_cache_only_malformed_or_nonobject_json_blocks(self):
        for data in ("{invalid", "[]", "null", '"string"', "42"):
            with self.subTest(data=data):
                self.put(self.cache_path, data)
                self.git("add", "--", self.cache_path)
                self.assertTrue(self.errors())

    def test_cache_only_does_not_validate_whole_repo(self):
        cache = {self.source: {"targets": {"de": {"target_hash": "stale"}, "fr": {}}}}
        self.save_cache(cache)
        self.assertEqual([], self.errors())

    def test_changed_language_does_not_require_other_languages(self):
        self.stage_translation()
        cache = self.record(self.source, self.target, self.english, self.translated)
        cache[self.source]["targets"]["fr"] = {"source_hash": "stale"}
        self.save_cache(cache)
        self.assertEqual([], self.errors())

    def test_uk_is_a_supported_language(self):
        target = "docs/uk/docs/page.md"
        self.put(target, "# Сторінка {#page}\n")
        self.git("add", "--", target)
        self.assertTrue(self.errors())
        self.save_cache(self.record(self.source, target, self.english, Path(target).read_bytes()))
        self.assertEqual([], self.errors())

    def test_missing_index_source_skips_even_with_worktree_source(self):
        self.put("docs/de/docs/local-only.md", "Localized only\n")
        self.git("add", "--", "docs/de/docs/local-only.md")
        self.put("docs/en/docs/local-only.md", "Unstaged source\n")
        self.assertEqual([], self.errors())

    def test_downloads_index_is_excluded(self):
        for lang in ("en", "de", "uk"):
            path = f"docs/{lang}/docs/downloads/index.md"
            self.put(path, "Downloads\n")
            self.git("add", "--", path)
        self.save_cache({})
        self.assertEqual([], self.errors())

    def test_deleted_target_is_skipped(self):
        self.git("rm", "--", self.target)
        self.save_cache({})
        self.assertEqual([], self.errors())

    def test_deleted_source_means_no_counterpart(self):
        self.stage_translation()
        self.git("rm", "--", self.source)
        self.save_cache({})
        self.assertEqual([], self.errors())

    def test_base_valid_head_ignores_dirty_index_and_worktree(self):
        self.valid_translation()
        self.commit()
        self.git("rm", "--", self.source)
        self.put(self.target, b"Staged target\n")
        self.put(self.cache_path, "invalid index JSON")
        self.git("add", "--", self.target, self.cache_path)
        self.put(self.source, b"Working source\n")
        self.put(self.target, b"Working target\n")
        self.put(self.cache_path, "invalid worktree JSON")
        self.assertEqual([], self.errors(base=self.base))
        # Literal --base HEAD still selects HEAD blobs, not the index.
        self.assertEqual([], self.errors(base="HEAD", files=[("M", self.target)]))
        self.assertEqual([], precommit.staged_files("HEAD"))
        self.assertEqual(0, self.run_main(["--base", "HEAD"]))

    def test_base_stale_head_cannot_be_fixed_by_dirty_index(self):
        self.stage_translation()
        self.commit()
        self.save_cache(self.record(self.source, self.target, self.english, self.translated))
        self.put(self.cache_path, "invalid worktree JSON")
        self.assertTrue(self.errors(base=self.base))
        self.assertTrue(self.errors(base="HEAD", files=[("M", self.target)]))

    def test_base_source_existence_uses_head_not_index_or_worktree(self):
        target, source = "docs/de/docs/local-only.md", "docs/en/docs/local-only.md"
        self.put(target, "Localized only\n")
        self.commit()
        self.put(source, "New staged source\n")
        self.git("add", "--", source)
        self.assertEqual([], self.errors(base=self.base))

    def test_base_source_prose_uses_head_not_dirty_source(self):
        self.valid_translation()
        self.put(self.source, self.english + b"New HEAD prose\n")
        self.commit()
        self.put(self.source, self.english)
        self.git("add", "--", self.source)
        self.assertTrue(self.errors(base=self.base))

    def test_base_cache_only_malformed_head_blocks_despite_index_fix(self):
        self.put(self.cache_path, "{invalid")
        self.commit()
        self.save_cache({})
        self.assertTrue(self.errors(base=self.base))

    def run_main(self, argv, anchor_error=False):
        def check_lang(lang, pages, english, report):
            if anchor_error:
                report.errors.append(f"{lang}/page.md: injected anchor error")

        with patch.object(anchors, "load_lang", return_value={}), \
                patch.object(anchors, "check_lang", side_effect=check_lang), \
                patch.object(i18n_check, "check_language_files", return_value=[]), \
                patch.object(i18n_check, "check_page", return_value=[]), \
                patch.object(precommit, "add_missing_ids"), redirect_stdout(io.StringIO()):
            return precommit.main(argv)

    def test_main_staged_cache_error_returns_one(self):
        self.stage_translation()
        self.assertEqual(1, self.run_main([]))

    def test_main_base_cache_error_returns_one(self):
        self.stage_translation()
        self.commit()
        self.assertEqual(1, self.run_main(["--base", self.base]))

    def test_main_base_noncache_error_also_returns_one(self):
        self.valid_translation()
        self.commit()
        self.assertEqual(1, self.run_main(["--base", self.base], anchor_error=True))

    def test_main_checks_cache_when_only_css_config_or_binary_changed(self):
        for rest in ("docs/stylesheets/custom.css", "mkdocs.yml", "docs/images/image.png"):
            with self.subTest(rest=rest):
                self.git("reset", "--hard", self.base)
                self.git("clean", "-fdq")
                source, target = "docs/en/" + rest, "docs/de/" + rest
                raw = b"\x89PNG\x00\xff" if rest.endswith(".png") else b"content\n"
                self.put(source, raw)
                self.put(target, raw)
                self.git("add", "--", source, target)
                self.assertEqual(1, self.run_main([]))
                self.commit()
                self.assertEqual(1, self.run_main(["--base", self.base]))

    def test_main_cache_only_malformed_json_returns_one(self):
        self.put(self.cache_path, "{invalid")
        self.git("add", "--", self.cache_path)
        self.assertEqual(1, self.run_main([]))
        self.commit()
        self.assertEqual(1, self.run_main(["--base", self.base]))

    def test_main_valid_snapshot_returns_zero(self):
        self.valid_translation()
        self.assertEqual(0, self.run_main([]))
        self.commit()
        self.assertEqual(0, self.run_main(["--base", self.base]))
        self.assertEqual(0, self.run_main(["--base", "HEAD"]))


if __name__ == "__main__":
    unittest.main()
