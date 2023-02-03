# used modules
from importlib import reload #reloading libraries
from turtle import Screen, mainloop
from time import sleep, strftime
from math import sqrt
import turtle as t
import random as r
import pygame as p

# main script
user = input("please input your name to start the OS: ")
print("starting...")
sleep(1)
print('''welcome to pyOS V1.0.1, {}.
type /help for help.'''.format(user)) #format {variable}

while True:
    def run(app):
        print("opening {} for {}...".format(app, user))
        sleep(1)
        print("{} opened successfully.".format(app))

    def quit(app):
        quit = input("are you sure you want to quit {}? y/n: ".format(app))
        if quit == "y":
            print("{} quited successfully.".format(app))

    software=input()

    if software == "/help":
        print('''commands for {}:
OS commands:
/calc : opens the calculator.
/pic : draws a picture in turtle.
other commands:
/help : list of commands.
/time : show date and time.
/exit : exit the program.'''.format(user))

# calculator
    elif software == "/calc": 
        run("calculator")
        
        while True:
            operation = input('''Please type the math operation you'd like to complete:
+ : addition
- : subtraction
* : multiplication
/ : division
% : modulo
sqrt : square root
abs : absolute value
quit : quit the app
''')
            if operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == "%":

                a = float(input("Enter your first number: "))
                b = float(input("Enter your second number: "))

                if operation == "+":
                    try:
                        print("{} + {} = ".format(a, b))
                        print(a + b)
                    except:
                        print("please use a float.")

                elif operation == "-":
                    try:
                        print("{} - {} = ".format(a, b))
                        print(a - b)
                    except:
                        print("please use a float.")

                elif operation == "*":
                    try:
                        print("{} * {} = ".format(a, b))
                        print(a * b)
                    except:
                        print("please use a float.")                

                elif operation == "/":
                    try:
                        print("{} / {} = ".format(a, b))
                        print(a / b)
                    except:
                        print("please use a float.")

                elif operation == "%":
                    print("{} % {} = ".format(a,b))
                    try:
                        print(a % b)
                    except:
                        print("please use a float.")

            elif operation == "sqrt":
                    try:
                        c = float(input("Enter your number: "))
                        print("√ {} = ".format(c))
                        print(sqrt(c))
                    except:
                        print("please use a float.")

            elif operation == "abs":
                    try:
                        c = float(input("Enter your number: "))
                        print("|{}| = ".format(c))
                        print(abs(c))
                    except:
                        print("please use a float.")

            elif operation == "quit":
                quit("calculator")
                break

            else:
                print("{}, You have not typed a valid operator or syntax.".format(user))

            again = input("calculate again? y/n: ")
            if again == "n":
                quit("calculator")
                break

# turtle shapes
    elif software == "/pic":
        pos = t.setpos()
        penup = t.penup()
        pendn = t.pendown()
        draw = t.begin_fill
        color = t.end_fill

        def settings(shape):
            reload(t)
            wn = Screen()
            wn.title(shape, "for {}".format(user))
            wn.clear()
            wn.bgcolor("brown")
            t.pen(pencolor="orange", fillcolor="yellow", pensize=10, speed=5)
      
        while True:
            shape = input("input your shape (quit to exit): ")
            if shape == "circle":
                settings("circle")
                penup()
                pos(-100, 0)
                pendn()
                draw()
                t.circle(200)
                color()
                mainloop()

            elif shape == "square":
                settings("square")
                penup()
                pos(-100, -100)
                pendn()
                draw()
                for start in range(4):
                    t.fd(200)
                    t.lt(90)
                color()
                mainloop()

            elif shape == "triangle":
                settings("triangle")
                penup
                pos(-100, -100)
                pendn
                draw()
                for start in range(4):
                    t.fd(200)
                    t.lt(120)
                color()
                mainloop()

            elif shape == "quit":
                quit("pics")
                break

            else:
                print("please type a valid shape.")

# mini-game(soon)
    elif software == "/game":
        print("soon...")

    elif software == "/time":
        print(strftime("%Y/%m/%d %H:%M")) # strftime shows date and time

    elif software == "/exit":
        exit = input("{} are you sure you want to exit the OS? y/n: ".format(user))
        if exit == "y":
            print("exiting pyOS...")
            break; exit()

    else:
        print('''please type a valid software, {}. 
hint: use /help to see more.'''.format(user))
#finish