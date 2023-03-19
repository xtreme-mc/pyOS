from main import *

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

try:
    t.setup(width = 500, height = 400)
    icon()
    t.title(f"generator for {user}")
    t.hideturtle()
    t.penup()

    password = generate_password(12)
    t.goto(0, 0)
    t.write(password, align = "center", font = ("Arial", 16, "normal"))
    t.goto(0, -32)
    t.write("copied to clipboard", align = "center", font = ("Arial", 16, "normal"))
    pyperclip.copy(password)
    t.mainloop()
    quit(True)
except:
    quit(False)