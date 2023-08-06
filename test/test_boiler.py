import unittest
import json
import git
from pathlib import Path
from artec.boiler import boiler_builder
from artec.templates import static_list, templates

VAILD_JSON = Path("./test/resources/structure.json")
INVAILD_JSON = Path("./test/resources/structure.txt")


class TestBoilerBuilder(unittest.TestCase):
    def test_init(self):
        builder = boiler_builder(
            source="structure.json", target="target"
        )
        self.assertEqual(builder.target, "target")
        self.assertIsInstance(builder.structure, list)

    def test_source_temp(self):
        builder = boiler_builder(
            template="python", target="target"
        )
        self.assertEqual(
            builder.structure, templates["python"].format("target")
        )

    def test_source(self):
        with open(VAILD_JSON, "rt", encoding="utf-8") as file_data:
            structure = static_list(json.load(file_data)).format("target")
        builder = boiler_builder(
            source=VAILD_JSON, target="target"
        )
        self.assertEqual(builder.structure, structure)

    def test_build(self):
        builder = boiler_builder(
            source=VAILD_JSON, target="target"
        )
        builder.build()
        self.assertTrue(Path("target/test").is_dir())
        self.assertTrue(Path("target/README.md").is_file())

    def test_git(self): 
        builder = boiler_builder(
            template="python", target="target", git=True
        )
        builder.build()
        self.assertTrue(Path("target/test").is_dir())
        self.assertTrue(Path("target/README.md").is_file())
        self.assertIsInstance(git.Repo("target"), git.Repo)


    def test_exception_handling(self):
        builder = boiler_builder(
            source=INVAILD_JSON, target="target"
        )
        self.assertEqual(
            builder.structure, templates["python"].format("target")
        )

        builder = boiler_builder(
            template="invalid", target="target"
        )
        self.assertEqual(
            builder.structure, templates["python"].format("target")
        )

        builder = boiler_builder(target="target")
        self.assertEqual(
            builder.structure, templates["python"].format("target")
        )



if __name__ == "__main__":
    pass
