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

from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode,
)

from inline_markdown import (
    split_nodes_at_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)

text_node_text = TextNode("The coolest thing ever.", text_type_text)
text_node_bold = TextNode("This is even cooler!", text_type_bold)
text_node_italic = TextNode("This is just pretentious...", text_type_italic)
text_node_code = TextNode("vertical-align", text_type_code)
text_node_link = TextNode("Click Here!", text_type_link, "https://www.dead.lnk")
text_node_image = TextNode("Spawt the Cat!", text_type_image, "https://www.Spawt.com/Images/Spawt.png")
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

    mixed_node = TextNode("`This` is `code` with a `code block` word and *another* `code block` word...", text_type_text)
    code_node = TextNode("This is a `code` block text node...", text_type_text)
    split_node = split_nodes_at_delimiter([code_node], "`", text_type_code)

    text_with_image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)."
    text_without_image = "This is a text with no image markdown syntax."
    print(extract_markdown_images(text_with_image))
    print(extract_markdown_images(text_without_image))

    text_with_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text_with_link))

main()