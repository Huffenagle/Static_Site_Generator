import os
from blockline_markdown import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, 'r')
    markdown = from_file.read()
    from_file.close()
    template_file = open(template_path, 'r')
    template = template_file.read()
    template_file.close()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace(" {{ Title }} ", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    print(dest_dir_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, 'w')
    to_file.write(template)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# ") == True:
            return line[2:]
        raise Exception("There is no valid header from which to extract a title...")
        