import unittest
from markdown_to_blocks import (
        markdown_to_blocks,
        block_to_block_type,
        BlockType
        )

class TestMarkdownToBlocks(unittest.TestCase):
    def test_function(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_types(self):
        test_cases = [
                block_to_block_type("##### This is a heading ```"),
                block_to_block_type("``` ######## This is a heading ```"),
                block_to_block_type(">``` ######## \n>This is a heading ```"),
                block_to_block_type(">``` ######## This\n is a heading ```"),
                block_to_block_type("- ``` #######\n- # This is a heading ```"),
                block_to_block_type("1. ``` ##\n ###### This \n3. is a heading ```"),
                block_to_block_type("1. ``` ##\n2. ###### This \n3. is a heading ```")
                ]
        self.assertEqual(test_cases, [
           BlockType.HEADING,
           BlockType.CODE,
           BlockType.QUOTE,
           BlockType.PARAGRAPH,
           BlockType.UNORDERED_LIST,
           BlockType.PARAGRAPH,
           BlockType.ORDERED_LIST,
            ])

if __name__ == "__main__":
    unittest.main()
