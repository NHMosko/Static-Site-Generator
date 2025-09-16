from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
        if blocks[i] == "":
            del blocks[i]
    return blocks

def block_to_block_type(md_block):
    if md_block[0] == "#" and " " in md_block[1:7]:
        return BlockType.HEADING
    if md_block[:3] == "```" and md_block[-3:] == "```":
        return BlockType.CODE
    if md_block[0] == ">":
        for i in range(len(md_block)):
            if md_block[i] == "\n":
                if not md_block[i+1] == ">":
                    return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if md_block[:2] == "- ":
        for i in range(len(md_block)):
            if md_block[i] == "\n":
                if not md_block[i+1:i+3] == "- ":
                    return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if md_block[0].isnumeric() and md_block[1:3] == ". ":
        for i in range(len(md_block)):
            if md_block[i] == "\n":
                if not (md_block[i+1].isnumeric() and md_block[i+2:i+4] == ". "):
                    return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def debug():
    print("heading:", block_to_block_type("##### This is a heading ```"))
    print("code:", block_to_block_type("``` ######## This is a heading ```"))
    print("quote:", block_to_block_type(">``` ######## \n>This is a heading ```"))
    print("paragraph:", block_to_block_type(">``` ######## This\n is a heading ```"))
    print("unordered:", block_to_block_type("- ``` #######\n- # This is a heading ```"))
    print("paragraph:", block_to_block_type("1. ``` ##\n ###### This \n3. is a heading ```"))
    print("ordered:", block_to_block_type("1. ``` ##\n2. ###### This \n3. is a heading ```"))

# debug()
