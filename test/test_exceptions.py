import unittest
from artec.exceptions import NotJsonFile, NoSource, NotValidJson, InValidTemplate


class TestExceptions(unittest.TestCase):
    def test_not_json_file(self):
        exception = NotJsonFile(False)
        self.assertEqual(exception.errno, 101)
        self.assertEqual(str(exception), "> Provided Source isn't valid JSON file")

    def test_no_source(self):
        exception = NoSource(False)
        self.assertEqual(exception.errno, 102)
        self.assertEqual(str(exception), "> No Source Provided")

    def test_not_valid_json(self):
        exception = NotValidJson(False)
        self.assertEqual(exception.errno, 103)
        self.assertEqual(str(exception), "> Provided Json file format is incorrect")

    def test_invalid_template(self):
        exception = InValidTemplate(False)
        self.assertEqual(exception.errno, 104)
        self.assertEqual(str(exception), "> Provided Template argument is invalid")


if __name__ == "__main__":
    pass