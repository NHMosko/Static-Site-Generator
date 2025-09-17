import sys
from page_generator import from_dir_to_dir, recursive_page_generator

dir_static = "./static"
dir_public = "./docs"
dir_content = "./content"
template_file = "./template.html"
basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

def main():
    print(basepath)
    from_dir_to_dir(dir_static, dir_public)
    recursive_page_generator(dir_content, template_file, dir_public, basepath)


main()
