from htmlnode import LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        children.append(make_html_from(block, block_type))
    return ParentNode("div", children, None)

def make_html_from(md_block, block_type):
    type_tag = "p"
    children = []
    leaf_nodes = None
    match block_type:
        case BlockType.HEADING:
            if md_block.startswith("# "):
                md_block = md_block[2:]
                type_tag = 'h1'
            elif md_block.startswith("## "):
                md_block = md_block[3:]
                type_tag = 'h2'
            elif md_block.startswith("### "):
                md_block = md_block[4:]
                type_tag = 'h3'
            elif md_block.startswith("#### "):
                md_block = md_block[5:]
                type_tag = 'h4'
            elif md_block.startswith("##### "):
                md_block = md_block[6:]
                type_tag = 'h5'
            elif md_block.startswith("###### "):
                md_block = md_block[7:]
                type_tag = 'h6'
        case BlockType.CODE: # ! special case
            code_text = md_block[3:-3]
            if code_text.startswith("\n"):
                code_text = code_text[1:]
            return ParentNode(
                "pre",
                [ParentNode("code", [text_node_to_html_node(TextNode(code_text, TextType.TEXT))])]
            )
        case BlockType.QUOTE:
            new_block = []
            for line in md_block.split("\n"):
               line = line.removeprefix("> ") if line.startswith("> ") else line.removeprefix(">")
               new_block.append(line)
            md_block = "\n".join(new_block)
            type_tag = 'blockquote'
        case BlockType.ORDERED_LIST:
            leaf_nodes = []
            for line in md_block.split("\n"):
                text = line[3:]
                tns = text_to_textnodes(text)
                li_children = [text_node_to_html_node(tn) for tn in tns]
                leaf_nodes.append(ParentNode("li", li_children))
            type_tag = 'ol'
        case BlockType.UNORDERED_LIST:
            leaf_nodes = []
            for line in md_block.split("\n"):
                text = line[2:]
                tns = text_to_textnodes(text)
                li_children = [text_node_to_html_node(tn) for tn in tns]
                leaf_nodes.append(ParentNode("li", li_children))
            type_tag = 'ul'
    
    if leaf_nodes:
        return ParentNode(type_tag, leaf_nodes)
    else:
        text = " ".join(md_block.splitlines())
        tns = text_to_textnodes(text) 
        children = [text_node_to_html_node(tn) for tn in tns]
        return ParentNode(type_tag, children)


# print(markdown_to_html_node("just a paragraph\n\n### this is **heading**\n\n> this is a _quote_\n>still a quote\n\n1. this is\n2. a list\n\n- what\n- about\n- unordered\n\n```def code():\n   print(here **is** code)```"))

