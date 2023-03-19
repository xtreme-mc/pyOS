from main import *

class shapes:
    def __init__(self, sides, size):
        self.sides = sides
        self.size = size

    def draw(self):
        t.clear()
        t.hideturtle()
        t.pendown()
        t.speed(2)
        t.goto(0, 0)
        for _ in range(self.sides):
            t.fd(self.size)
            t.lt(360/(self.sides))

try:  
    icon()
    t.title(f"draw for {user}")
    while True:
        try:
            sides = int(t.textinput("input sides", "number of sides: "))
            size = int(t.textinput("input size", "size of each line: "))
            break
        except ValueError:
            print("type a valid value.")

    userShape = shapes(sides, size)
    userShape.draw()
    t.mainloop()
    quit(True)
except:
    quit(False)