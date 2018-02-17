# Running Quick Start applications

The recommended point of execution is `runner.py`. This script can execute in one of two ways.

* **pyle.Bootstrap** class can be instantiated and executed - either as default class or as inherited  
* **pyle.Application** class can be instantiated and executed - either as default or as inherited

Executing from Bootstrap allows for more specialized configuration.

### Window Section

 default: `sample_1_app.json` | user-defined: `sample_2_app.json`
 ![default window size][def_win] | ![user defined size][usr_win]
 

You can execute `runnery.py` passing in either one of the **sample_x_app.json** files shown in the table.
![runner settings in PyCharm][runner]


[def_win]: https://github.com/razorware/pyxelbox/blob/master/images/350_x_350_default_window.PNG "Default Window Size"
[usr_win]: https://github.com/razorware/pyxelbox/blob/master/images/500_x_300_window.PNG "User Defined Window Size"
[runner]: https://github.com/razorware/pyxelbox/blob/master/images/quick_start_sample_configs.PNG "PyCharm runner configuration"