import json

class Converter():
    def convert(self, input):
        data = json.loads(input)

        entries = []

        for item in data:
            node = data[item]
            for address in node["network"]["addresses"]:
                if not "fe80:" in address and not "fda0" in address:
                    entries.append(address + "	" + node["hostname"])

        return "\n".join(reversed(entries)) + "\n"