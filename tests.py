import unittest
import freifunk_etc_hosts
import logging
import os.path
import json

class TestConverter(unittest.TestCase):

    def setUp(self):
        self.converter = freifunk_etc_hosts.Converter()

    def test_parse_json(self):
        simple_node = """
    {
        "c4:6e:1f:a2:97:ae": {
            "network": {
              "addresses": [
                "fe80:0:0:0:c66e:1fff:fea2:97ae",
                "fda0:747e:ab29:cafe:c66e:1fff:fea2:97ae",
                "2a03:2260:40:0:c66e:1fff:fea2:97ae"
              ]
            },
            "hostname": "testhost"
        }
    }
"""

        expected = "2a03:2260:40:0:c66e:1fff:fea2:97ae	testhost\n"
        result = self.converter._parse_json(json.loads(simple_node))

        self.assertEqual(result, expected)

    def test_convert(self):
        f = open('tests/fixtures/case-1/hosts', 'r')
        expected = f.read()
        f.close()

        f = open('tests/fixtures/case-1/alfred_merged.json', 'r')
        result = self.converter.convert(f)
        f.close()

        self.assertEqual(str(result), str(expected))

    def test_alphabetical_order(self):
        f = open('tests/fixtures/alphabetical_order/hosts', 'r')
        expected = f.read()
        f.close()

        f = open('tests/fixtures/alphabetical_order/alfred_merged.json', 'r')
        result = self.converter.convert(f)
        f.close()

        self.assertEqual(str(result), str(expected))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()

