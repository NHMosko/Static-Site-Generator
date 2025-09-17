import os
import shutil
from markdown_to_html import markdown_to_html_node

def from_dir_to_dir(source, destination):
    if not os.path.exists(source):
        raise Exception("invalid source path")
    items = os.listdir(source)
    print("Items to be copied:", items)
    if os.path.exists(destination):
        if len(os.listdir(destination)) > 0:
            print("Deleting destination's old files")
            try:
                shutil.rmtree(destination)
            except Exception as e:
                print(e)
    os.mkdir(destination)
    print("Starting copy...")

    print()
    
    for item in items:
        print("Current:", f"{source}/{item}")
        if os.path.isfile(f"{source}/{item}"):
            print(f"copying {item}...")
            shutil.copy(f"{source}/{item}", f"{destination}/{item}")
            print("done!\n")
            continue
        print(f"{item} is a directory, it will be moved to: {destination}/{item}")
        from_dir_to_dir(f"{source}/{item}", f"{destination}/{item}")
              

def extract_title(markdown):
    lines = markdown.splitlines()
    if lines[0].startswith("# "):
        print(f"Generating '{lines[0][2:]}' page\n")
        return lines[0][2:]
    raise Exception("missing title")


def generate_page(from_path, template_path, dest_path):
    if not os.path.exists(from_path):
        raise Exception("invalid source path")
    if not os.path.exists(template_path):
        raise Exception("invalid template path")

    print(f"Generating page from {from_path} to {dest_path}, based on {template_path}")
    
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as t:
        template = t.read()

    document = markdown_to_html_node(markdown)
    html_title = extract_title(markdown)

    titled_doc = template.replace("{{ Title }}", html_title)
    final_doc = titled_doc.replace("{{ Content }}", document.to_html())

    
    with open(f"{dest_path}/index.html", "w") as out:
        out.write(final_doc)
        print("Check!\n")

def recursive_page_generator(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise Exception("invalid source path")
    if not os.path.exists(template_path):
        raise Exception("invalid template path")

    print(f"Crawling on {dir_path_content}...\n")
    if not os.path.exists(dest_dir_path):
        print(f"Making directory {dest_dir_path}")
        os.mkdir(dest_dir_path)

    items = os.listdir(dir_path_content)
    for item in items:
        if os.path.isfile(f"{dir_path_content}/{item}"):
            generate_page(f"{dir_path_content}/{item}", template_path, dest_dir_path)
            continue
        recursive_page_generator(f"{dir_path_content}/{item}", template_path, f"{dest_dir_path}/{item}")

    print("All done!\n")
