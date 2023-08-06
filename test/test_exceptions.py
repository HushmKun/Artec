import unittest
from artec.exceptions import (
    NotJsonFile,
    NoSource,
    NotValidJson,
    InValidTemplate,
    GitError,
)


class TestExceptions(unittest.TestCase):
    def test_not_json_file(self):
        exception = NotJsonFile()
        self.assertEqual(exception.errno, 101)
        self.assertEqual(
            str(exception), "> Provided Source isn't valid JSON file"
        )

    def test_no_source(self):
        exception = NoSource()
        self.assertEqual(exception.errno, 102)
        self.assertEqual(str(exception), "> No Source Provided")

    def test_not_valid_json(self):
        exception = NotValidJson()
        self.assertEqual(exception.errno, 103)
        self.assertEqual(
            str(exception), "> Provided Json file format is incorrect"
        )

    def test_invalid_template(self):
        exception = InValidTemplate()
        self.assertEqual(exception.errno, 104)
        self.assertEqual(
            str(exception), "> Provided Template argument is invalid"
        )

    def test_git_error(self):
        exception = GitError()
        self.assertEqual(exception.errno, 105)
        self.assertEqual(str(exception), "> Git has encountered a problem")


if __name__ == "__main__":
    pass
