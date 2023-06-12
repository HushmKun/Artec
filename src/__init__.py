from argparser import main_args
from pyboiler import boiler_builder
from os.path import exists

VERSION = '0.1.0'
DESCRIPTION = "Creates a configurable python project template in a given directory."


def main():
	args = main_args()

	exist = exists(args.target)
	should_override = input("> Should Override ? (Y/n) : ").lower()


	if exist and ( should_override == 'y' )  :
		builder = boiler_builder(args.source, args.target, override=True)
	else:
		builder = boiler_builder(args.source, args.target, override=False)

	builder.build()


if __name__ == '__main__' : 
	main()