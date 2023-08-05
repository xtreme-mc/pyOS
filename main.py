"""
PyOS : Python Operating System

Introduction : It's a project containing apps and games developed using `python3`.  

Feedback : If you have bugs, issues, glitches or got any idea to improve our program please let us know in [Github]('https://github.com/Sansoun/pyOS').

Made by Xtreme MC Studios 2023. © All rights reserved.
"""

import getpass, time

# getting the username
try:
    user = getpass.getuser()
except:
    user = "guest"

# getting local date and time
datetime = time.strftime("%H:%M %d/%m/%Y")

# welcoming the user
print(f"welcome, {user}.")
print(datetime)

# setting up the icon of the GUI
def icon(root): root.iconbitmap("assets\logo-pyOS.ico")
