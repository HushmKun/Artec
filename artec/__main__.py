from . import argparser as parser
from . import boiler
from . import logging, console_handler
from .temp import * 

__app_name__ = "Artec"
__version__ = "0.3.1"
__desc__ = "Creates a configurable python project \
    template in a given directory."

ERROR_LOGING = {
    0: logging.FATAL,
    1: logging.ERROR,
    2: logging.WARN,
    3: logging.INFO,
}


def main():
    args = parser.main_args(__version__)

    console_handler.setLevel(ERROR_LOGING[args.verbose])
    builder = boiler.boiler_builder(
        args.source, args.target, args.template, args.git
    )

    builder.build()


if __name__ == "__main__":
    main()
    
