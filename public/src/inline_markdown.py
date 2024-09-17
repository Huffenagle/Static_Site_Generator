import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_image,
    text_type_italic,
    text_type_link
)

def split_nodes_at_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) %2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed...")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if (i % 2) == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        alt_url_pairs = extract_markdown_images(node.text)
        if len(alt_url_pairs) == 0:
            new_nodes.extend([node])
        else:
            split_nodes = []
            original_text = node.text
            image_alt, image_link = alt_url_pairs[0]
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)
            for i in range(len(alt_url_pairs)):
                image_alt, image_link = alt_url_pairs[i]
                if i == 0:
                    sections = original_text.split(f"![{image_alt}]({image_link})", 1)
                else:
                    sections = sections[1].split(f"![{image_alt}]({image_link})", 1)
                if sections[0] != "":
                    split_nodes.append(TextNode(sections[0], text_type_text))
                split_nodes.append(TextNode(image_alt, text_type_image, image_link))
            if sections[1] != "":
                split_nodes.append(TextNode(sections[1], text_type_text))
            new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        txt_url_pairs = extract_markdown_links(node.text)
        if len(txt_url_pairs) == 0:
            new_nodes.extend([node])
        else:
            split_nodes = []
            original_text = node.text
            link_txt, link_url = txt_url_pairs[0]
            sections = original_text.split(f"[{link_txt}]({link_url})", 1)
            for i in range(len(txt_url_pairs)):
                if len(sections) != 2:
                    raise ValueError("Invalid markdown, link section not closed")
                link_txt, link_url = txt_url_pairs[i]
                if i == 0:
                    sections = original_text.split(f"[{link_txt}]({link_url})", 1)
                else:
                    sections = sections[1].split(f"[{link_txt}]({link_url})", 1)
                if sections[0] != "":
                    split_nodes.append(TextNode(sections[0], text_type_text))
                split_nodes.append(TextNode(link_txt, text_type_link, link_url))
            if sections[1] != "":
                split_nodes.append(TextNode(sections[1], text_type_text))
            new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    delim_dict = {"**":text_type_bold, "*":text_type_italic, "`":text_type_code}
    for delim in delim_dict:
        nodes = split_nodes_at_delimiter(nodes, delim, delim_dict[delim])
    nodes = split_nodes_images(split_nodes_links(nodes))
    return nodes