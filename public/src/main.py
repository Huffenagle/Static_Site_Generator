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
    split_nodes_image,
    split_nodes_links
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

    text_with_image = "![Image 1](https://i.imgur.com/img1.gif)![Image 2](https://i.imgur.com/img2.gif) text between images ![Image 3](https://i.imgur.com/img3.gif) more text between images ![Image 4](https://i.imgur.com/img4.gif) text after images.![Image 5](https://i.imgur.com/img5.gif)"
    text_with_image2 = "![Image 1](https://i.imgur.com/img1.gif)"
    text_with_image3 = "![Image 2](https://i.imgur.com/img2.gif)![Image 3](https://i.imgur.com/img3.gif)"
    node_with_image = TextNode(text_with_image, text_type_text)
    node_with_image2 = TextNode(text_with_image2, text_type_text)
    node_with_image3 = TextNode(text_with_image3, text_type_text)
    new_nodes = split_nodes_image([text_node_text, node_with_image, text_node_link, node_with_image2, node_with_image3])
    for node in new_nodes:
        print(node)

    test_node = TextNode("![Image 1](https://www.test.com/img1.png) with text between ![Image 2](https://www.test.com/img2.png)", text_type_text)
    test_node_list = split_nodes_image([test_node])
    print(test_node_list)

    #text_with_link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    #print(extract_markdown_links(text_with_link))

main()