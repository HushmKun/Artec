import unittest
from src import argparser

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = argparser.Parser()
        self.parser.setup()

    def test_arg_target(self):
        parsed = self.parser.parse_args(['-o', '/dir/r'])
        self.assertEqual(parsed.target, '/dir/r')

    def test_arg_source(self):
        parsed = self.parser.parse_args(['-o', '/dir/r', '-s', '/dir/s'])
        self.assertEqual(parsed.source, '/dir/s')

