from main import *
import random, string, pyperclip

def generate():
    char = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(char, k=12))

    showPw = tk.Label(root, padx=5, pady=5, text=password)
    showPw.pack()

    copy = tk.Button(root, width=20, text="copy",command=lambda:pyperclip.copy(password))
    copy.pack(padx=5, pady=5)

def upgrade():
    letters = string.ascii_letters
    num = string.digits
    punc = string.punctuation

    userInput = tk.Entry(root, width=100)
    userInput.pack(padx=5, pady=5)

    def check():
        password = userInput.get()
        if not any(word in password for word in letters):
            noLetter = tk.Label(root, padx=5, pady=5, text="Your password should contain at least one letter.")
            noLetter.pack()
        elif not any(word in password for word in num):
            noNum = tk.Label(root, padx=5, pady=5, text="Your password should contain at least one number.")
            noNum.pack()
        elif not any(word in password for word in punc):
            noPunc = tk.Label(root, padx=5,pady=5, text="Your password should contain at least one special character.")
            noPunc.pack()
        elif len(password) < 12:
            tinyLen = tk.Label(root, padx=5, pady=5, text="Your password should contain at least 12 characters.")
            tinyLen.pack()
        else:
            successMsg = tk.Label(root, padx=5, pady=5, text="Your password is okay!")
            successMsg.pack()

    upg = tk.Button(root, width=20, text="upgrade",command=check)
    upg.pack(padx=5, pady=5)

root = tk.Tk()
root.title(f"password manager for {user}")
root.geometry("400x300")

icon(root)

generate()
upgrade()

tk.mainloop()
