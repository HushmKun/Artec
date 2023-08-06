import sys
import os
from shutil import rmtree
import unittest

sys.path.insert(0, os.path.abspath(".."))


def cleanUp():
    os.remove('log.txt') 
    rmtree("target")

unittest.addModuleCleanup(cleanUp)