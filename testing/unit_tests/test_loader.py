import json
import os
import tkinter as tk
import importlib

import unittest

from pyle.framework import TargetInfo
from pyle.framework.loader import Loader, \
    S_WINDOW, \
    S_GRID


_test_view_info = {
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


class TestLoader(unittest.TestCase):

    def test_initialization(self):
        target_module = importlib.import_module('quick_start.views')
        view_info = TargetInfo(target_module, 'sample_1.jss')

        loader = Loader(view_info)

        self.assertIsNotNone(loader)
        self.assertIsNotNone(loader.window)

        view = loader.window()

        from tkinter import Tk
        from tkinter import Frame

        self.assertTrue(isinstance(view.frame, Frame))
        self.assertTrue(isinstance(view.master, Tk))

    def test_sections(self):
        target_module = importlib.import_module('quick_start.views')
        view_info = TargetInfo(target_module, 'sample_3.json')

        loader = Loader(view_info)

        self.assertTrue(len(loader.sections) == 2)
        self.assertTrue(S_WINDOW in loader.sections)
        self.assertTrue(S_GRID in loader.sections)

    def test_default_window_size(self):
        target_module = importlib.import_module('quick_start.views')
        view_info = TargetInfo(target_module, 'sample_1.json')

        loader = Loader(view_info)
        size = loader.size

        self.assertEqual(350, size['width'])
        self.assertEqual(350, size['height'])

        # functional: shows window
        # window = loader.window(cnf=size)
        # window.master.title(loader.title)
        #
        # window.master.mainloop()

    def test_window_size(self):
        target_module = importlib.import_module('quick_start.views')
        view_info = TargetInfo(target_module, 'sample_2.json')

        loader = Loader(view_info)
        size = loader.size

        self.assertEqual(500, size['width'])
        self.assertEqual(300, size['height'])

        # functional: shows window
        window = loader.window(cnf=size)
        window.master.title(loader.title)

        tk_module = importlib.import_module('tkinter')
        cls_label = getattr(tk_module, 'Label')
        tk_label = cls_label(window.frame, text="Hello,")
        tk_label.grid(row=0, column=0)

        label = tk.Label(window.frame, text="World!")
        label.grid(row=1, column=1)

        window.master.mainloop()

    def test_child_container_empty(self):
        target_module = importlib.import_module('quick_start.views')
        view_info = TargetInfo(target_module, 'sample_1.json')

        loader = Loader(view_info)

        self.assertTrue(len(loader.children) == 0)

    def test_child_container(self):
        test_path = '..\\..\\quick_start\\views'
        expected_file = os.path.join(test_path, 'sample_3a.json')
        test_file = os.path.join(test_path, 'sample_3a.jss')

        if os.path.isfile(test_file):
            print(os.path.abspath(test_file))

            with open(expected_file) as m_file:
                test_markup = json.load(m_file)

        target_module = importlib.import_module('quick_start.views')
        view_info = TargetInfo(target_module, 'sample_3a.jss')

        loader = Loader(view_info)

        self.assertTrue(len(loader.children) == 1)


if __name__ == '__main__':
    unittest.main()
