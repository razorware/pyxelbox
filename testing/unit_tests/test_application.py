import importlib
from os import path

import unittest
###
from pyle.bootstrap import Application
from pyle.framework import TargetInfo


class TestApplication(unittest.TestCase):

    def test_initialization(self):
        exp_app_name = 'Sample App'
        exp_app_target = TargetInfo(importlib.import_module("quick_start.views"), 'sample_1')

        app_file = "sample_1_app.jss"
        markup_file = path.join("..\\..\\quick_start", app_file)

        app = Application(TargetInfo(exp_app_target.module, markup_file))

        self.assertEqual(exp_app_name, app.name)
        self.assertEqual(exp_app_target.module, app.views)
        self.assertEqual(path.abspath(path.join("..\\..\\quick_start\\views\\sample_1.jss")), app.target)

if __name__ == '__main__':
    unittest.main()
