from page_generator import from_dir_to_dir, recursive_page_generator

def main():
    from_dir_to_dir("static","public")
    recursive_page_generator("content", "template.html", "public")


main()
