import unittest
import freifunk_etc_hosts
import logging
import os.path
import json

class TestConverter(unittest.TestCase):
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
    f = open('tests/fixtures/case-1/hosts', 'r')
    case_1_expected = f.read()
    f.close()

    def setUp(self):
        self.converter = freifunk_etc_hosts.Converter()

    def test_parse_json(self):
        expected = "2a03:2260:40:0:c66e:1fff:fea2:97ae	testhost\n"
        result = self.converter._parse_json(json.loads(self.simple_node))

        self.assertEqual(result, expected)

    def test_convert(self):
        f = open('tests/fixtures/case-1/alfred_merged.json', 'r')
        result = self.converter.convert(f)
        f.close()

        self.assertEqual(str(result), str(self.case_1_expected))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()

