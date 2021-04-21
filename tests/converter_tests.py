import unittest
import json
from digital_thought_commons.converters import json as json_converter


class TestDigests(unittest.TestCase):

    def test_json_to_excel(self):
        with open(r'/Users/matthew.westwood-hill/PycharmProjects/dt/digital-thought-osint/tests/out2.json', 'r') as j:
            data = json.load(j)
            json_converter.json_list_to_excel(data, 'report', 'out3.xlsx')