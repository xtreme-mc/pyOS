from main import *

class shapes:
    """shows a shape in a graphical window with number of sides and size specified by user."""
    def __init__(self, master, sides, size):
        self.master = master
        t.clear()
        self.hideturtle()
        self.pendown()
        self.speed(2)
        self.goto(0, 0)
        for _ in range(sides):
            self.fd(size)
            self.lt(360/(sides))

icon()
t.title(f"draw for {user}")
while True:
    try:
        sides = int(t.textinput("input sides", "number of sides: "))
        size = int(t.textinput("input size", "size of each line: "))
        break
    except ValueError:
        print("type a valid value.")

troot = t.Turtle()
userShape = shapes(troot, sides, size)
t.mainloop()
quit(True)