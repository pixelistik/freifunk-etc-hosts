import converter
import argparse
import urllib

def main():
	c = converter.Converter()

	args = _parseArguments()

	input_file = urllib.urlopen(args.i)
	print c.convert(input_file)

def _parseArguments():
		"""
		Get the given command line arguments
		"""
		argumentParser = argparse.ArgumentParser(description="Convert an Alfred JSON file into an /etc/hosts file.")
		argumentParser.add_argument(
			'-i',
			metavar='input URL',
			default="http://ffmap.freifunk-rheinland.net/alfred_merged.json",
			help='input URL'
		)
		"""argumentParser.add_argument(
			'-o',
			metavar='output file',
			default="-",
			help='output file'
		)"""
		return argumentParser.parse_args()

if __name__ == '__main__':
	main()