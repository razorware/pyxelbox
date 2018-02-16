# Running Quick Start applications

The recommended point of execution is `runner.py`. This script can execute in one of two ways.

* **pyle.Bootstrap** class can be instantiated and executed - either as default class or as inherited  
* **pyle.Application** class can be instantiated and executed - either as default or as inherited

Executing from Bootstrap allows for more specialized configuration.

### Window Section

If there is not setting in for the window size, PyLE provides a default window setting of 350x350.
![default window size][def_win]

...compared to setting a size parameter in the Window section
![user defined size][usr_win]


[def_win]: (https://github.com/razorware/pyxelbox/blob/master/images/350_x_350_default_window.PNG) "Default Window Size"
[usr_win]: (https://github.com/razorware/pyxelbox/blob/master/images/500_x_300_window.PNG) "User Defined Window Size"