from .argparser import main_args
from .boiler import boiler_builder

__app_name__ = 'artec'
__version__ = '0.1.0'
__desc__ = "Creates a configurable python project template in a given directory."

def main():
	args = main_args()

	builder = boiler_builder(args.source, args.target)
	
	builder.build()


if __name__ == '__main__' : 
	main()

