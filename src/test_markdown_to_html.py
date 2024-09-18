import unittest

from blockline_markdown import (
    markdown_to_html_node,
)

class TestMarkdownToHTMLNodes(unittest.TestCase):
    
    def test_MarkdownToHTML(self):
        with open('src/testing/markdown_test.md') as doc_markdown:
            test_markdown = doc_markdown.read()
            doc_markdown.close()
        with open('src/testing/proof_html_1.txt') as doc_proof:
            proof_html = doc_proof.read()
            doc_proof.close()
        self.assertEqual(markdown_to_html_node(test_markdown).to_html(), proof_html)