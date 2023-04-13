from main import *

class shapes:
    """shows a shape in a graphical window with number of sides and size specified by user."""
    def __init__(self, master, sides, size):
        t.clear()
        master.hideturtle()
        master.pendown()
        master.speed(2)
        master.goto(0, 0)
        for _ in range(sides):
            master.fd(size)
            master.lt(360/(sides))

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