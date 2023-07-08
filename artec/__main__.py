from .argparser import main_args
from .boiler import boiler_builder

__app_name__ = "Artec"
__version__ = "0.2.0"
__desc__ = "Creates a configurable python project \
    template in a given directory."


def main():
    args = main_args(__version__)

    builder = boiler_builder(args.source, args.target, args.verbose, args.template)

    builder.build()


if __name__ == "__main__":
    main()
