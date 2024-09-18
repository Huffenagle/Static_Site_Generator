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
        self.assertListEqual(extract_markdown_links(text), [])

class TestExtractMarkdownAndLinks(unittest.TestCase):

    def test_link_then_image(self):
        text_with_link_image = "This is text with a link [to boot dev](https://www.boot.dev) and an image ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)."
        test_list_image = [('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        test_list_link = [('to boot dev', 'https://www.boot.dev')]
        self.assertListEqual(extract_markdown_images(text_with_link_image), test_list_image)
        self.assertListEqual(extract_markdown_links(text_with_link_image), test_list_link)

class TestSplitNodesImage(unittest.TestCase):

    def test_single_node_single_image(self):
        test_node = TextNode("![Alt Text goes here...](https://www.test.com/img.png)", text_type_text)
        proof_node = TextNode("Alt Text goes here...", text_type_image, "https://www.test.com/img.png")
        self.assertListEqual(split_nodes_images([test_node]), [proof_node])

    def test_single_node_double_image(self):
        test_node = TextNode("![Image 1](https://www.test.com/img1.png)![Image 2](https://www.test.com/img2.png)", text_type_text)
        proof_node1 = TextNode("Image 1", text_type_image, "https://www.test.com/img1.png")
        proof_node2 = TextNode("Image 2", text_type_image, "https://www.test.com/img2.png")
        proof_node_list = [proof_node1, proof_node2]
        self.assertListEqual(split_nodes_images([test_node]), proof_node_list)

    def test_single_node_double_image(self):
        test_node = TextNode("![Image 1](https://www.test.com/img1.png) with text between ![Image 2](https://www.test.com/img2.png)", text_type_text)
        proof_node1 = TextNode("Image 1", text_type_image, "https://www.test.com/img1.png")
        proof_node2 = TextNode(" with text between ", text_type_text)
        proof_node3 = TextNode("Image 2", text_type_image, "https://www.test.com/img2.png")
        proof_node_list = [proof_node1, proof_node2, proof_node3]
        self.assertListEqual(split_nodes_images([test_node]), proof_node_list)

    def test_double_node_single_image(self):
        test_node_1 = TextNode("![Image 1](https://www.test.com/img1.png) with text after Image 1.", text_type_text)
        test_node_2 = TextNode("![Image 2](https://www.test.com/img2.png) with text after Image 2.", text_type_text)
        proof_node1 = TextNode("Image 1", text_type_image, "https://www.test.com/img1.png")
        proof_node2 = TextNode(" with text after Image 1.", text_type_text)
        proof_node3 = TextNode("Image 2", text_type_image, "https://www.test.com/img2.png")
        proof_node4 = TextNode(" with text after Image 2.", text_type_text)
        test_node_list = [test_node_1, test_node_2]
        test_split_nodes = split_nodes_images(test_node_list)
        proof_node_list = [proof_node1, proof_node2, proof_node3, proof_node4]
        self.assertListEqual(test_split_nodes, proof_node_list)
    
    def test_double_node_double_image(self):
        test_node_1 = TextNode("![Image 1](https://www.test.com/img1.png) with text after Image 1. ![Image 2](https://www.test.com/img2.png) with text after Image 2.", text_type_text)
        test_node_2 = TextNode("![Image 3](https://www.test.com/img3.png) with text after Image 3. ![Image 4](https://www.test.com/img4.png) with text after Image 4.", text_type_text)
        proof_node_list = [
            TextNode("Image 1", text_type_image, "https://www.test.com/img1.png"),
            TextNode(" with text after Image 1. ", text_type_text),
            TextNode("Image 2", text_type_image, "https://www.test.com/img2.png"),
            TextNode(" with text after Image 2.", text_type_text),
            TextNode("Image 3", text_type_image, "https://www.test.com/img3.png"),
            TextNode(" with text after Image 3. ", text_type_text),
            TextNode("Image 4", text_type_image, "https://www.test.com/img4.png"),
            TextNode(" with text after Image 4.", text_type_text)
            ]
        test_node_list = [test_node_1, test_node_2]
        test_split_nodes = split_nodes_images(test_node_list)
        self.assertListEqual(test_split_nodes, proof_node_list)

    def test_image_with_link(self):
        test_node = TextNode("![Image 1](https://www.test.com/img1.png) with a [link](https://www.bunk.com) after Image 1.", text_type_text)
        proof_node_list = [
            TextNode("Image 1", text_type_image, "https://www.test.com/img1.png"),
            TextNode(" with a [link](https://www.bunk.com) after Image 1.", text_type_text),
            ]
        test_split_nodes = split_nodes_images([test_node])
        self.assertListEqual(test_split_nodes, proof_node_list)

    def test_passes_text_node(self):
        test_node = TextNode("This is just a text block.", text_type_text)
        proof_node_list = [TextNode("This is just a text block.", text_type_text)]
        test_split_nodes = split_nodes_images([test_node])
        self.assertListEqual(test_split_nodes, proof_node_list)

    def test_passes_link_node(self):
        test_node = TextNode("This is only a [link](https://www.bunk.com) block.", text_type_text)
        test_split_nodes = split_nodes_images([test_node])
        self.assertListEqual(test_split_nodes, [test_node])

    def test_passes_other_nodes(self):
        test_node_list = [
            TextNode("This is a **bold** node.", text_type_bold),
            TextNode("This is an *italic* node.", text_type_italic),
            TextNode("This is a `code` node.", text_type_code),
            ]   
        test_split_nodes = split_nodes_images(test_node_list)
        self.assertListEqual(test_split_nodes, test_node_list)

class TestSplitNodesLinks(unittest.TestCase):

    def test_single_node_single_link(self):
        test_node = TextNode("[Click Me!](https://www.test.com)", text_type_text)
        proof_node = TextNode("Click Me!", text_type_link, "https://www.test.com")
        self.assertListEqual(split_nodes_links([test_node]), [proof_node])

    def test_single_node_double_link(self):
        test_node = TextNode("[Click Me!](https://www.test.com), or [Click Me!!](https://www.test.com/test.html)", text_type_text)
        proof_node_list = [
            TextNode("Click Me!", text_type_link, "https://www.test.com"),
            TextNode(", or ", text_type_text),
            TextNode("Click Me!!", text_type_link, "https://www.test.com/test.html")
            ]
        self.assertListEqual(split_nodes_links([test_node]), proof_node_list)
    
    def test_double_node_double_link(self):
        test_node_list = [
            TextNode("You should [Click Me!](https://www.test.com), or [Click Me!!](https://www.test.com/test.html).", text_type_text),
            TextNode("[Don't Click Me...](https://www.bunk.com), or [Woo!](https://www.dotcom.com)!", text_type_text)
            ]
        proof_node_list = [
            TextNode("You should ", text_type_text),
            TextNode("Click Me!", text_type_link, "https://www.test.com"),
            TextNode(", or ", text_type_text),
            TextNode("Click Me!!", text_type_link, "https://www.test.com/test.html"),
            TextNode(".", text_type_text),
            TextNode("Don't Click Me...", text_type_link, "https://www.bunk.com"),
            TextNode(", or ", text_type_text),
            TextNode("Woo!", text_type_link, "https://www.dotcom.com"),
            TextNode("!", text_type_text),
            ]
        self.assertListEqual(split_nodes_links(test_node_list), proof_node_list)

    def test_passes_other_nodes(self):
        test_node_list = [
            TextNode("This is an ![Image](https://www.bunk.net/image.png) text node.", text_type_text),
            TextNode("Image Node", text_type_image, "https://www.test.com/img2.png"),
            TextNode("Link Node Alt Text", text_type_link, "https://www.Link.org"),
            TextNode("This is a **bold** node.", text_type_bold),
            TextNode("This is an *italic* node.", text_type_italic),
            TextNode("This is a `code` node.", text_type_code),
            ]   
        test_split_nodes = split_nodes_links(test_node_list)
        self.assertListEqual(test_split_nodes, test_node_list)

class TestPlainTextToTextNodes(unittest.TestCase):

    def test_error_cases(self):
        text = "This is not *bold** text."
        with self.assertRaises(ValueError):
            text_to_textnodes(text)
        
        text = "This is not *italic` text."
        with self.assertRaises(ValueError):
            text_to_textnodes(text)

    def test_text(self):
        text = "This is plain text."
        test_nodes = text_to_textnodes(text)
        proof_nodes = [TextNode("This is plain text.", text_type_text)]
        self.assertListEqual(test_nodes, proof_nodes)

    def test_bold(self):
        text = "This is **bold** text."
        test_nodes = text_to_textnodes(text)
        proof_nodes = [
            TextNode("This is ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" text.", text_type_text),
            ]
        self.assertListEqual(test_nodes, proof_nodes)

    def test_bunch_of_bold(self):
        text = "This is **bold** and **bold** and **bold** text."
        test_nodes = text_to_textnodes(text)
        proof_nodes = [
            TextNode("This is ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" and ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" and ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" text.", text_type_text),
            ]
        self.assertListEqual(test_nodes, proof_nodes)

    def test_italic(self):
        text = "This is *italic* text."
        test_nodes = text_to_textnodes(text)
        proof_nodes = [
            TextNode("This is ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" text.", text_type_text),
            ]
        self.assertListEqual(test_nodes, proof_nodes)

    def test_bunch_of_italic(self):
        text = "This is *italic* and *italic* and *italic* text."
        test_nodes = text_to_textnodes(text)
        proof_nodes = [
            TextNode("This is ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" and ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" and ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" text.", text_type_text),
            ]
        self.assertListEqual(test_nodes, proof_nodes)

    def test_code(self):
        text = "This is `code` text."
        test_nodes = text_to_textnodes(text)
        proof_nodes = [
            TextNode("This is ", text_type_text),
            TextNode("code", text_type_code),
            TextNode(" text.", text_type_text),
            ]
        self.assertListEqual(test_nodes, proof_nodes)

    def test_bunch_of_code(self):
        text = "This is `code` and `code` and `code` text."
        test_nodes = text_to_textnodes(text)
        proof_nodes = [
            TextNode("This is ", text_type_text),
            TextNode("code", text_type_code),
            TextNode(" and ", text_type_text),
            TextNode("code", text_type_code),
            TextNode(" and ", text_type_text),
            TextNode("code", text_type_code),
            TextNode(" text.", text_type_text),
            ]
        self.assertListEqual(test_nodes, proof_nodes)

    def test_three_delims(self):
        text = "This is **bold** and *italic* and `code` text."
        test_nodes = text_to_textnodes(text)
        proof_nodes = [
            TextNode("This is ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" and ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" and ", text_type_text),
            TextNode("code", text_type_code),
            TextNode(" text.", text_type_text),
            ]
        self.assertListEqual(test_nodes, proof_nodes)

    def test_image(self):
        text = "This is ![image](https://www.test.net/img.png) text."
        test_nodes = text_to_textnodes(text)
        proof_nodes = [
            TextNode("This is ", text_type_text),
            TextNode("image", text_type_image, "https://www.test.net/img.png"),
            TextNode(" text.", text_type_text),
            ]
        self.assertListEqual(test_nodes, proof_nodes)

    def test_link(self):
        text = "This is [a Link!](https://www.test.net) with text."
        test_nodes = text_to_textnodes(text)
        proof_nodes = [
            TextNode("This is ", text_type_text),
            TextNode("a Link!", text_type_link, "https://www.test.net"),
            TextNode(" with text.", text_type_text),
            ]
        self.assertListEqual(test_nodes, proof_nodes)
    
    def test_image_link(self):
        text = "This is ![image](https://www.test.net/img.png) text.  This is [a Link!](https://www.test.net) with text."
        test_nodes = text_to_textnodes(text)
        proof_nodes = [
            TextNode("This is ", text_type_text),
            TextNode("image", text_type_image, "https://www.test.net/img.png"),
            TextNode(" text.  This is ", text_type_text),
            TextNode("a Link!", text_type_link, "https://www.test.net"),
            TextNode(" with text.", text_type_text),
            ]
        self.assertListEqual(test_nodes, proof_nodes)

    def test_complex(self):
        text = "Text ![image](https://www.test.net/img.png) text **bold** text *italic* text `code` text [a Link!](https://www.test.net) text."
        test_nodes = text_to_textnodes(text)
        proof_nodes = [
            TextNode("Text ", text_type_text),
            TextNode("image", text_type_image, "https://www.test.net/img.png"),
            TextNode(" text ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" text ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" text ", text_type_text),
            TextNode("code", text_type_code),
            TextNode(" text ", text_type_text),
            TextNode("a Link!", text_type_link, "https://www.test.net"),
            TextNode(" text.", text_type_text),
            ]
        self.assertListEqual(test_nodes, proof_nodes)

if __name__ == "__main__":
    unittest.main()