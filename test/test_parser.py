import unittest
from artec import argparser


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = argparser.Parser('appVersion')
        self.parser.setup()

    def test_arg_target(self):
        parsed = self.parser.parse_args(["-o", "/dir/r"])
        self.assertEqual(parsed.target, "/dir/r")

    def test_arg_source(self):
        parsed = self.parser.parse_args(["-o", "/dir/r", "-s", "/dir/s"])
        self.assertEqual(parsed.source, "/dir/s")

    def test_arg_verbose(self):
        parsed = self.parser.parse_args(["-o", "/dir/r", "-v"])
        self.assertTrue(parsed.verbose)

    def test_arg_template(self):
        parsed = self.parser.parse_args(["-o", "/dir/r", "-t", "python"])
        self.assertEqual(parsed.template, "python")

    def tearDown(self) -> None:
        del self.parser
