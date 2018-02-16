import importlib

from os import path

import unittest
###
from pyle.framework import load_markup, \
    load_file_module, \
    load_reference, \
    sanitize_markup, \
    TargetInfo


class TestUtils(unittest.TestCase):

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

        self.assertEqual(exp_markup, sanitize_markup(source=source))

    def test_valid_json_file(self):
        exp_good_file = "test_1.json"
        markup_file = path.join("..\\markups", exp_good_file)

        self.assertIsNotNone(load_markup(markup_file))

    def test_file_not_found(self):
        markup_file = path.join("..\\markups", "foo.json")
        self.assertRaises(FileExistsError, load_markup, markup_file)

    def test_file_not_json(self):
        markup_file = path.join("..\\markups", "foo.invalid")
        self.assertRaises(Exception, load_markup, markup_file)

    def test_load_cnf_from_json(self):
        exp_cnf = {
            "Window": {
                "class": "sample.Sample",
                "title": "Sample 1: Basic Quick Start",
                "size": "w:500 h:300"
            },
            "Grid": [
                {"Label": {
                    "text": "Hello, World!",
                    "size": "w:50"
                }}
            ]
        }
        good_file = "test_1.json"
        markup_file = path.join("..\\markups", good_file)

        act_cnf = load_markup(markup_file)

        self.assertEqual(exp_cnf, act_cnf)

    def test_load_target_info(self):
        file = "sample_1_app.json"
        markup_file = path.join("..\\..\\quick_start", file)

        exp_module = TargetInfo(importlib.import_module('quick_start.views', 'sample'), "").module
        act_module = load_file_module(markup_file)

        self.assertEqual(exp_module, act_module)

    def test_load_reference(self):
        from quick_start.views.sample import Sample

        parent_module = importlib.import_module("quick_start.views")
        ref_class = load_reference(parent_module, "sample.Sample")

        self.assertIsNotNone(ref_class)
        self.assertEqual(Sample, ref_class)

if __name__ == '__main__':
    unittest.main()
