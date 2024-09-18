import re

from htmlnode import (
    HTMLNode,
    ParentNode,
    LeafNode,
)

from inline_markdown import (
    text_to_textnodes,
)

from textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link
)

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"



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

def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    children = []
    block_tag = "div"
    for block in markdown_blocks:
        if block_to_block_type(block) == block_type_paragraph:
            children.append(paragraph_block_to_html_node(block))
        if block_to_block_type(block) == block_type_heading:
            children.append(heading_block_to_html_node(block))
        if block_to_block_type(block) == block_type_quote:
            children.append(quote_block_to_html_node(block))
        if block_to_block_type(block) == block_type_code:
            children.append(code_block_to_html_node(block))
        if block_to_block_type(block) == block_type_ulist:
            children.append(ulist_block_to_html_node(block))
        if block_to_block_type(block) == block_type_olist:
            children.append(olist_block_to_html_node(block))
    html_node = ParentNode(block_tag, children)
    return html_node
    
def paragraph_block_to_html_node(block):
    lines = block.split("\n")
    block_tag = "p"
    block_text = " ".join(lines)
    children = text_to_children(block_text)
    html_node = ParentNode(block_tag, children)
    return html_node

def heading_block_to_html_node(block):
    lines = block.split("\n")
    for line in lines:
        if line.startswith("# "):
            block_tag = "h1"
            block_text = line.replace('# ', '')
        if line.startswith("## "):
            block_tag = "h2"
            block_text = line.replace('## ', '')
        if line.startswith("### "):
            block_tag = "h3"
            block_text = line.replace('### ', '')
        if line.startswith("#### "):
            block_tag = "h4"
            block_text = line.replace('#### ', '')
        if line.startswith("##### "):
            block_tag = "h5"
            block_text = line.replace('##### ', '')
        if line.startswith("###### "):
            block_tag = "h6"
            block_text = line.replace('###### ', '')
    children = text_to_children(block_text)
    html_node = ParentNode(block_tag, children)
    return html_node

def quote_block_to_html_node(block):
    block_tag = "blockquote"
    block_text = block.replace(">", "")
    children = text_to_children(block_text)
    html_node = ParentNode(block_tag, children)
    return html_node

def code_block_to_html_node(block):
    lines = block.split("\n")
    block_tag = "pre"
    block_text = ""
    for i in range(1, len(lines) - 1):
        block_text += f"{lines[i]}\n"
    block_text = block_text.rstrip("\n")
    text_node = TextNode(block_text, text_type_code)
    code_node = text_node_to_html_node(text_node)
    html_node = ParentNode(block_tag, [code_node])
    return html_node

def ulist_block_to_html_node(block):
    lines = block.split("\n")
    block_tag = "ul"
    list_item_tag = "li"
    ul_child_nodes = []
    for line in lines:
        block_text = line.replace("* ","").replace("- ","")
        li_child_node = text_to_children(block_text)
        li_node = ParentNode(list_item_tag, li_child_node)
        ul_child_nodes.append(li_node)
    html_node = ParentNode(block_tag, ul_child_nodes)
    return html_node

def olist_block_to_html_node(block):
    lines = block.split("\n")
    block_tag = "ol"
    list_item_tag = "li"
    ul_child_nodes = []
    for i in range(0, len(lines)):
        block_text = lines[i].replace(f"{i+1}. ","")
        li_child_node = text_to_children(block_text)
        li_node = ParentNode(list_item_tag, li_child_node)
        ul_child_nodes.append(li_node)
    html_node = ParentNode(block_tag, ul_child_nodes)
    return html_node

def text_to_children(text):
    children = []
    child_nodes = text_to_textnodes(text)
    for child in child_nodes:
        children.append(text_node_to_html_node(child))
    return children

'''
def block_to_block_type_HUFF(markdown_block):
    heading_exp = r"^(#{1,6}\s{1}\w)"
    code_exp = r"(?s)(^`{3})(.*?)(`{3}$)"
    quote_exp = r"(^\>{1}\w|\>{1}\s(.*?))"
    unordered_list_exp = r"^(\-{1}\s(.*?))|^(\*{1}\s(.*?))"
    ordered_list_exp = r"^([0-9]+\.\s(.*?))"
    if re.match(heading_exp, markdown_block):
        return "heading"
    if re.match(code_exp, markdown_block):
        return "code"
    split_blocks = markdown_block.split("\n")
    if all(re.match(quote_exp, block) for block in split_blocks):
        return "quote"
    if all(re.match(unordered_list_exp, block) for block in split_blocks):
        return "unordered_list"
    if all(re.match(ordered_list_exp, block) for block in split_blocks):
        iteration = 0
        numbers = []
        for block in split_blocks:
            iteration += 1
            number = re.findall(r"^([0-9]+)", block)
            numbers.append((int(number[0]), iteration))
        if all(pair[0] == pair[1] for pair in numbers):
            return("ordered_list")
    return "paragraph"
'''