from os import path

import unittest
###
from pyledriver.framework import load_markup, \
    clean_markup


class TestJsonUtils(unittest.TestCase):

    def test_clean_json_source(self):
        source = '{	/*	section: Window */\r' \
                    '"Window": [\r' \
                    '/* set up the window object */ \r' \
                    '{"class": "sample.Sample"},\r\n' \
                    '{"title": "Sample 1: Basic Quickstart"},\r' \
                    '//	default size if properties not included \n' \
                    '{"size": "w:500 h:300"}\r' \
                 ']}'
        exp_markup = '{"Window": [ ' \
                     '{"class": "sample.Sample"},' \
                     '{"title": "Sample 1: Basic Quickstart"},' \
                     '{"size": "w:500 h:300"}' \
                     ']}'

        self.assertEqual(exp_markup, clean_markup(source=source))

    def test_valid_json_file(self):
        exp_good_file = "sample_1.json"
        markup_file = path.join("..\\markups", exp_good_file)

        self.assertIsNotNone(load_markup(markup_file))

    def test_file_not_found(self):
        markup_file = path.join("..\\markups", "foo.json")
        self.assertRaises(FileExistsError, load_markup, markup_file)

    def test_file_not_json(self):
        markup_file = path.join("..\\markups", "foo.invalid")
        self.assertRaises(Exception, load_markup, markup_file)

    def test_load_json_file(self):
        exp_markup = {
            "Window": [
                {"class": "sample.Sample"},
                {"title": "Sample 1: Basic Quick Start"},
                {"size": "w:500 h:300"}
            ],
            "Grid": [
                {"Label": [
                    {"text": "Hello, World!"},
                    {"size": "w:50"}
                ]}
            ]
        }
        exp_good_file = "sample_1.json"
        markup_file = path.join("..\\markups", exp_good_file)

        act_markup = load_markup(markup_file)

        self.assertEqual(exp_markup, act_markup)


if __name__ == '__main__':
    unittest.main()
