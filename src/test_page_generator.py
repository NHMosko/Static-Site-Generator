import unittest
from page_generator import extract_title

class TestPageGenerator(unittest.TestCase):
    def test_page_gen(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
