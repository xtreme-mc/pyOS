
"""
This module is the main module for pyOS project. Make sure you have this module and you have the following modules:
```python
from time import sleep, strftime
import tkinter as tk
import turtle as t
import random, string
import getpass
```

PyOS : Python Operating System

Introduction : It's a project containing apps and games developed using `python3`.  

`calculator` : Calculate operations.
`draw` : Draw shape with sides and size.
`guess` : Guess the random number.
`timer` : Count the time remaining.
`generator` : Generate random password.

Feedback : If you have bugs, issues, glitches or got any idea to improve our program please let us know in https://github.com/Sansoun/pyOS.

Made by Xtreme MC Studios 2023. © All rights reserved.
"""

try:
    from time import sleep, strftime
    import tkinter as tk
    import turtle as t
    import random, string
    import getpass
except:
    print("make sure you have these modules: time, tkinter, turtle, random, string, getpass.")

try:
    user = getpass.getuser()
except:
    user = "guest"

print(f"welcome, {user}.")
print(strftime("%H:%M %d/%m/%Y"))

def icon():
    wnicon = t.getcanvas()._root()
    wnicon.iconbitmap("assets\logo-pyOS.ico")