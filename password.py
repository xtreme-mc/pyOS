from main import *
from tkinter import messagebox
import tkinter as tk
import string

"Setting up characters."
letters = string.ascii_letters
num = string.digits
punc = string.punctuation

root = tk.Tk()
root.title(f"password manager for {user}")
root.geometry("400x200")
icon(root)

paragraph = tk.Label(root, text="Type your password below to upgrade.\n\nNote: We do not collect any data.")
paragraph.pack(padx=5, pady=5)

userInput = tk.Entry(root, width=50)
userInput.pack(padx=5, pady=5)

def check():
    "Checking the password."
    password = userInput.get()
    if not any(word in password for word in letters):
        noLetter = messagebox.showinfo("Error", "Your password should contain at least one letter.")
    elif not any(word in password for word in num):
        noNum = messagebox.showinfo("Error", "Your password should contain at least one number.")
    elif not any(word in password for word in punc):
        noPunc = messagebox.showinfo("Error", "Your password should contain at least one special character.")
    elif len(password) < 8:
        tinyLen = messagebox.showinfo("Error", "Your password should contain at least 8 characters.")
    else:
        successMsg = messagebox.showinfo("Congratulations", "Your password is okay!")

upg = tk.Button(root, text="upgrade", command=check, width=10)
upg.pack(padx=5, pady=5)

root.mainloop()
exit()
