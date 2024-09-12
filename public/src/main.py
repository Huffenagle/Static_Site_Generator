from textnode import *
from htmlnode import *

def main():
    
    p_node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")],)
    b_node = ParentNode("p", [LeafNode("i", "italic text"), LeafNode(None, "Normal text"), LeafNode("i", "bold text"), LeafNode(None, "Normal text")],)
    div_node_a = ParentNode("div", [p_node, b_node], {"align": "center"})
    div_node_b = ParentNode("div", [p_node, b_node], {"align": "center"})
    test_node = ParentNode("table", [div_node_a, div_node_b], {"v-align": "middle", "align": "center", "padding": "20px", "margin": "10px"})
    print(test_node.to_html())

main()