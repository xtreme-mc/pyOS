from main import *

def timer(seconds):
    t.clear()
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    while seconds > 0:
        t.clear()
        t.write(seconds, align = "center", font = ("Arial", 16, "normal"))
        sleep(1)
        seconds = seconds - 1
        t.update()
    t.clear()
    t.write("finish", align = "center", font = ("Arial", 16, "normal"))

try:
    t.setup(width = 500, height = 400)
    icon()
    t.title(f"timer for {user}")
    while True:
        try:
            timer(int(t.textinput("time by seconds", "input seconds:")))
            break
        except ValueError:
            continue

    t.mainloop()
    quit(True)
except:
    quit(False)