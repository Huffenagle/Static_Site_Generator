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
)

def main():
    test_markdown = (
        f"# This is a heading.\n\n"
        f"## This is also a heading.\n\n"
        f"### This is an even better heading.\n\n"
        f"This is a paragraph of text. It has some `code words` in it.\n\n"
        f"This is another paragraph of text. It has some **bold** and *italic* words in it.\n It even has a dropped line to make sure it appends correctly.\n\n"
        f"* This is the first list item in a list block.\n"
        f"* This is a list item.\n"
        f"* Another list item.\n\n"
        f"1. This is the first list item in an ordered list block.\n"
        f"2. This is the second item.\n"
        f"3. Item #3."
        )    
    markdown_blocks = markdown_to_blocks(test_markdown)

    test_block = block_to_block_type("## heading")
    print(test_block)
    test_block = block_to_block_type("```This is a Code block with a\nnew line of code and another\nnew line of code!```")
    print(test_block)
    test_block = block_to_block_type(">Quote 1\n>Quote2\n>Quote 3")
    print(test_block)
    test_block = block_to_block_type("- Item\n- Item\n- Item\n- Item")
    print(test_block)
    test_block = block_to_block_type("1. Item\n2. Item\n3. Item\n4. Item\n5. Item\n6. Item\n7. Item\n8. Item\n9. Item\n10. Item\n11. Item\n12. Item")
    print(test_block)
    test_block = block_to_block_type("This is just a line of text.")
    print(test_block)

    ordered_list_string = ""
    for i in range(1, 1001):
        ordered_list_string += f"{i}. Item {i}\n"
    print(block_to_block_type(ordered_list_string.rstrip("\n")))

main()