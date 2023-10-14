"""
PyOS : Python Operating System

Introduction : It's a project containing apps and games developed using `python3`.  

Feedback : If you have bugs, issues, glitches or got any idea to improve our program please let us know in [Github]('https://github.com/Sansoun/pyOS').

Made by Xtreme MC Studios 2023. © All rights reserved.
"""

import getpass, time

try:
    "Trying to get username."
    user = getpass.getuser()
except:
    "Else username is guest."
    user = "guest"

"Getting local date and time."
datetime = time.strftime("%H:%M %d/%m/%Y")

"Welcoming the user."
print(f"welcome, {user}.")
print(datetime)

"Setting up the icon of the GUI."
def icon(root): root.iconbitmap("assets\logo-pyOS.ico")
