import unittest

from textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)
        self.assertEqual(node.text, node2.text)
        self.assertEqual(node.text_type, node2.text_type)
        self.assertEqual(node.url, node2.url)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a also text node", "italic", "http://test.net")
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node.text, node2.text)
        self.assertNotEqual(node.text_type, node2.text_type)
        self.assertNotEqual(node.url, node2.url)
    
    def test_no_url(self):
        node = TextNode("This is a text node", "bold")
        self.assertIsNone(node.url)
    
    def test_eq_url(self):
        node = TextNode("This is a also text node", "italic", "http://test.net")
        node2 = TextNode("This is a also text node", "italic", "http://test.net")
        self.assertIs(node.url, node2.url)

    def test_is_empty(self):
        node = TextNode("", "", None)
        self.assertIs(node.text, "")
        self.assertIs(node.text_type, "")
        self.assertIs(node.url, None)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", text_type_text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold", text_type_bold)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_italic(self):
        node = TextNode("This is italic", text_type_italic)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic")

    def test_code(self):
        node = TextNode("This is a code block", text_type_code)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code block")

    def test_image(self):
        node = TextNode("This is an image!", text_type_image, "https://www.boot.dev/img.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "https://www.boot.dev/img.png", "alt": "This is an image!"})
    
    def test_link(self):
        node = TextNode("This is a hyperlink!", text_type_link, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a hyperlink!")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    def test_bunk(self):
        node = TextNode("Whoopsie Doodle!", "bunks", "www.bunk.net")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()