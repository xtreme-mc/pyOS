from main import *
import random, string, pyperclip

def generate():
    char = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(char, k=12))
    
    showPw = tk.Label(root, padx=10, pady=10, text=password)
    showPw.pack()

    copy = tk.Button(root, text="copy", padx=10, command=pyperclip.copy(password))
    copy.pack()

def upgrade():
    letters = string.ascii_letters
    num = string.digits
    punc = string.punctuation

    userInput = tk.Entry(root, padx=10)
    userInput.pack

    def check():
        userInput.get()
        if not any(word in userInput for word in letters):
            noLetter = tk.Label(root, padx=10,pady=10, text="your password should contain at least one letter.")
            noLetter.pack()
        elif not any(word in userInput for word in num):
            noNum = tk.Label(root, padx=10,pady=10, text="your password should contain at least one number.")
            noNum.pack()
        elif not any(word in userInput for word in punc):
            noPunc = tk.Label(root, padx=10,pady=10, text="your password should contain at least one special character.")
            noPunc.pack()
        elif len(userInput) < 12:
            tinyLen = tk.Label(root, padx=10,pady=10, text="your password should contain at least 12 characters.")
            tinyLen.pack() 
        else:
            successMsg = tk.Label(root, padx=10,pady=10, text="your password is okay!.")
            successMsg.pack()

    upg = tk.Button(root, text="upgrade", padx=40, pady=20, command=check)
    upg.pack()

root = tk.Tk()
root.title(f"password manager for {user}")
icon(root)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="generator", command=generate)
file_menu.add_command(label="upgrader", command=upgrade)
file_menu.add_separator()
file_menu.add_command(label="exit", command=root.quit)
menu_bar.add_cascade(label="actions", menu=file_menu)
root.config(menu=menu_bar)

tk.mainloop()
