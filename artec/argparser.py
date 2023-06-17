"""
	Parser class is a wrapper for easy access of argparse module
"""
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter


class Parser(ArgumentParser):
    def __init__(self):
        prog = "Artec"
        usage = "artec [OPTIONS] -o [DEST] "
        description = "Artec is a simple python 3 script to create a project template in a given directory."
        epilog = """Examples:\n\tartec -o dest\n\tartec -o dest -s structure.json"""
        super().__init__(
            prog, usage, description, epilog, formatter_class=RawTextHelpFormatter
        )

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

        # ! Not Implemented Yet.
        self.add_argument(
            "-i",
            "--interactive",
            dest="tui",
            help="Runs Artec in interactive mode.",
            action="store_true",
            required=False,
        )

        self.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            help="Runs Artec in verbose mode.",
            action="store_true",
            required=False,
        )

def main_args() -> Namespace:
    parser = Parser()
    parser.setup()
    return parser.parse_args()


if __name__ == "__main__":
    pass
