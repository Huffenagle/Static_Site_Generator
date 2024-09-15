import re
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