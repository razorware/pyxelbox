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
        view_info = TargetInfo(target_module, 'sample_1.json')

        loader = Loader(view_info)

        self.assertIsNotNone(loader)
        self.assertIsNotNone(loader.window)

        view = loader.window()

        from tkinter import Tk
        from tkinter import Frame

        self.assertTrue(isinstance(view, Frame))
        self.assertTrue(isinstance(view.master, Tk))

    def test_sections(self):
        target_module = importlib.import_module('quick_start.views')
        view_info = TargetInfo(target_module, 'sample_1.json')

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

        # functional - shows window
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

        # functional - shows window
        window = loader.window(cnf=size)
        window.master.title(loader.title)

        window.master.mainloop()


if __name__ == '__main__':
    unittest.main()
