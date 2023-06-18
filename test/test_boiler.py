import unittest
import os 
import sys 
from shutil import rmtree
from artec import boiler


# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout.close()
    sys.stdout = sys.__stdout__

class BoilerTest(unittest.TestCase):
    def setUp(self):
        self.boiler = boiler.boiler_builder(target="fake")

    def test_default_structure(self):
        blockPrint()
        self.boiler.build()
        enablePrint()

    def tearDown(self):
        del self.boiler
        rmtree("fake")
