<p align="center">
    <img src="https://github.com/razorware/pyxelbox/blob/master/images/razorware_pyxelbox_logo.png"
         alt="razorware.pyxelbox logo"
         title="RazorWare.Pyxelbox" />
</p>

# Pyxelbox: Python Lightweight Engine (PyLE)
*(and soon-to-come PyDE Pyper)*

Pyxelbox is a python-powered, micro-framework for creating lightweight desktop GUIs by consuming and interpreting JSON markup into visual interfaces making extensive use of the Tcl/Tk package distributed with Python 3.x.

![JSON markup to Tkinter GUI][json_to_gui]

Pyxelbox introduces the following:

* **PyLE** is a lightweight environment engine that consumes JSON as a markup language. The markup is a GUI development tool allowing developers to create robust user interfaces. PyLE relies on a convention conducive to creating manageable graphic interfaces that implement the Model-View-Presenter (MVP) paradigm.

The JSON markup differs from pure JSON only by the inclusion of comments - both multi- and single-line.
```
{
  /*
    Quick Start demonstrates several features of JSON markup.
    1. comments: both in single- and multi-line formats. To 
       validate JSON markup, comments are stripped away before 
       being loaded into the engine.

    2. sections: while sections	are not required to appear in 
       the order shown in this and subsequent tutorials; however,
       it is recommended as a general practice.

    3. packed parameters: values take advantage of packing 
       parameters in a manner similar to CSS. Tutorials will
       demonstrate both packed and expanded varieties of 
       parameters.
  */
	
  // section: Window
  "Window": {
    // set up the window object
    class": "sample.Sample",
    "title": "Sample 1: Basic Quick Start",
    // packed size parameters
    "size": "w:500 h:300"
  },
  // section: Grid
  "Grid": [
    {"Label": {
      "text": "Hello, World!",
      "size": "w:50"
    }}
  ]
}
```

Prior to consumption, the above JSON markup is sanitized by stripping the comments leaving the following:
```json
{
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
```

Before an application can be run, the PyLE bootstrap needs to know where to find the initial/start up view:
```
{
  /*
    Application markup tells the bootstrap the name of the application
    and the target (t:) initial view.
  */
  "application": "n:'Sample App' t:views.sample_1"
}
```

* runner.py
the recommended method to execute the bootstrap uses `runner.py`:
```python
# the advantage of this script is that the *_app.json file is passed in the command line parameter
import sys

from pyle.bootstrap import Application

if __name__ == "__main__":
    file = sys.argv[1]

    app = Application(file)
    app.mainloop()
```

* bootstrap.py
an alternative method for execution using `bootstrap.py`:
```python
import importlib

from pyle import TargetInfo
from pyle.bootstrap import Bootstrap


# custom implementation of the PyLE Bootstrap class
class Application(Bootstrap):
    def __init__(self, file):
        mod_info = TargetInfo(importlib.import_module('module_name'), file)
        Bootstrap.__init__(self, mod_info)
```

[json_to_gui]: https://github.com/razorware/pyxelbox/blob/master/images/json_to_gui.png "JSON markup to Tkinter GUI"
