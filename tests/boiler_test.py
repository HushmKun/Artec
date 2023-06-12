import unittest
from shutil import rmtree
from src.pyboiler import boiler_builder 

class BoilerTest(unittest.TestCase):
    def setUp(self):
        self.boiler = boiler_builder(target='fake', override=True)
        self.boiler_json = boiler_builder(source="res\simple.json", target='fake', override=True)
        
    def test_default_structure(self):
        self.boiler.build()
        
    def test_given_structure(self):
        self.boiler_json.build()

    def tearDown(self):
        del self.boiler_json
        del self.boiler
        rmtree('fake')


