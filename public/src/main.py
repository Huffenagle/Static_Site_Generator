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

from blockline_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
)

with open('src/markdown_test.md') as doc_markdown:
    test_markdown = doc_markdown.read()
    doc_markdown.close()

def main():
    #print(markdown_to_html_node(test_markdown).to_html())
    return

main()