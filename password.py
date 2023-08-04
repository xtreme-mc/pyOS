from main import *
from tkinter import messagebox
import tkinter as tk
import random, string

def generate():
    def new():
        char = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choices(char, k=random.randint(8,16)))
        showPw = messagebox.showinfo(f"Password for {user}", f"Here is your password:\n\n{password}")

    generatePw = tk.Button(root, text="generate", command=new)
    generatePw.pack(padx=5, pady=5)

def upgrade():
    letters = string.ascii_letters
    num = string.digits
    punc = string.punctuation

    userInput = tk.Entry(root)
    userInput.pack(padx=5, pady=5)

    def check():
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

    upg = tk.Button(root, text="upgrade", command=check)
    upg.pack(padx=5, pady=5)

root = tk.Tk()
root.title(f"password manager for {user}")
root.geometry("200x100")

icon(root)

generate()
upgrade()

tk.mainloop()
exit()
