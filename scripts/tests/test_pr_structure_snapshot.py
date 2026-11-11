"""PR structure checks read committed docs/config, not index/worktree repairs."""
from contextlib import redirect_stdout
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import anchors
import i18n_check
import precommit
import translation_delta as delta

SOURCE = "docs/en/docs/page.md"
TARGET = "docs/de/docs/page.md"


class StructureSnapshotTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name).resolve()
        old = Path.cwd()
        os.chdir(self.root)
        self.addCleanup(os.chdir, old)
        for module, name, value in (
            (anchors, "REPO_ROOT", self.root), (anchors, "DOCS_ROOT", self.root / "docs"),
            (i18n_check, "REPO_ROOT", self.root), (i18n_check, "DOCS_ROOT", self.root / "docs"),
            (i18n_check, "ALLOWLIST_PATH", self.root / "scripts/i18n_allowlist.yml"),
        ):
            p = patch.object(module, name, value)
            p.start()
            self.addCleanup(p.stop)
        self.git("init", "-q")
        for key, value in (("user.name", "Test"), ("user.email", "test@example.invalid"),
                           ("core.autocrlf", "false"), ("core.hooksPath", ".disabled-hooks"),
                           ("commit.gpgsign", "false")):
            self.git("config", key, value)
        self.put(SOURCE, "# Page {#page}\n\nOriginal.\n")
        self.put(TARGET, "# Seite {#page}\n\nText.\n")
        for lang in ("en", "de"):
            self.put(f"docs/{lang}/mkdocs.yml", "plugins: []\n")
        self.put("scripts/i18n_allowlist.yml", "[]\n")
        self.record()
        self.commit("base")
        self.base = self.git("rev-parse", "HEAD").strip()

    def git(self, *args):
        return subprocess.check_output(["git", *args], stderr=subprocess.STDOUT).decode("utf-8")

    def put(self, path, text):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode("utf-8"))

    def commit(self, message):
        self.git("add", ".")
        self.git("commit", "-qm", message)

    def record(self):
        self.put(delta.CACHE_FILE, json.dumps({SOURCE: {"targets": {"de": {
            "source_hash": delta.source_hashes(Path(SOURCE), Path(SOURCE).read_bytes())[0],
            "target_hash": delta.target_hash(Path(TARGET)),
        }}}}))

    def run_check(self):
        output = io.StringIO()
        with redirect_stdout(output):
            result = precommit.main(["--base", self.base])
        return result, output.getvalue()

    def test_related_page_uses_head_not_dirty_worktree(self):
        self.put(SOURCE, "# Page {#page}\n\n[Other](other.md#other)\n")
        self.put("docs/en/docs/other.md", "# Other {#other}\n")
        self.commit("links")
        self.put("docs/en/docs/other.md", "# Other {#different}\n")
        code, output = self.run_check()
        self.assertEqual(code, 0, output)

    def test_committed_broken_link_cannot_be_hidden_by_worktree_fix(self):
        self.put(SOURCE, "# Page {#page}\n\n[Other](other.md#other)\n")
        self.put("docs/en/docs/other.md", "# Other {#different}\n")
        self.commit("broken link")
        self.put("docs/en/docs/other.md", "# Other {#other}\n")
        code, output = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertIn("broken anchor link", output)

    def test_redirect_config_uses_head(self):
        path = "docs/en/mkdocs.yml"
        self.put(path, "plugins:\n  - redirects:\n      redirect_maps:\n        old.md: page.md\n")
        self.commit("valid redirect")
        self.put(path, "plugins:\n  - redirects:\n      redirect_maps:\n        old.md: missing.md\n")
        code, output = self.run_check()
        self.assertEqual(code, 0, output)

    def test_dirty_source_target_cache_and_allowlist_do_not_change_result(self):
        self.put(TARGET, "# Seite {#page}\n\nAnderer Text.\n")
        self.record()
        self.commit("translation")
        for path in (SOURCE, TARGET):
            self.put(path, "# Dirty heading without ID\n")
        self.put(delta.CACHE_FILE, "invalid JSON")
        self.put("scripts/i18n_allowlist.yml", "invalid: [yaml")
        self.git("add", ".")
        before = self.git("diff", "--cached", "--binary")
        code, output = self.run_check()
        self.assertEqual(code, 0, output)
        self.assertEqual(self.git("diff", "--cached", "--binary"), before)
        self.assertEqual(Path(TARGET).read_text(encoding="utf-8"), "# Dirty heading without ID\n")

    def test_legal_comparison_still_reads_real_git_baseline(self):
        legal = "\n## Sicherheit {#safety-information}\n\nApproved wording.\n"
        self.put(TARGET, Path(TARGET).read_text(encoding="utf-8") + legal)
        self.record()
        self.commit("approved legal section")
        self.base = self.git("rev-parse", "HEAD").strip()
        self.put(TARGET, "# Seite {#page}\n\nAnderer Text.\n")
        self.record()
        self.commit("removed legal section")
        code, output = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertIn("protected-section", output)

    def test_export_attributes_do_not_filter_snapshot_and_roots_restore(self):
        self.put(".gitattributes", "docs/en/docs/page.md export-ignore\n")
        self.commit("export attribute")
        roots = anchors.REPO_ROOT, anchors.DOCS_ROOT, i18n_check.DOCS_ROOT, i18n_check.ALLOWLIST_PATH
        with precommit.committed_docs("HEAD"):
            self.assertEqual((anchors.REPO_ROOT / SOURCE).read_bytes(),
                             subprocess.check_output(["git", "show", "HEAD:" + SOURCE]))
            self.assertEqual(i18n_check.ALLOWLIST_PATH.read_text(encoding="utf-8"), "[]\n")
        self.assertEqual(roots, (anchors.REPO_ROOT, anchors.DOCS_ROOT,
                                i18n_check.DOCS_ROOT, i18n_check.ALLOWLIST_PATH))

    def test_snapshot_rejects_symlinks_without_following_them(self):
        oid = subprocess.check_output(["git", "hash-object", "-w", "--stdin"],
                                      input=b"../../../../outside.md").decode().strip()
        self.git("update-index", "--add", "--cacheinfo", "120000", oid, "docs/en/docs/link.md")
        self.git("commit", "-qm", "symlink")
        code, output = self.run_check()
        self.assertEqual(code, 1, output)
        self.assertIn("documentation must be a regular file", output)


if __name__ == "__main__":
    unittest.main()
