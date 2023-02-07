"""
This project is created by Xtreme MC Studios.
This is a simulator, not a real Operating System.
Visit us on: https://youtube.com/@xtrememc8661
"""

#!/usr/bin/env python3
from time import sleep, strftime #date and time
from math import sqrt
import turtle as t

#username
user = input("please input your name to start the OS: ")
print("starting...")
sleep(1)
print(f'''welcome to pyOS V1.0.1, {user}.
type /help for help.''')

while True:
    def run(app):
        print(f"opening {app} for {user}...")
        sleep(1)
        print(f"{app} opened successfully.")
        return None

    def quit(app):
        quit = input(f"are you sure you want to quit {app}? y/n: ")
        if quit == "y":
            print(f"{app} quited successfully.")
        return None

    software=input() #choose app

#help
    if software == "/help":
        print(f'''commands for {user}:
OS commands:
/help : list of commands.
/calc : opens the calculator.
/draw : draws a picture in turtle.
/time : show date and time.
/game : coming soon...
/exit : exit the program.''')

#calculator
    elif software == "/calc": 
        run("calculator")
        
        while True:
            operation = input("Please type the math operation: +, -, *, /, sqrt or quit: ") #choose operation

            if operation in ("+", "*", "-", "/", "%"):
#addiction
                if operation == "+":
                    while True:
                        try:
                            a = float(input("Enter your first number: "))
                            b = float(input("Enter your second number: "))
                            print(f"{a} + {b} = ")
                            print(a + b)
                            break
                        except:
                            print("please use a number.")

#subtraction
                elif operation == "-":
                    while True:
                        try:
                            a = float(input("Enter your first number: "))
                            b = float(input("Enter your second number: "))
                            print(f"{a} - {b} = ")
                            print(a - b)
                            break
                        except:
                            print("please use a number.")

#multiplication
                elif operation == "*":
                    while True:
                        try:
                            a = float(input("Enter your first number: "))
                            b = float(input("Enter your second number: "))
                            print(f"{a} * {b} = ")
                            print(a * b)
                            break
                        except:
                            print("please use a number.")                

#division
                elif operation == "/":
                    while True:
                        try:
                            a = float(input("Enter your first number: "))
                            b = float(input("Enter your second number: "))
                            print(f"{a} / {b} = ")
                            print(a / b)
                            break
                        except:
                            print("please use a number.")

#modulo
                elif operation == "%":
                    while True:
                        try:
                            a = float(input("Enter your first number: "))
                            b = float(input("Enter your second number: "))
                            print(f"{a} % {b} = ")
                            print(a % b)
                            break
                        except:
                            print("please use a number.")

#square root
            elif operation == "sqrt":
                while True :
                    try:
                        c = float(input("Enter your number: "))
                        print(f"√{c} = ")
                        print(sqrt(abs(c)))
                        break
                    except:
                        print("please use a number.")

#quit app
            elif operation == "quit":
                quit("calculator")
                break

#invalid operator
            else:
                print(f"{user}, You have not typed a valid operator or syntax.")

#calculate again
            again = input("calculate again? y/n: ")
            if again == "n":
                print(f"calculator quited successfully.") ;break

# pics shapes
    elif software == "/draw":
#circle
        def circle():
            root = t.getcanvas()._root()
            root.iconbitmap("shape.ico")
            t.title(f"{shape} for {user}")
            t.clear()
            t.bgcolor("brown")
            t.pencolor("orange")
            t.fillcolor("yellow")
            t.speed(3)
            t.penup()
            t.setpos(0, 0)
            t.pendown()
            t.begin_fill()
            t.circle(200)
            t.end_fill()
            t.mainloop()
            return("done")

#square
        def square():
            t.title(f"{shape} for {user}")
            t.clear()
            t.bgcolor("brown")
            t.pencolor("orange")
            t.fillcolor("yellow")
            t.speed(3)
            t.penup()
            t.setpos(0, 0)
            t.pendown()
            t.begin_fill()
            for start in range(4):
                t.fd(200)
                t.lt(90)
            t.end_fill()
            t.mainloop()
            return("done")

#triangle
        def triangle():
            t.title(f"{shape} for {user}")
            t.clear()
            t.bgcolor("brown")
            t.pencolor("orange")
            t.fillcolor("yellow")
            t.speed(3)
            t.penup()
            t.setpos(0, 0)
            t.pendown()
            t.begin_fill()
            for start in range(3):
                t.fd(200)
                t.lt(120)
            t.mainloop()
            t.end_fill()
            return("done")

#rectangle
        def rectangle():
            t.title(f"{shape} for {user}")
            t.clear()
            t.bgcolor("brown")
            t.pencolor("orange")
            t.fillcolor("yellow")
            t.speed(3)
            t.penup()
            t.setpos(0, 0)
            t.pendown()
            t.begin_fill()
            for start in range(3):
                t.fd(400)
                t.lt(90)
                t.fd(200)
                t.lt(90)
            t.end_fill()
            t.mainloop()
            return("done")

        while True:
            shape = input("input your shape (quit to exit): ") #choose shape

            if shape == "circle":
                circle()

            elif shape == "square":
                square()

            elif shape == "triangle":
                triangle()

            elif shape == "rectangle":
                rectangle()         

#quit app
            elif shape == "quit":
                quit("pics"); break

#invalid shape
            else:
                print("please type a valid shape.")

#game (soon)
    elif software == "/game":
        print("soon...")

#time
    elif software == "/time":
        while True:
            day = strftime("%A, %B %d, %Y")
            hour = strftime("%H:%M:%S")
            window = input("do you want output in another window? y/n: ")

            def clock():
                t.title(f"time for {user}")
                t.clear()
                t.bgcolor("brown")
                t.setpos(0, 0)
                t.hideturtle()
                t.penup()
                t.pencolor("yellow")
                t.write(day, align = "center", font = ("Arial", 16, "normal"))
                t.setpos(0, -24)
                t.write(hour, align = "center", font = ("Arial", 16, "normal"))
                t.mainloop()

            if window == "y":
                run("time")
                clock(); break

            elif window == "n":
                print(day)
                print(hour)
                break

            else:
                print("please type y (yes) or n (no).")    

#exit OS
    elif software == "/exit":
        exit = input(f"{user}, are you sure you want to exit the OS? y/n: ")
        if exit == "y":
            print("exiting pyOS...")
            sleep(1)
            break; exit()

#invalid app
    else:
        print(f'''please type a valid software, {user}. 
hint: use /help to see more.''')
#finish