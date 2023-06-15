import unittest
from shutil import rmtree
from artec import boiler 

class BoilerTest(unittest.TestCase):
    def setUp(self):
        self.boiler = boiler.boiler_builder(target='fake')
        
    def test_default_structure(self):
        self.boiler.build()

    def tearDown(self):
        del self.boiler
        rmtree('fake')


