"""This project is created by Xtreme MC Studios.
This is a simulator, not a real Operating System.
Visit us on: https://youtube.com/@xtrememc8661"""

#!/usr/bin/env python3
from time import sleep, strftime
from math import sqrt
import turtle as t

#username
while True:
    user = input("please input your name to start the OS: ")
    if user == "":
        print("please type a valid name.")
    else:
        print("starting...")
        sleep(1)
        print(f'''welcome to pyOS V0.1.2, {user}.
type /help for help.'''); break

#app icon
def icon():
    root = t.getcanvas()._root()
    root.iconbitmap("main\logo-pyOS.ico")

#run app
def run(app):
    print(f"opening {app} for {user}...")
    sleep(1)
    print(f"{app} opened successfully.")
    return True

#quit app
def quit(app):
    print(f"{app} quited successfully.")
    return True

while True:
    software=input()

#help
    if software == "/help":
        print(f'''commands for {user}:
OS commands:
/help : list of commands.
/calc : opens the calculator.
/draw : draws a picture in turtle.
/time : show date and time.
/quiz : coming soon...
/exit : exit the program.''')

#calculator
    elif software == "/calc": 
        run("calculator")
        
        while True:
            operation = input("Please type the math operation: +, -, *, /, sqrt or quit: ")

            if operation == "+": #add
                while True:
                    try:
                        a = float(input("Enter your first number: "))
                        b = float(input("Enter your second number: "))
                        print(f"{a} + {b} = ")
                        print(a + b)
                        break
                    except:
                        print("please use a number.")

            elif operation == "-": #sub
                while True:
                    try:
                        a = float(input("Enter your first number: "))
                        b = float(input("Enter your second number: "))
                        print(f"{a} - {b} = ")
                        print(a - b)
                        break
                    except:
                        print("please use a number.")

            elif operation == "*": #multi
                while True:
                    try:
                        a = float(input("Enter your first number: "))
                        b = float(input("Enter your second number: "))
                        print(f"{a} * {b} = ")
                        print(a * b)
                        break
                    except:
                        print("please use a number.")                

            elif operation == "/": #div
                while True:
                    try:
                        a = float(input("Enter your first number: "))
                        b = float(input("Enter your second number: "))
                        print(f"{a} / {b} = ")
                        print(a / b)
                        break
                    except:
                        print("please use a number.")

            elif operation == "%": #mod
                while True:
                    try:
                        a = float(input("Enter your first number: "))
                        b = float(input("Enter your second number: "))
                        print(f"{a} % {b} = ")
                        print(a % b)
                        break
                    except:
                        print("please use a number.")

            elif operation == "sqrt": #sqrt
                while True :
                    try:
                        c = float(input("Enter your number: "))
                        print(f"√{c} = ")
                        print(sqrt(abs(c)))
                        break
                    except:
                        print("please use a number.")

            elif operation == "quit": #quit
                quit("calculator"); break

            else: #invalid
                print(f"{user}, You have not typed a valid operator or syntax.")

#calculate again
            calc_again = input("calculate again? y/n: ")
            if calc_again == "n":
                quit("calculator") ;break

# pics shapes
    elif software == "/draw":
        icon()

        t.title(f"draw for {user}")
#circle
        def shape_cir():
            t.clear()
            t.bgcolor("brown")
            t.pencolor("orange")
            t.fillcolor("yellow")
            t.speed(3)
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.begin_fill()
            t.circle(200)
            t.end_fill()
            return True

#square
        def shape_squ():
            t.clear()
            t.bgcolor("brown")
            t.pencolor("orange")
            t.fillcolor("yellow")
            t.speed(3)
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.begin_fill()
            for start in range(4):
                t.fd(200)
                t.lt(90)
            t.end_fill()
            return True

#triangle
        def shape_tri():
            t.clear()
            t.bgcolor("brown")
            t.pencolor("orange")
            t.fillcolor("yellow")
            t.speed(3)
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.begin_fill()
            for start in range(3):
                t.fd(200)
                t.lt(120)
            t.end_fill()
            return True

#rectangle
        def shape_rec():
            t.clear()
            t.bgcolor("brown")
            t.pencolor("orange")
            t.fillcolor("yellow")
            t.speed(3)
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.begin_fill()
            for start in range(3):
                t.fd(400)
                t.lt(90)
                t.fd(200)
                t.lt(90)
            t.end_fill()
            return True

        while True:
            try:
                shape = t.textinput("Enter your shape" ,"Type exit to quit:")

                if shape == "circle":
                    shape_cir()

                elif shape == "square":
                    shape_squ()

                elif shape == "triangle":
                    shape_tri()

                elif shape == "rectangle":
                    shape_rec()         

                elif shape == "quit": #quit
                    t.clear()
                    t.penup()
                    t.goto(0, 0)
                    t.write("please wait...", align = "center", font = ("Arial", 16, "normal"))
                    t.bye()
                    quit("draw")
                    break

                else: #invalid
                    t.clear()
                    t.penup()
                    t.goto(0, 0)
                    t.write("please type a valid shape.", align = "center", font = ("Arial", 16, "normal"))

                t.goto(0,0)
                t.penup()
                draw_again = t.textinput("draw again ?", "type y/n:")
                if draw_again == "n":
                    t.bye()
                    quit("draw")
                    break
            except:
                t.bye()
                quit("draw")
                break

#game
    elif software == "/quiz":
        print("soon...")

#time
    elif software == "/time":
        day = strftime("%A, %B %d, %Y")
        hour = strftime("%H:%M:%S")

        icon()
        t.title(f"time for {user}")

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
            return True

        run("time")
        clock()
        quit("time")

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