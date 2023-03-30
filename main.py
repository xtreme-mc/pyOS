from time import sleep, strftime
import tkinter as tk
import turtle as t
import random, string
import getpass

try:
    user = getpass.getuser()
except:
    user = "guest"

print(f"welcome, {user}.")
print(strftime("%H:%M %d/%m/%Y"))

def icon():
    wnicon = t.getcanvas()._root()
    wnicon.iconbitmap("assets\logo-pyOS.ico")