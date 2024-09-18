import unittest

from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode,
)

#HTML NODE ARGS: (self, tag=None, value=None, children=None, props=None):

test_props_p = {
    "align": "center",
    "strength": "bold",
}

test_props_a = {
    "href": "https://www.google.com", 
    "target": "_blank",
}

test_childa = HTMLNode("P", "This is a short paragraph.")
test_childb = HTMLNode("A", "This is a hyperlink.", None, test_props_a)
test_children = (test_childa, test_childb)

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("P", "This is a paragraph.", None, test_props_p)
        node2 = HTMLNode("P", "This is a paragraph.", None, test_props_p)
        self.assertEqual(node, node2)
    
    def test_eq_complex(self):
        node = HTMLNode("P", "This is a paragraph.", test_children, test_props_p)
        node2 = HTMLNode("P", "This is a paragraph.", test_children, test_props_p)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("P", "This is a paragraph", None, test_props_p)
        node2 = HTMLNode("A", "This is a hyperlink", None, test_props_a)
        self.assertNotEqual(node, node2)
    
    def test_no_children(self):
        node = HTMLNode("P", "This is a paragraph", None, test_props_p)
        self.assertIsNone(node.children)

    def test_has_children(self):
        node = HTMLNode("P", "This is a paragraph.", test_children, test_props_p)
        self.assertIsNotNone(node.children)

    def test_has_props(self):
        node = HTMLNode("P", "This is a paragraph.", None, test_props_p)
        self.assertIsNotNone(node.props)

    def test_no_props(self):
        node = HTMLNode("P", "This is a paragraph.")
        self.assertIsNone(node.props)

    def test_is_empty(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

if __name__ == "__main__":
    unittest.main()