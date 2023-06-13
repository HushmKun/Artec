"""
	Parser class is a wrapper for easy access of argparse module
"""
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter 


class Parser(ArgumentParser):
	def __init__(self):
		prog = "PyBoiler"
		usage = "pyboiler [OPTIONS] -o [DEST] "
		description = "PyBoiler is a simple python 3 script to create \
		a project template in a given directory."
		epilog = """Examples : \n\tpython src/__init__.py -o dest\n\tpython src/__init__.py -o dest -s res/simple.json"""
		super().__init__(prog, usage, description, epilog,formatter_class=RawTextHelpFormatter)

	def setup(self):
		self.add_argument(
			"-o",
			"--output-directory",
			dest="target",
			help="Target output path where the structure will be created",
			type=str,
			required=True,
		)

		self.add_argument(
			"-s",
			"--source-file",
			dest="source",
			help="Source JSON file containing structure to be created",
			type=str,
			required=False,
		)

		

def main_args() -> Namespace :
	parser = Parser()
	parser.setup()
	return parser.parse_args()

if __name__ == '__main__': 
	pass