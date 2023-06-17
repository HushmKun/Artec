import unittest
from shutil import rmtree
from artec import boiler


class BoilerTest(unittest.TestCase):
    def setUp(self):
        self.boiler = boiler.boiler_builder(target="fake")
        self.boiler_2 = boiler.boiler_builder(target="fake",verbose=True)

    def test_default_structure(self):
        self.boiler.build()
        self.boiler_2.build()

    def tearDown(self):
        del self.boiler
        del self.boiler_2
        rmtree("fake")
