from main import *

software = "draw"
class shapes:
    def __init__(self, sides, size, fill, outline):
        self.sides = sides
        self.size = size
        self.fill = fill
        self.outline = outline
    def draw(self):
        t.speed(2)
        t.fillcolor(self.fill)
        t.pencolor(self.outline)
        t.goto(0, 0)
        for side in range(self.sides):
            t.fd(self.size)
            t.lt(360/(side+1))

try:  
    icon()
    t.title(f"draw for {user}")

    while True:
        try:
            sides = int(input("number of sides: "))
            size = int(input("size of each line: "))
            fill = input("fill color: ")
            outline = input("line color: ")
            break
        except ValueError:
            print("type a valid value.")

    userShape = shapes(sides, size, fill, outline)
    userShape.draw()
    t.mainloop()
    quit(True)
except:
    quit(False)