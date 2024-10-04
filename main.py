"""
This module is used to get some informations about the user.

- Username: Used for the welcome message, and for window names like this: [appName] for [username]
- Date & Time: Shows local date & time in the terminal, after the welcome message.

NOTE: We do not collect any personal information other than what is indicated above.
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

def icon(root): 
    "The icon of the GUI window."
    root.iconbitmap("assets\logo-pyOS.ico")
