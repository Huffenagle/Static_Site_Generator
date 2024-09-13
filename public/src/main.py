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
    split_nodes_images,
    split_nodes_links,
    text_to_textnodes
)

def main():

    #new_nodes = text_to_textnodes("This ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) is **text** with an *italic* word *and* a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev).")
    #new_nodes = text_to_textnodes("Basic and simple text.")
    new_nodes = text_to_textnodes("Basic and **bold** text.")
    new_nodes = text_to_textnodes("Basic and *italic* text.")
    for node in new_nodes:
        print(node)

main()