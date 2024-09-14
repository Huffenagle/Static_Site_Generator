from textnode import (
    TextNode,
    text_type_text, text_type_bold, text_type_code, text_type_image, text_type_italic, text_type_link,
    text_node_to_html_node
)



def markdown_to_blocks(markdown):
    split_list = markdown.strip().split("\n\n")
    blocks = []
    final_blocks = []
    for block in split_list:
        if block != "":
            split_blocks = block.split("\n")
            string = ""
            for split_block in split_blocks:
                string += f"{split_block.strip()}\n"
            blocks.append(string.rstrip("\n").lstrip("\n"))
    for block in blocks:
        if block != "":
            final_blocks.append(block)
    return final_blocks