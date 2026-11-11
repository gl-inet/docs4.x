"""Regression tests for adding IDs without changing rendered ATX headings."""
from pathlib import Path
import sys
import unittest

import markdown

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import anchors

PAGE = anchors.DOCS_ROOT / "en" / "docs" / "example.md"


def render(text):
    return markdown.markdown(text, extensions=anchors.MD_EXTENSIONS,
                             extension_configs=anchors.MD_EXTENSION_CONFIGS)


class HeadingIdTests(unittest.TestCase):
    def test_adding_id_preserves_rendered_heading_and_anchor(self):
        lines = (
            "## New heading ##\n",
            "## New heading ###\r\n",
            "## New heading\t##\n",
            "## New *heading* ##",
            "## C#\n",
            "## Heading##\n",
            "## Heading \\#\n",
        )
        for raw in lines:
            with self.subTest(raw=raw):
                page = anchors.load_page("en", PAGE, raw)
                heading = page.headings[0]
                anchors.set_heading_id(page, heading, heading.rendered_id)
                self.assertEqual(render(page.text), render(raw))
                self.assertEqual(page.headings[0].explicit_id, heading.rendered_id)
                self.assertTrue(page.changed)
                self.assertEqual(page.text[len(page.text.rstrip("\r\n")):],
                                 raw[len(raw.rstrip("\r\n")):])

    def test_suggested_fix_uses_same_closing_hash_handling(self):
        raw = "## New heading ##\n"
        page = anchors.load_page("en", PAGE, raw)
        fixes = anchors.missing_id_fixes(page)
        self.assertEqual(len(fixes), 1)
        heading, fixed = fixes[0]
        self.assertEqual(fixed, "## New heading {#new-heading}\n")
        self.assertEqual(render(fixed), render(raw))
        self.assertEqual(heading.rendered_id, "new-heading")


if __name__ == "__main__":
    unittest.main()
