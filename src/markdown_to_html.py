from htmlnode import HTMLNode, ParentNode
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from inline_markdown import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        children.append(make_html_from(block, block_type))
    return HTMLNode('<html>', None, children, None)

def make_html_from(md_block, block_type):
    type_tag = "<p>"
    match block_type:
        case BlockType.HEADING:
            if md_block.startswith("# "):
                md_block = md_block[2:]
                type_tag = '<h1>'
            elif md_block.startswith("## "):
                md_block = md_block[3:]
                type_tag = '<h2>'
            elif md_block.startswith("### "):
                md_block = md_block[4:]
                type_tag = '<h3>'
            elif md_block.startswith("#### "):
                md_block = md_block[5:]
                type_tag = '<h4>'
            elif md_block.startswith("##### "):
                md_block = md_block[6:]
                type_tag = '<h5>'
            elif md_block.startswith("###### "):
                md_block = md_block[7:]
                type_tag = '<h6>'
        case BlockType.CODE:
            md_block = md_block[3:-3]
            type_tag = '<code>'
        case BlockType.QUOTE:
            new_block = []
            for line in md_block.split("\n"):
                new_block.append(line[1:])
            md_block = "\n".join(new_block)
            type_tag = '<blockquote>'
            ## JUST FINISHED MAKING THIS ONE WORK
        case BlockType.ORDERED_LIST:
            for line in md_block.split("\n"):
                line = "<li>" + line[2:]
            type_tag = '<ol>'
        case BlockType.UNORDERED_LIST:
            for line in md_block.split("\n"):
                line = "<li>" + line[3:]
            type_tag = '<ul>'

    return ParentNode(type_tag, text_to_textnodes(md_block))


print(markdown_to_html_node("### this is **heading**\n\n> this is _quote_\n>still a quote\n\n1. this is\n2. a list\n\n- what\n- about\n- unordered"))
