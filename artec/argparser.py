"""
	Parser class is a wrapper for easy access of argparse module v2.1.0
"""
from argparse import (
    ArgumentParser,
    Namespace,
    RawTextHelpFormatter,
    _VersionAction,
)
from .temp import *
import sys


class list_templates(_VersionAction):
    def __call__(self, parser: ArgumentParser, *args, **kwargs) -> None:
        formatter = parser._get_formatter()
        formatter.add_text(
            list_available_templates()
        )
        parser._print_message(formatter.format_help(), sys.stdout)
        parser.exit()


class Parser(ArgumentParser):
    def __init__(self, appVersion):
        self.appVersion = appVersion
        prog = "Artec"
        usage = "artec [OPTIONS] -o [DEST] "
        description = "Artec is a python application that creates a configurable python project template in a given directory."
        epilog = "Examples:\n\tartec -h\n\tartec -o dest\
            \n\tartec -o dest -t python \n\tartec -o dest -s structure.json\
             \n\tartec -o dest -s structure.json -v"
        super().__init__(
            prog,
            usage,
            description,
            epilog,
            formatter_class=RawTextHelpFormatter,
        )

    def setup(self):
        group = self.add_mutually_exclusive_group()
        
        group.add_argument(
            "-s",
            "--source-file",
            dest="source",
            help="Source JSON file containing structure to be created",
            type=str,
            required=False,
        )

        group.add_argument(
            "-t",
            "--template",
            dest="template",
            help="Uses ready-made templates.",
            required=False,
        )


        self.add_argument(
            "-o",
            "--output-directory",
            dest="target",
            help="Target output path where the structure will be created",
            type=str,
        )

        self.add_argument(
            "-i",
            "--interactuve",
            dest="interactive",
            help="Runs artec in interactive mode.",
            action="store_true",
        )

        self.add_argument(
            "-ls",
            "--list-template",
            help="lists all ready-made templates.",
            action=list_templates,
        )

        self.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            help="Runs Artec in verbose mode.",
            action="count",
            default=0,
            required=False,
        )

        self.add_argument(
            "-g",
            "--git-init",
            dest="git",
            help="Creates a git Repo for the project.",
            action="store_true",
            required=False,
        )

        self.add_argument(
            "-V",
            "--version",
            help="Display current version of Artec",
            action="version",
            version=f"{self.prog} {self.appVersion}",
        )


def main_args(appVersion) -> Namespace:
    parser = Parser(appVersion)
    parser.setup()
    args = parser.parse_args()

    if args.interactive:
        print("Running Artec in interactive mode ....")  
    else:
        if not args.target:
            parser.error("The '-o' argument is required when not in interactive mode.")

    return args


if __name__ == "__main__":
    pass
