import json

class Converter():
    def convert(self, input_file):
        data = json.load(input_file)

        return self._parse_json(data)

    def _parse_json(self, data):
        entries = []

        for item in data:
            node = data[item]
            for address in node["network"]["addresses"]:
                if not "fe80:" in address and not "fda0" in address:
                    entries.append(address + "	" + node["hostname"])

        return "\n".join(reversed(entries)) + "\n"