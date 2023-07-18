import unittest
import json 
from shutil import rmtree
from pathlib import Path
from artec.boiler import boiler_builder
from artec.templates import static_list, templates

VAILD_JSON = "test\\resources\\structure.json"
INVAILD_JSON = "test\\resources\\structure.txt"

class TestBoilerBuilder(unittest.TestCase):
    def test_init(self):
        builder = boiler_builder(source="structure.json", target="target", verbose=False)
        self.assertEqual(builder.target, "target")
        self.assertEqual(builder.verbose, False)
        self.assertIsInstance(builder.structure, list)

    def test_source_temp(self):
        builder = boiler_builder(template="python", target="target", verbose=False)
        self.assertEqual(builder.structure, templates["python"].format("target"))

    def test_source(self):
        with open(VAILD_JSON, "rt", encoding="utf-8") as file_data:
            structure = static_list(json.load(file_data)).format("target")
        builder = boiler_builder(source=VAILD_JSON, target="target", verbose=False)
        self.assertEqual(builder.structure, structure)

    def test_build(self):
        builder = boiler_builder(source=VAILD_JSON, target="target", verbose=False)
        builder.build()
        self.assertTrue(Path("target/test").is_dir())
        self.assertTrue(Path("target/README.md").is_file())
        rmtree('target')


    def test_exception_handling(self):
        builder = boiler_builder(source=INVAILD_JSON, target="target", verbose=False)
        self.assertEqual(builder.structure, templates["python"].format("target"))

        builder = boiler_builder(template="invalid", target="target", verbose=False)
        self.assertEqual(builder.structure, templates["python"].format("target"))
        
        builder = boiler_builder(target="target", verbose=False)
        self.assertEqual(builder.structure, templates["python"].format("target"))
        

if __name__ == "__main__":
    pass
