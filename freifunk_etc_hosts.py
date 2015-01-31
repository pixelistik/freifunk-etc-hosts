import argparse
import urllib
import json

class Converter():
    def convert(self, input_file):
        data = json.load(input_file)

        return self._parse_json(data)

    def _parse_json(self, data):
        entries = []

        for key, node in data.iteritems():
            for address in node["network"]["addresses"]:
                if not "fe80:" in address and not "fda0" in address:
                    entries.append((node["hostname"], address))

        return "\n".join(map(lambda entry: entry[1] + "\t" + entry[0], sorted(entries))) + "\n"

def main():
	c = Converter()

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