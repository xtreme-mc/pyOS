from time import sleep, strftime
from random import choice
from math import sqrt, pi
import tkinter as tk
import turtle as t

user = ""
while user == "":
    user = input("please input your name to start: ")

print("starting...")
sleep(1)
print(f"welcome, {user}.")
print(strftime("%H:%M %d/%m/%Y"))

def icon():
    root = t.getcanvas()._root()
    root.iconbitmap("assets\logo-pyOS.ico")