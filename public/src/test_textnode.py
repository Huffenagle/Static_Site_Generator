import unittest

from textnode import (
    TextNode,
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

    def test_is_empty(self):
        node = TextNode("", "", None)
        self.assertIs(node.text, "")
        self.assertIs(node.text_type, "")
        self.assertIs(node.url, None)

if __name__ == "__main__":
    unittest.main()