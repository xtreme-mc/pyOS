from main import *
from tkinter import filedialog

class editor:
    def __init__(self, master):
        self.master = master
        master.title(f"open text for {user}")
        icon(master)
        self.filename = None

        self.menu_bar = tk.Menu(master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        master.config(menu=self.menu_bar)

        self.text_widget = tk.Text(master)
        self.text_widget.pack(expand=True, fill="both")

    def new_file(self):
        self.filename = None
        self.text_widget.delete(1.0, tk.END)

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt",
                                                    filetypes=[("Text Files", "*.txt"),
                                                               ("All Files", "*.*")])
        if self.filename:
            self.text_widget.delete(1.0, tk.END)
            with open(self.filename, "r") as file:
                self.text_widget.insert(1.0, file.read())

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_widget.get(1.0, tk.END))
        else:
            self.save_as_file()

    def save_as_file(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text Files", "*.txt"),
                                                                ("All Files", "*.*")])
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_widget.get(1.0, tk.END))

root = tk.Tk()
text_editor = editor(root)
root.mainloop()

sys.exit()