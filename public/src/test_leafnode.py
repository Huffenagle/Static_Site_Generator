import unittest

from htmlnode import *

#HTML NODE ARGS: (self, tag=None, value=None, children=None, props=None):

test_props_p = {
    "align": "center",
    "strength": "bold",
}

test_props_a = {
    "href": "https://www.google.com", 
    "target": "_blank",
}

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "This is a paragraph.")
        node2 = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node, node2)
    
    def test_eq_props(self):
        node = LeafNode("p", "This is a paragraph.", test_props_p)
        node2 = LeafNode("p", "This is a paragraph.", test_props_p)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = LeafNode("p", "This is a paragraph.")
        node2 = LeafNode("a", "This is a hyperlink.", test_props_a)
        self.assertNotEqual(node, node2)

    def test_returns_raw_text(self):
        node = LeafNode(None, "Raw Text")
        self.assertEqual(node.to_html(), "Raw Text")

    def test_returns_properly_hyperlink(self):
        node = LeafNode("a", "Click Me!", test_props_a)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click Me!</a>')
    
    def test_returns_properly_paragraph(self):
        node = LeafNode("p", "This is a short paragraph...")
        self.assertEqual(node.to_html(), '<p>This is a short paragraph...</p>')

if __name__ == "__main__":
    unittest.main()