import getpass, time

def user_get():
    "Returns local username from the machine."
    try:
        user = getpass.getuser()
    except:
        print("Cannot find local username from your machine.")
        user = "user"
    return user

def datetime_get():
    "Returns local date and time from the machine."
    try:
        datetime = time.strftime("%H:%M %d/%m/%Y")
    except:
        datetime = "Cannot find local date and time from your machine."
        return datetime

def icon(root): 
    "The window icon of the graphical user interface."
    root.iconbitmap("assets\logo-pyOS.ico")

print("Starting...")
time.sleep(1)
user_get()
print(f"welcome, {user_get}.")
print(datetime_get)
