"""Check staged headings/anchors without modifying partially staged pages."""
from contextlib import redirect_stdout
import io
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

PAGE = "docs/en/docs/page.md"
BASE = "# Page {#page}\n"


class StagedAnchorTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name).resolve()
        old = Path.cwd()
        os.chdir(self.root)
        self.addCleanup(os.chdir, old)
        for module, name, value in (
            (anchors, "REPO_ROOT", self.root),
            (anchors, "DOCS_ROOT", self.root / "docs"),
            (i18n_check, "DOCS_ROOT", self.root / "docs"),
        ):
            p = patch.object(module, name, value)
            p.start()
            self.addCleanup(p.stop)
        self.git("init", "-q")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "core.hooksPath", ".disabled-hooks")
        self.git("config", "commit.gpgsign", "false")
        self.put(PAGE, BASE)
        self.git("add", ".")
        self.git("commit", "-qm", "base")

    def git(self, *args):
        return subprocess.check_output(["git", *args], stderr=subprocess.STDOUT).decode("utf-8")

    def put(self, path, text):
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(text.encode("utf-8"))

    def run_hook(self):
        output = io.StringIO()
        with redirect_stdout(output):
            result = precommit.main([])
        return result, output.getvalue()

    def test_unstaged_id_fix_cannot_hide_missing_staged_id(self):
        staged = BASE + "\n## New heading\n"
        working = BASE + "\n## New heading {#new-heading}\n"
        self.put(PAGE, staged)
        self.git("add", PAGE)
        self.put(PAGE, working)
        code, output = self.run_hook()
        self.assertEqual(code, 1, output)
        self.assertIn("heading has no explicit ID", output)
        self.assertEqual(self.git("show", ":" + PAGE), staged)
        self.assertEqual(Path(PAGE).read_text(encoding="utf-8"), working)

    def test_unstaged_broken_link_does_not_block_valid_staged_page(self):
        staged = BASE + "\n[Page](#page)\n"
        working = BASE + "\n[Page](#missing)\n"
        self.put(PAGE, staged)
        self.git("add", PAGE)
        self.put(PAGE, working)
        code, output = self.run_hook()
        self.assertEqual(code, 0, output)
        self.assertEqual(self.git("show", ":" + PAGE), staged)
        self.assertEqual(Path(PAGE).read_text(encoding="utf-8"), working)

    def test_unstaged_link_fix_cannot_hide_broken_staged_link(self):
        self.put(PAGE, BASE + "\n[Page](#missing)\n")
        self.git("add", PAGE)
        self.put(PAGE, BASE + "\n[Page](#page)\n")
        code, output = self.run_hook()
        self.assertEqual(code, 1, output)
        self.assertIn("broken anchor link", output)

    def test_fully_staged_page_still_gets_ids_automatically(self):
        self.put(PAGE, BASE + "\n## New heading\n")
        self.git("add", PAGE)
        code, output = self.run_hook()
        self.assertEqual(code, 0, output)
        self.assertIn("## New heading {#new-heading}", self.git("show", ":" + PAGE))
        self.assertEqual(self.git("diff", "--name-only"), "")

    def test_staged_deletion_does_not_use_recreated_worktree_page(self):
        self.git("rm", PAGE)
        self.put(PAGE, "# Unstaged recreation\n")
        files = precommit.staged_files()
        self.assertNotIn("page.md", precommit.checked_pages("en", files))


if __name__ == "__main__":
    unittest.main()
