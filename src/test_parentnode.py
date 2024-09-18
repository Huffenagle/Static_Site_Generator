import unittest

from htmlnode import (
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

test_child_a = ParentNode("A", None, test_props_a)
test_child_b = ParentNode("P", test_child_a, test_props_p)
test_children = (test_child_a, test_child_b)

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("P", test_child_a, None)
        node2 = ParentNode("P", test_child_a, None)
        self.assertEqual(node, node2)
    
    def test_eq_complex(self):
        node = ParentNode("P", test_children, test_props_p)
        node2 = ParentNode("P", test_children, test_props_p)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = ParentNode("P", None, test_props_p)
        node2 = ParentNode("A", None, test_props_a)
        self.assertNotEqual(node, node2)
    
    def test_no_children(self):
        node = ParentNode("P", None, test_props_p)
        self.assertIsNone(node.children)

    def test_has_children(self):
        node = ParentNode("P", test_children, test_props_p)
        self.assertIsNotNone(node.children)

    def test_has_props(self):
        node = ParentNode("P", None, test_props_p)
        self.assertIsNotNone(node.props)

    def test_no_children(self):
        node = ParentNode("P", None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_tag(self):
        node = ParentNode(None, test_children, None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_nested_thrice(self):
        p_node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")],)
        div_node = ParentNode("div", [p_node], {"align": "center"})
        test_node = ParentNode("table", [div_node], {"v-align": "middle", "align": "center", "padding": "20px", "margin": "10px"})
        html = '<table v-align="middle" align="center" padding="20px" margin="10px"><div align="center"><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div></table>'
        self.assertEqual(test_node.to_html(), html)

    def test_nested_twice(self):
        p_node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")],)
        div_node = ParentNode("div", [p_node], {"align": "center"})
        html = '<div align="center"><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>'
        self.assertEqual(div_node.to_html(), html)
    
    def test_nested_once(self):
        p_node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")],)
        html = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(p_node.to_html(), html)

    def test_nested_simple(self):
        p_node = ParentNode("p", [LeafNode(None, "Normal text")],)
        html = '<p>Normal text</p>'
        self.assertEqual(p_node.to_html(), html)

    def test_nested_complex(self):
        p_node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")],)
        b_node = ParentNode("p", [LeafNode("i", "italic text"), LeafNode(None, "Normal text"), LeafNode("i", "bold text"), LeafNode(None, "Normal text")],)
        div_node_a = ParentNode("div", [p_node, b_node], {"align": "center"})
        div_node_b = ParentNode("div", [p_node, b_node], {"align": "center"})
        test_node = ParentNode("table", [div_node_a, div_node_b], {"v-align": "middle", "align": "center", "padding": "20px", "margin": "10px"})
        html = (
            f'<table v-align="middle" align="center" padding="20px" margin="10px">'
            f'<div align="center"><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
            f'<p><i>italic text</i>Normal text<i>bold text</i>Normal text</p></div>'
            f'<div align="center"><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
            f'<p><i>italic text</i>Normal text<i>bold text</i>Normal text</p></div></table>'
        )
        self.assertEqual(test_node.to_html(), html)



if __name__ == "__main__":
    unittest.main()