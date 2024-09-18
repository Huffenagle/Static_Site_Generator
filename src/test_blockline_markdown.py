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
    text_to_textnodes,
)

from blockline_markdown import (
    markdown_to_blocks,
    block_to_block_type,
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
        proof_blocks = [
                        '#This is a heading.', 
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
            f"```This is a code block of text that will run for multiple\nlines. The purpose of this is to see how it comes out in\nblock form.```\n\n"
            f"*This is the first list item in a list block.\n"
            f"*This is a list item.\n"
            f"*Another list item.\n\n"
            f"1. This is the first list item in an ordered list block.\n"
            f"2. This is the second item.\n"
            f"3. Item #3."
            )
        proof_blocks = [
                        '#This is a heading.',
                        '##This is also a heading.',
                        '###This is an even better heading.',
                        'This is a paragraph of text. It has some `code words` in it.',
                        'This is another paragraph of text. It has some **bold** and *italic* words in it.\nIt even has a dropped line to make sure it appends correctly.',
                        '```This is a code block of text that will run for multiple\nlines. The purpose of this is to see how it comes out in\nblock form.```',
                        '*This is the first list item in a list block.\n*This is a list item.\n*Another list item.',
                        '1. This is the first list item in an ordered list block.\n2. This is the second item.\n3. Item #3.'
                        ]
        self.assertListEqual(markdown_to_blocks(test_markdown), proof_blocks)

class TestBlockToBlockType(unittest.TestCase):
    
    def test_return_paragraph(self):
        self.assertEqual(block_to_block_type("This is just a paragraph"), "paragraph")
        self.assertEqual(block_to_block_type("This is just a paragraph \nwith a dropped line."), "paragraph")
    
    def test_return_heading_levels(self):
        self.assertEqual(block_to_block_type("# Heading1"), "heading")
        self.assertEqual(block_to_block_type("## Heading2"), "heading")
        self.assertEqual(block_to_block_type("### Heading3"), "heading")
        self.assertEqual(block_to_block_type("#### Heading4"), "heading")
        self.assertEqual(block_to_block_type("##### Heading5"), "heading")
        self.assertEqual(block_to_block_type("###### Heading6"), "heading")

    def test_return_not_heading(self):
        self.assertNotEqual(block_to_block_type("####### Heading7"), "heading")
        self.assertNotEqual(block_to_block_type("#Heading1"), "heading")
        self.assertNotEqual(block_to_block_type("##Heading2"), "heading")
        self.assertNotEqual(block_to_block_type("###Heading3"), "heading")
        self.assertNotEqual(block_to_block_type("####Heading4"), "heading")
        self.assertNotEqual(block_to_block_type("#####Heading5"), "heading")
        self.assertNotEqual(block_to_block_type("######Heading6"), "heading")
        self.assertNotEqual(block_to_block_type("#######Heading7"), "heading")
        self.assertNotEqual(block_to_block_type("########Heading8"), "heading")

    def test_return_code(self):
        self.assertEqual(block_to_block_type("```\n<HTML></HTML>\n```"), "code")
        self.assertEqual(block_to_block_type("```\n<HTML>\n<p>Paragraph Text</p>\n</HTML>\n```"), "code")
        self.assertEqual(block_to_block_type("```\n<HTML>\n<title>Code Text</title>\n\n<p>Paragraph Text</p>\n\n</HTML>\n```"), "code")

    def test_return_not_code(self):
        self.assertNotEqual(block_to_block_type("```<HTML></HTML>```"), "code")
        self.assertNotEqual(block_to_block_type("-`-`-`\n<HTML></HTML>\n`-`-`-"), "code")
        self.assertNotEqual(block_to_block_type("``<HTML></HTML>``"), "code")
        self.assertNotEqual(block_to_block_type("`<HTML></HTML>`"), "code")
        self.assertNotEqual(block_to_block_type("<HTML></HTML>"), "code")
        self.assertNotEqual(block_to_block_type("```<HTML></HTML>"), "code")
        self.assertNotEqual(block_to_block_type("<HTML></HTML>```"), "code")

    def test_return_quote(self):
        quote_list_block = ""
        for i in range(0, 10):
            quote_list_block += f"> Quote\n"
            quote_list_block = quote_list_block.rstrip("\n")
        self.assertEqual(block_to_block_type(quote_list_block), "quote")

    def test_return_quote_alt(self):
        quote_list_block = ""
        for i in range(0, 10):
            quote_list_block += f">Quote\n"
            quote_list_block = quote_list_block.rstrip("\n")
        self.assertEqual(block_to_block_type(quote_list_block), "quote")

    def test_return_unordered_list_asterisk(self):
        unordered_list_block = ""
        for i in range(0, 10):
            unordered_list_block += f"* Item\n"
            unordered_list_block = unordered_list_block.rstrip("\n")
        self.assertEqual(block_to_block_type(unordered_list_block), "unordered_list")

    def test_return_unordered_list_dash(self):
        unordered_list_block = ""
        for i in range(0, 10):
            unordered_list_block += f"- Item\n"
            unordered_list_block = unordered_list_block.rstrip("\n")
        self.assertEqual(block_to_block_type(unordered_list_block), "unordered_list")

    def test_return_not_unordered_list_asterisk(self):
        unordered_list_block = ""
        for i in range(0, 10):
            unordered_list_block += f"*Item\n"
            unordered_list_block = unordered_list_block.rstrip("\n")
        self.assertNotEqual(block_to_block_type(unordered_list_block), "unordered_list")

    def test_return_not_unordered_list_dash(self):
        unordered_list_block = ""
        for i in range(0, 10):
            unordered_list_block += f"-Item\n"
            unordered_list_block = unordered_list_block.rstrip("\n")
        self.assertNotEqual(block_to_block_type(unordered_list_block), "unordered_list")
    
    def test_return_ordered_list(self):
        ordered_list_block = ""
        for i in range(1, 10):
            ordered_list_block += f"{i}. Item {i}\n"
            ordered_list_block = ordered_list_block.rstrip("\n")
        self.assertEqual(block_to_block_type(ordered_list_block), "ordered_list")
        self.assertEqual(block_to_block_type("1. Item\n2. Item\n3. Item\n4. Item\n5. Item"), "ordered_list")

    def test_not_ordered_lists(self):
        self.assertNotEqual(block_to_block_type("1.Item\n2.Item\n3.Item\n4.Item\n5.Item"), "ordered_list")
        self.assertNotEqual(block_to_block_type(" 1. Item\n2. Item\n3. Item\n4. Item\n5. Item"), "ordered_list")
        self.assertNotEqual(block_to_block_type("2. Item\n4. Item\n9. Item\n11. Item\n56. Item\n7. Item\n32. Item\n32. Item"), "ordered_list")
        self.assertNotEqual(block_to_block_type(". Item\n. Item\n. Item\n. Item\n. Item"), "ordered_list")
        self.assertNotEqual(block_to_block_type("1 Item\n2 Item\n3 Item\n4 Item\n5 Item"), "ordered_list")
        self.assertNotEqual(block_to_block_type("1) Item\n2) Item\n3) Item\n4) Item\n5) Item"), "ordered_list")
        self.assertNotEqual(block_to_block_type("1)Item\n2)Item\n3)Item\n4)Item\n5)Item"), "ordered_list")
        self.assertNotEqual(block_to_block_type("1-Item\n2-Item\n3-Item\n4-Item\n5-Item"), "ordered_list")
        self.assertNotEqual(block_to_block_type("1. Item\n2) Item\n3- Item\n4 Item\n5. Item"), "ordered_list")
        self.assertNotEqual(block_to_block_type("1. Item 2. Item \n3. Item 4. Item \n5. Item"), "ordered_list")