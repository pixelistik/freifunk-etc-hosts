import unittest
from freifunk_etc_hosts import converter
import logging
import os.path

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
    f = open('tests/fixtures/case-1/alfred_merged.json', 'r')
    case_1_input = f.read()
    f.close()

    f = open('tests/fixtures/case-1/hosts', 'r')
    case_1_output = f.read()
    f.close()

    def setUp(self):
        self.converter = converter.Converter()

    def testConvert(self):
        expected = "2a03:2260:40:0:c66e:1fff:fea2:97ae	testhost\n"
        result = self.converter.convert(self.simple_node)

        self.assertEqual(result, expected)

    def testConvertFile(self):
        result = self.converter.convert(self.case_1_input)

        self.assertEqual(str(result), str(self.case_1_output))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()

