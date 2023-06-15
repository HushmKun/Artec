from argparser import main_args
from boiler import boiler_builder

def main():
	args = main_args()

	builder = boiler_builder(args.source, args.target, args.tui)
	
	builder.build()


if __name__ == '__main__' : 
	main()