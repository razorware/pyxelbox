import sys
import importlib

from os import path

from pyle.framework import TargetInfo
from pyle.bootstrap import Application

if __name__ == "__main__":
    module = importlib.import_module('quick_start')
    file = path.join(path.dirname(module.__file__), sys.argv[1])

    app = Application(TargetInfo(module, file))
    app.mainloop()
