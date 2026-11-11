"""Automatic heading IDs must not read partial pages or follow symlinks."""
from contextlib import redirect_stdout
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import anchors
import precommit

PAGE = "docs/en/docs/page.md"


class HeadingAutofixGuardTests(unittest.TestCase):
    def assert_skipped(self, unstaged, symlink):
        with patch.object(precommit, "git", return_value=unstaged) as git, \
                patch.object(Path, "is_symlink", return_value=symlink), \
                patch.object(anchors, "load_page", side_effect=AssertionError("must not read page")), \
                patch.object(anchors, "write_page") as write, redirect_stdout(io.StringIO()):
            precommit.add_missing_ids([("M", PAGE)])
        write.assert_not_called()
        self.assertEqual(git.call_count, 1)  # Only list unstaged paths, never git add.
        self.assertEqual(git.call_args.args, ("diff", "--name-only", "-z"))

    def test_partially_staged_page_is_skipped_before_reading(self):
        self.assert_skipped(PAGE + "\0", False)

    def test_symlink_is_skipped_before_reading(self):
        # Mock the filesystem query so Windows does not need symlink privileges.
        self.assert_skipped("", True)

    def test_deleted_and_non_english_pages_are_not_read(self):
        with patch.object(precommit, "git", return_value=""), \
                patch.object(anchors, "load_page", side_effect=AssertionError("must not read page")):
            precommit.add_missing_ids([("D", PAGE), ("M", "docs/de/docs/page.md"),
                                      ("M", "docs/en/docs/image.png")])


if __name__ == "__main__":
    unittest.main()
