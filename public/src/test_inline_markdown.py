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
)

class TestSplitNode(unittest.TestCase):
    def test_code_node(self):
        node = TextNode("This is a `code` block text node...", text_type_text)
        split_node = split_nodes_at_delimiter([node], "`", text_type_code)
        test_node_0 = TextNode("This is a ", text_type_text, None)
        test_node_1 = TextNode("code", text_type_code, None)
        test_node_2 = TextNode(" block text node...", text_type_text, None)
        test_nodes = [test_node_0, test_node_1, test_node_2]
        self.assertListEqual(split_node, test_nodes)

    def test_doublecode_node(self):
        node = TextNode("This is a `code` block text node with another `code` block text node...", text_type_text)
        split_node = split_nodes_at_delimiter([node], "`", text_type_code)
        test_node_0 = TextNode("This is a ", text_type_text, None)
        test_node_1 = TextNode("code", text_type_code, None)
        test_node_2 = TextNode(" block text node with another ", text_type_text, None)
        test_node_3 = TextNode("code", text_type_code, None)
        test_node_4 = TextNode(" block text node...", text_type_text, None)
        test_nodes = [test_node_0, test_node_1, test_node_2, test_node_3, test_node_4]
        self.assertListEqual(split_node, test_nodes)

    def test_codefirst_node(self):
        node = TextNode("`Code Node` at the front of the node...", text_type_text)
        split_node = split_nodes_at_delimiter([node], "`", text_type_code)
        test_node_0 = TextNode("Code Node", text_type_code, None)
        test_node_1 = TextNode(" at the front of the node...", text_type_text, None)
        test_nodes = [test_node_0, test_node_1]
        self.assertListEqual(split_node, test_nodes)
    
    def test_bold_node(self):
        node = TextNode("This is a **bold** block text node...", text_type_text)
        split_node = split_nodes_at_delimiter([node], "**", text_type_bold)
        test_node_0 = TextNode("This is a ", text_type_text, None)
        test_node_1 = TextNode("bold", text_type_bold, None)
        test_node_2 = TextNode(" block text node...", text_type_text, None)
        test_nodes = [test_node_0, test_node_1, test_node_2]
        self.assertListEqual(split_node, test_nodes)

    def test_doublebold_node(self):
        node = TextNode("This is a **bold** block text node with another **bold** block text node...", text_type_text)
        split_node = split_nodes_at_delimiter([node], "**", text_type_bold)
        test_node_0 = TextNode("This is a ", text_type_text, None)
        test_node_1 = TextNode("bold", text_type_bold, None)
        test_node_2 = TextNode(" block text node with another ", text_type_text, None)
        test_node_3 = TextNode("bold", text_type_bold, None)
        test_node_4 = TextNode(" block text node...", text_type_text, None)
        test_nodes = [test_node_0, test_node_1, test_node_2, test_node_3, test_node_4]
        self.assertListEqual(split_node, test_nodes)

    def test_boldfirst_node(self):
        node = TextNode("**Bold Node** at the front of the node...", text_type_text)
        split_node = split_nodes_at_delimiter([node], "**", text_type_bold)
        test_node_0 = TextNode("Bold Node", text_type_bold, None)
        test_node_1 = TextNode(" at the front of the node...", text_type_text, None)
        test_nodes = [test_node_0, test_node_1]
        self.assertListEqual(split_node, test_nodes)
    
    def test_italic_node(self):
        node = TextNode("This is an *italic* block text node...", text_type_text)
        split_node = split_nodes_at_delimiter([node], "*", text_type_italic)
        test_node_0 = TextNode("This is an ", text_type_text, None)
        test_node_1 = TextNode("italic", text_type_italic, None)
        test_node_2 = TextNode(" block text node...", text_type_text, None)
        test_nodes = [test_node_0, test_node_1, test_node_2]
        self.assertListEqual(split_node, test_nodes)

    def test_doubleitalic_node(self):
        node = TextNode("This is an *italic* block text node with another *italic* block text node...", text_type_text)
        split_node = split_nodes_at_delimiter([node], "*", text_type_italic)
        test_node_0 = TextNode("This is an ", text_type_text, None)
        test_node_1 = TextNode("italic", text_type_italic, None)
        test_node_2 = TextNode(" block text node with another ", text_type_text, None)
        test_node_3 = TextNode("italic", text_type_italic, None)
        test_node_4 = TextNode(" block text node...", text_type_text, None)
        test_nodes = [test_node_0, test_node_1, test_node_2, test_node_3, test_node_4]
        self.assertListEqual(split_node, test_nodes)

    def test_italicfirst_node(self):
        node = TextNode("*Italic Node* at the front of the node...", text_type_text)
        split_node = split_nodes_at_delimiter([node], "*", text_type_italic)
        test_node_0 = TextNode("Italic Node", text_type_italic, None)
        test_node_1 = TextNode(" at the front of the node...", text_type_text, None)
        test_nodes = [test_node_0, test_node_1]
        self.assertListEqual(split_node, test_nodes)

    def test_bolditalic_node(self):
        node = TextNode("This is an *italic* text node with an additional **bold** text node...", text_type_text)
        split_node = split_nodes_at_delimiter([node], "**", text_type_bold)
        split_node = split_nodes_at_delimiter(split_node, "*", text_type_italic)
        test_node_0 = TextNode("This is an ", text_type_text, None)
        test_node_1 = TextNode("italic", text_type_italic, None)
        test_node_2 = TextNode(" text node with an additional ", text_type_text, None)
        test_node_3 = TextNode("bold", text_type_bold, None)
        test_node_4 = TextNode(" text node...", text_type_text, None)
        test_nodes = [test_node_0, test_node_1, test_node_2, test_node_3, test_node_4]
        self.assertListEqual(split_node, test_nodes)

    def test_bolditaliccode_node(self):
        node = TextNode("This is an *italic* text node with an additional **bold** text node and a `code` text node...", text_type_text)
        split_node = split_nodes_at_delimiter([node], "**", text_type_bold)
        split_node = split_nodes_at_delimiter(split_node, "*", text_type_italic)
        split_node = split_nodes_at_delimiter(split_node, "`", text_type_code)
        test_node_0 = TextNode("This is an ", text_type_text, None)
        test_node_1 = TextNode("italic", text_type_italic, None)
        test_node_2 = TextNode(" text node with an additional ", text_type_text, None)
        test_node_3 = TextNode("bold", text_type_bold, None)
        test_node_4 = TextNode(" text node and a ", text_type_text, None)
        test_node_5 = TextNode("code", text_type_code, None)
        test_node_6 = TextNode(" text node...", text_type_text, None)
        test_nodes = [test_node_0, test_node_1, test_node_2, test_node_3, test_node_4, test_node_5, test_node_6]
        self.assertListEqual(split_node, test_nodes)

    def test_valid_node(self):
        node = TextNode("This is a **broken* block text node...", text_type_text)
        with self.assertRaises(ValueError):
            split_node = split_nodes_at_delimiter([node], "**", text_type_bold)

