"""PR content checks must use committed text and preserve Git filenames."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pr_check as pc


class ContentSnapshotTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        root = patch.object(pc, "REPO_ROOT", self.root)
        root.start()
        self.addCleanup(root.stop)
        self.git("init", "-q")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "core.autocrlf", "false")
        self.git("config", "core.hooksPath", ".disabled-hooks")
        self.git("config", "commit.gpgsign", "false")

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, stderr=subprocess.STDOUT)

    def put(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(text.encode("utf-8"))

    def commit(self, message):
        self.git("add", ".")
        self.git("commit", "-qm", message)

    def test_unicode_rename_added_lines_and_dirty_worktree(self):
        old, new = "docs/en/docs/old.md", "docs/en/docs/中文 page.md"
        added = "docs/en/docs/日本語 space.md"
        self.put(old, "# Old {#old}\n" + "unchanged\n" * 20)
        self.commit("base")
        self.git("branch", "base")
        (self.root / old).rename(self.root / new)
        self.put(new, "# New {#new}\n" + "unchanged\n" * 20 + "added\n")
        self.put(added, "new prose\n")
        self.commit("change")
        self.put(new, "uncommitted text\n")
        self.assertIn((old, new), pc.changed_paths("base"))
        self.assertEqual(pc.added_lines("base"), {new: {1, 22}, added: {1}})
        self.assertEqual(pc.page_lines(new)[0], "# New {#new}")
        findings = pc.check_heading_ids("base")
        self.assertEqual([(f.path, f.check) for f in findings], [(new, "heading-id")])
        self.assertIn("old", findings[0].message)
        # Removing the working file does not remove committed content from checks.
        (self.root / new).unlink()
        self.assertEqual(pc.page_lines(new)[0], "# New {#new}")

    def test_rename_and_recreated_old_path_do_not_mix_hunks(self):
        old, new = "docs/en/docs/old.md", "docs/en/docs/new.md"
        text = "# Page {#page}\n" + "unchanged\n" * 30
        self.put(old, text)
        self.commit("base")
        self.git("branch", "base")
        (self.root / old).rename(self.root / new)
        self.put(new, text + "added\n")
        self.put(old, "different\n" * 4)
        self.commit("rename plus replacement")
        # Isolate the mapping: Git rename heuristics vary when old also exists.
        with patch.object(pc, "changed_paths", return_value=[(old, new), (old, old)]):
            self.assertEqual(pc.added_lines("base")[new], {32})

    def test_nul_records_preserve_tabs_quotes_and_newlines(self):
        name = 'docs/en/docs/中文\t"quote"\npage.md'
        with patch.object(pc, "git", return_value=f"R100\0old.md\0{name}\0M\0other.md\0") as git:
            self.assertEqual(pc.changed_paths("base"), [("old.md", name), ("other.md", "other.md")])
            self.assertIn("-z", git.call_args.args[0:])

    def test_new_pages_and_non_markdown_have_no_removed_heading_ids(self):
        self.put("docs/en/docs/existing.md", "# Existing {#existing}\n")
        self.commit("base")
        self.git("branch", "base")
        self.put("docs/en/docs/new.md", "# New {#new}\n")
        self.put("docs/en/docs/asset.txt", "not Markdown\n")
        self.commit("added files")
        self.assertEqual(pc.check_heading_ids("base"), [])


if __name__ == "__main__":
    unittest.main()
