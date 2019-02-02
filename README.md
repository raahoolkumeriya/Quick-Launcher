# Quick-Launcher

[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/2499/badge)](https://bestpractices.coreinfrastructure.org/projects/2499) [![CircleCI](https://circleci.com/gh/raahoolkumeriya/Quick-Launcher/tree/master.svg?style=svg)](https://circleci.com/gh/raahoolkumeriya/Quick-Launcher/tree/master)

Python app to perform day-to-day task on single click 

![screenshot from 2019-01-04 23-54-06](https://user-images.githubusercontent.com/31859032/50704240-b3cc2380-107c-11e9-92f1-b33fedb23efd.png)

Python Quick Launcher is a tool for doing quick day-to-day task on desktop enviornment. This is Python Qt (PyQt) GUI applications.

The UI provide interface to do task on click button. 

Note: Currently it is with Python 3, Pull requests for Quick Launcher welcome!

## Installation:
---------------
To use the latest developmental version without installing:

    ``` 
    git clone git@github.com:raahoolkumeriya/Quick-Launcher.git
    ```

## Requirement (Python Packages added in script): 
To install all dependencies 
    ``` 
    pip -r requirements.txt
    ```

Package|Version
-----|-----
PyQt5| 5.9.2
xlsxwriter|1.1.2
sqlalchemy|1.2.15
cx_Oracle| 7.0.0
pyperclip|1.7.0

## Usage
-------
    ``` 
    python quicklaunch.py
    ```

Development
-----------
Please report bugs, along with their matching pull-requests, to:
https://github.com/raahoolkumeriya/Quick-Launcher


### Flow of Tool Development: 
- Design the tool using qt 4 Designser
- Convert ui file into py using below command
```    
    pyuic5 -x quicklaunch.ui -o quicklaunch.py
```

FAQ
---
**The app can be scale to large extend to use mutiple python utilities ?**

![screenshot from 2019-01-05 00-12-39](https://user-images.githubusercontent.com/31859032/50704809-b3348c80-107e-11e9-8fc5-170d98e6963a.png)
