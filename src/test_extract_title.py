import unittest

from gencontent import (
    extract_title,
)

class TestTitleExtraction(unittest.TestCase):
    
    def test_ExtractTitle(self):
        test_markdown = "# Heading level 1\nHere is some content after the header including an unordered list:\n* Item\n* Item\n* Item"
        proof = "Heading level 1"
        self.assertEqual(extract_title(test_markdown), proof)
    
    def test_ExtractNoTitle(self):
        test_markdown = "## Heading level 2\nHere is some content after the header including an unordered list:\n* Item\n* Item\n* Item"
        with self.assertRaises(Exception):
            extract_title(test_markdown)