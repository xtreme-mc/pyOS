# used modules
from turtle import Screen, title, mainloop
from time import sleep, strftime
from math import sqrt
import turtle
import random
import pygame

# main script
user = input("please input your name to start the OS: ")
print("starting...")
sleep(1)
print('''welcome to pyOS V1.0.0, {}.
type /help for help.'''.format(user))

while True:
    def run(app):
        print("opening {} for {}...".format(app, user))
        sleep(1)
        print("{} opened successfully.".format(app))

    def quit(app):
        print("{} quited successfully.".format(app))

    software=input()

    if software == "/help":
        print('''commands for {}:
OS commands:
/ai : opens Xtreme AI.
/calc : opens the calculator.
/pic : draws a picture in turtle.
other commands:
/help : list of commands.
/time : show date and time.
/exit : exit the program.'''.format(user))

# Xtreme AI
    if software == "/ai":
        run("Xtreme AI")
        print('''welcome to Xtreme AI, {}.
type "quit" to quit the app.'''.format(user))

        while True:
            print("-what's your favorite game, {} ?".format(user))
            favgame=input()
            if favgame == "quit":
                break

            sleep(1)

            print("-what's the topic of {} ?".format(favgame))
            input()
            if input() == "quit":
                break

            print("-Wow I think It's amazing, {}.".format(user))
            sleep(1)
            print("-I will try {} soon.".format(favgame))
            sleep(1)

            print('''thank for trying our AI.
see you soon {} !'''.format(user)); break
      
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
                        print("sqrt({}) = ".format(c))
                        print(sqrt(c))
                    except:
                        print("please use a float.")

            elif operation == "abs":
                    try:
                        c = float(input("Enter your number: "))
                        print("abs({}) = ".format(c))
                        print(abs(c))
                    except:
                        print("please use a float.")

            elif operation == "quit":
                quit("calculator")
                break

            else:
                print('''{}, You have not typed a valid operator or syntax, 
please run the calculator again by using /calc.'''.format(user))

            again = input("calculate again? y/n: ")
            if again == "n":
                quit("calculator")
                break

# turtle shapes
    elif software == "/pic":
        run("turtle")
        def settings(window):
            Screen()
            title(window)
            turtle.setpos(0, 400)
            turtle.write(window, align = "center", font = 50 )

            turtle.clear()
            turtle.bgcolor("brown")
            turtle.pen(pencolor="orange", fillcolor="yellow", pensize=10, speed=5)

        def position(x, y):
            turtle.penup()
            turtle.setpos(x, y)
            turtle.pendown()

        def move(go, angle):
            turtle.setheading(angle)
            turtle.forward(go)
      
        while True:
            shape = input("input your shape: ")

            if shape == "circle":
                settings("circle")
                position(0, -100)
                
                turtle.begin_fill()
                turtle.circle(200)
                turtle.end_fill()

                mainloop()

            elif shape == "square":
                settings("square")
                position(-100, -100)
                
                turtle.begin_fill()
                move(200, 90)
                move(200, 0)
                move(200, 270)
                move(200, 180)
                turtle.end_fill()

                mainloop()

            elif shape == "triangle":
                settings("triangle")
                position(0, 0)

                turtle.begin_fill()
                move(200, 120)
                move(200 ,240)
                move(200 ,360)

                turtle.end_fill()

                mainloop()

            elif shape == "quit":
                break

            else:
                print("please type a shape.")

# mini-game(soon)
    elif software == "/game":
        print("soon...")

    elif software == "/time":
# strftime shows date and time
        print(strftime("%Y/%m/%d %H:%M"))

    elif software == "/exit":
        break; exit()
#finish