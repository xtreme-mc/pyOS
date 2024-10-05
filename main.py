from freegames import square, vector
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
