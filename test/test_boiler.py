import unittest
import os 
import sys 
from artec import boiler
from shutil import rmtree



# Disable Print
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore Print
def enablePrint():
    sys.stdout.close()
    sys.stdout = sys.__stdout__


class BoilerTest(unittest.TestCase):

    def setUp(self):
        blockPrint()
        self.default_boiler = boiler.boiler_builder(target="default", verbose=True)
        self.template_boiler = boiler.boiler_builder(target="template", template='node.js', verbose=True)

    def test_default_structure(self):
        self.default_boiler.build()

    def test_template_structure(self):
        self.template_boiler.build()
        enablePrint()
    
    def __del__(self):
        rmtree("default")
        rmtree("template")