class TestExtractMarkdownImages(unittest.TestCase):

    def test_single_image_extraction(self):    
        text_with_image = "![rick roll](https://i.imgur.com/aKaOqIh.gif)."
        test_list = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif')]
        self.assertListEqual(extract_markdown_images(text_with_image), test_list)
    
    def test_double_image_extraction(self):    
        text_with_image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)."
        test_list = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertListEqual(extract_markdown_images(text_with_image), test_list)
    
    def test_no_image_extraction(self):
        text = "This is plain text."
        test_list = []
        self.assertListEqual(extract_markdown_images(text), test_list)

class TestExtractMarkdownLinks(unittest.TestCase):

    def test_single_link_extraction(self):    
        text_with_link = "This is text with a link [to boot dev](https://www.boot.dev)."
        test_list = [('to boot dev', 'https://www.boot.dev')]
        self.assertListEqual(extract_markdown_links(text_with_link), test_list)
    
    def test_double_link_extraction(self):    
        text_with_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        test_list = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertListEqual(extract_markdown_links(text_with_link), test_list)
    
    def test_no_link_extraction(self):
        text = "This is plain text."
        test_list = []
        self.assertListEqual(extract_markdown_links(text), test_list)

class TestExtractMarkdownAndLinks(unittest.TestCase):

    def test_link_then_image(self):
        text_with_link_image = "This is text with a link [to boot dev](https://www.boot.dev) and an image ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)."
        test_list_image = [('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        test_list_link = [('to boot dev', 'https://www.boot.dev')]
        self.assertListEqual(extract_markdown_images(text_with_link_image), test_list_image)
        self.assertListEqual(extract_markdown_links(text_with_link_image), test_list_link)
if __name__ == "__main__":
    unittest.main()