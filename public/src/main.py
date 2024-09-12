from textnode import *
from htmlnode import *

text_node_text = TextNode("The coolest thing ever.", "text")
text_node_bold = TextNode("This is even cooler!", "bold")
text_node_italic = TextNode("This is just pretentious...", "italic")
text_node_code = TextNode("vertical-align", "code")
text_node_link = TextNode("Click Here!", "link", "https://www.dead.lnk")
text_node_image = TextNode("Spawt the Cat!", "image", "https://www.Spawt.com/Images/Spawt.png")
#text_node_bunk = TextNode("Whoopsie Doodle!", "bunk", "www.bunk.net")
text_node_list = [text_node_text, text_node_bold, text_node_italic, text_node_code, text_node_link, text_node_image]

def main():
    
    ''' 
    p_node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text")],)
    b_node = ParentNode("p", [LeafNode("i", "italic text"), LeafNode(None, "Normal text"), LeafNode("i", "bold text"), LeafNode(None, "Normal text")],)
    div_node_a = ParentNode("div", [p_node, b_node], {"align": "center"})
    div_node_b = ParentNode("div", [p_node, b_node], {"align": "center"})
    test_node = ParentNode("table", [div_node_a, div_node_b], {"v-align": "middle", "align": "center", "padding": "20px", "margin": "10px"})
    print(test_node.to_html())
    '''

    for node in text_node_list:
        html_node = node.text_node_to_html_node()
        print(html_node.to_html())

main()