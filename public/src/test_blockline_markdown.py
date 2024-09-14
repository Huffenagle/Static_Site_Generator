import unittest

from textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link,
    text_type_text,
)
from inline_markdown import (
    split_nodes_at_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_images,
    split_nodes_links,
    text_to_textnodes
)

from blockline_markdown import (
    markdown_to_blocks
)

class TestMarkdownToBlocks(unittest.TestCase):
    def test_MarkdownToBlocks(self):
        test_markdown = (
            f"#This is a heading.\n\n"
            f"This is a paragraph of text. It has some **bold** and *italic* words in it.\n\n"
            f"*This is the first list item in a list block.\n"
            f"*This is a list item.\n"
            f"*Another list item.\n"
        )
        proof_blocks = ['#This is a heading.', 
                        'This is a paragraph of text. It has some **bold** and *italic* words in it.', 
                        '*This is the first list item in a list block.\n*This is a list item.\n*Another list item.'
                        ]
        self.assertListEqual(markdown_to_blocks(test_markdown), proof_blocks)

    def test_MarkdownToBlocks_HandlesWhiteSpaces(self):
        test_markdown = (
            f"   #This is a heading.  \n\n   "
            f"      This is a paragraph of text. It has some **bold** and *italic* words in it.  \n\n"
            f"            *This is the first list item in a list block.\n     "
            f"  *This is a list item.\n"
            f"*Another list item.\n"
        )
        proof_blocks = ['#This is a heading.', 
                        'This is a paragraph of text. It has some **bold** and *italic* words in it.', 
                        '*This is the first list item in a list block.\n*This is a list item.\n*Another list item.'
                        ]
        self.assertListEqual(markdown_to_blocks(test_markdown), proof_blocks)

    def test_MarkdownToBlocks_HandlesWonkiness(self):
        test_markdown = (
            f"   #This is a heading.  \n\n   \n\n\n"
            f"   \n\n   This is a paragraph of text. It has some **bold** and *italic* words in it.  \n\n"
            f"    \n        *This is the first list item in a list block.\n     "
            f"  *This is a list item.\n                               "
            f"*Another list item.\n"
        )
        proof_blocks = ['#This is a heading.', 
                        'This is a paragraph of text. It has some **bold** and *italic* words in it.', 
                        '*This is the first list item in a list block.\n*This is a list item.\n*Another list item.'
                        ]
        self.assertListEqual(markdown_to_blocks(test_markdown), proof_blocks)

    def test_MarkdownToBlocks_OneLine(self):
        test_markdown = ("#This is a heading.\n\n This is a paragraph of text. It has some **bold** and *italic* words in it.\n\n *This is the first list item in a list block.\n *This is a list item.\n *Another list item.")
        proof_blocks = ['#This is a heading.', 
                        'This is a paragraph of text. It has some **bold** and *italic* words in it.', 
                        '*This is the first list item in a list block.\n*This is a list item.\n*Another list item.'
                        ]
        self.assertListEqual(markdown_to_blocks(test_markdown), proof_blocks)

    def test_MarkdownToBlocks_BigMarkdown(self):
        test_markdown = (
            f"#This is a heading.\n\n"
            f"##This is also a heading.\n\n"
            f"###This is an even better heading.\n\n"
            f"This is a paragraph of text. It has some `code words` in it.\n\n"
            f"This is another paragraph of text. It has some **bold** and *italic* words in it.\n It even has a dropped line to make sure it appends correctly.\n\n"
            f"*This is the first list item in a list block.\n"
            f"*This is a list item.\n"
            f"*Another list item.\n\n"
            f"1. This is the first list item in an ordered list block.\n"
            f"2. This is the second item.\n"
            f"3. Item #3."
            )
        proof_blocks = ['#This is a heading.',
                        '##This is also a heading.',
                        '###This is an even better heading.',
                        'This is a paragraph of text. It has some `code words` in it.',
                        'This is another paragraph of text. It has some **bold** and *italic* words in it.\nIt even has a dropped line to make sure it appends correctly.',
                        '*This is the first list item in a list block.\n*This is a list item.\n*Another list item.',
                        '1. This is the first list item in an ordered list block.\n2. This is the second item.\n3. Item #3.']
        self.assertListEqual(markdown_to_blocks(test_markdown), proof_blocks)