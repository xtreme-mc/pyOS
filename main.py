from time import sleep, strftime
import tkinter as tk
import turtle as t
import random, getpass, string, pyperclip

try:
    user = getpass.getuser()
except:
    user = "guest"

print(f"welcome, {user}.")
print(strftime("%H:%M %d/%m/%Y"))

def icon():
    t.getcanvas()._root().iconbitmap("assets\logo-pyOS.ico")