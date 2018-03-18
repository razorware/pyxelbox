import importlib

from os import path

import unittest
###
from pyle.framework import load_markup, \
    load_file_module, \
    load_reference, \
    TargetInfo


class TestUtils(unittest.TestCase):

    def test_valid_jss_file(self):
        exp_good_file = "test_1.jss"
        markup_file = path.join("..\\markups", exp_good_file)

        self.assertIsNotNone(load_markup(markup_file))

    def test_load_target_info(self):
        file = "sample_1_app.jss"
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
