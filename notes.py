from main import *

import tkinter as tk
from tkinter import filedialog

def new_file():
    "Creating a new text file."
    text.delete("1.0", tk.END)

def open_file():
    "Opening a text file."
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text.delete("1.0", tk.END)
            text.insert(tk.END, content)

def save_file():
    "Saving the text file."
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        content = text.get("1.0", tk.END)
        with open(file_path, "w") as file:
            file.write(content)

app = tk.Tk()
icon(app)
app.title(f"Notes for {user}")

text = tk.Text(app, wrap=tk.WORD)
text.pack(expand=True, fill=tk.BOTH)

menu = tk.Menu(app)
app.config(menu=menu)

"Creating the navigation bar."
file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

app.mainloop()
