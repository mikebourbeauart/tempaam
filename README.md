# tempaam

For development:
================

Qt.py stubs for auto-completion
-------------------------------
https://github.com/mottosso/Qt.py/issues/199
1. Clone Qt.py fork and activate stub branch
2. In PyCharm add the path/to/stubs directory to the content root directory
in the project settings

Maya auto-completion
--------------------
https://stackoverflow.com/questions/39072433/how-to-reference-maya-commands-in-pycharm
1. Setup the Maya Python interpreter in Pycharm
    - In PyCharm, Ctrl+Alt+S to open your preferences and find Project Interpreter.
    - Next to the drop-down list, click the little gear icon, and choose Add Local.
    - Locate mayapy.exe or mayapy depending on your system. 
        - This is found in the bin folder in your Maya installation directory. 
            - On PC it's located under ...\Autodesk\Maya2018\bin
            - On Mac it's located under .../Autodesk/maya2016.5/Maya.app/Contents/bin/mayapy 

2. To make completions work
    - Download the Maya developer kit at https://apps.autodesk.com/MAYA/en/Detail/Index?id=5525491636376351277&os=Win64&appLang=en
    - Inside the zip file, copy the "devkit" folder to ...\Program Files\Autodesk\Maya2018\devkit
    - In PyCharm,  Click the [...] next to the drop-down list again and select More....
Select your newly added interpreter from the steps above, it will be named something like Python 2.7.6 (/path/to/mayapy) 

Click the Paths button in the bottom toolbar 
Pycharm Interpreter Toolbar 

Click the + sign and locate the folder where you extracted the developer kit. Then navigate to .../devkit/other/pymel/extras/extras/completion/py/ and hit OK.

Maya application integration
----------------------------

Allows you to run code from PyCharm and have it become activated in a session of Maya

1. Download the MayaCharm plugin into a safe place: https://plugins.jetbrains.com/plugin/8218-mayacharm
2. In PyCharm, Ctrl+Alt+S to open your preferences and find Plugins
3. Install plugin from disk
4. Find the MayaCharm plugin and install it
5. Go back to the settings and go to the MayaCharm settings
6. Follow instructions there to complete setup