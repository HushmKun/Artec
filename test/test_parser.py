import unittest
from artec.argparser import Parser, Namespace

VAILD_JSON = "test\\resources\\structure.json"
INVAILD_JSON = "test\\resources\\structure.txt"


class TestParser(unittest.TestCase):
    def test_init(self):
        parser = Parser("1.0.0")
        self.assertEqual(parser.prog, "Artec")
        self.assertEqual(parser.appVersion, "1.0.0")

    def test_setup(self):
        parser = Parser("1.0.0")
        parser.setup()
        self.assertIn("-h", parser.__dict__["_option_string_actions"])
        self.assertIn("-s", parser.__dict__["_option_string_actions"])
        self.assertIn("-t", parser.__dict__["_option_string_actions"])
        self.assertIn("-o", parser.__dict__["_option_string_actions"])
        self.assertIn("-ls", parser.__dict__["_option_string_actions"])
        self.assertIn("-v", parser.__dict__["_option_string_actions"])
        self.assertIn("-g", parser.__dict__["_option_string_actions"])
        self.assertIn("-V", parser.__dict__["_option_string_actions"])

    def test_main_args(self):
        parser = Parser("1.0.0")
        parser.setup()
        args = parser.parse_args(["-t", "target", "-o", "fake", "-v"])
        self.assertIsInstance(args, Namespace)
        self.assertIn("target", args.__dict__)
        self.assertIn("verbose", args.__dict__)

    def test_parse_without_args(self):
        parser = Parser("1.0.0")
        with self.assertRaises(SystemExit):
            parser.parse_args()

    def test_parse_with_source(self):
        parser = Parser("1.0.0")
        parser.setup()
        args = parser.parse_args(["-s", VAILD_JSON, "-o", "target"])
        self.assertIn("source", args.__dict__)
        self.assertEqual(args.source, VAILD_JSON)
        self.assertIn("target", args.__dict__)
        self.assertEqual(args.target, "target")

    def test_parse_with_template(self):
        parser = Parser("1.0.0")
        parser.setup()
        args = parser.parse_args(["-t", "python", "-o", "target"])
        self.assertIn("template", args.__dict__)
        self.assertEqual(args.template, "python")
        self.assertIn("target", args.__dict__)
        self.assertEqual(args.target, "target")


if __name__ == "__main__":
    pass
