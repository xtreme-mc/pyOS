# used modules
from turtle import Screen, title, mainloop
from time import sleep, strftime
from math import sqrt
import turtle
import random
import pygame

# main script
user = input("please input your name to start the OS: ")
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
        def topic():
            topic=input()
            print(topic)
            sleep(1)
            print("-Wow I think It's amazing, {}.".format(user))
            sleep(1)
            print("-I will try {} soon.".format(favgame))

        run("Xtreme AI")
        
        print("-what's your favorite game, {} ?".format(user))
        favgame=input()
        sleep(1)
        
        print("-do you really like {} ?".format(favgame))
        answer=input()
        sleep(1)
        print(answer)

        if "yes" in answer:
            print("-So what's the topic of {} ?".format(favgame))
            topic()

        else:
            print("please write a valid answer.")
            topic()

        sleep(1)
        print("-do you have any comments for the AI ?")
        comments=input()

        sleep(1)
        print("-thanks for your comments, {}.".format(user))

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
abs : absolute number
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
                        x = float(input("Enter your number: "))
                        print("sqrt({}) = ".format(x))
                        print(sqrt(x))
                    except:
                        print("please use a float.")

            elif operation == "abs":
                    try:
                        x = float(input("Enter your number: "))
                        print("abs({}) = ".format(x))
                        print(abs(x))
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
        def settings():
            turtle.clear()
            turtle.bgcolor("brown")
            turtle.pen(pencolor="orange", fillcolor="yellow", pensize=10, speed=5)
            turtle.begin_fill()

        def right(go):
                turtle.setheading(90)
                turtle.forward(go)

        def left(go):
            turtle.setheading(270)
            turtle.forward(go)
            
            
        def down(go):
            turtle.setheading(180)
            turtle.forward(go)
            
        def up(go):
            turtle.setheading(0)
            turtle.forward(go)

        shape = input("input your shape: ")
        
        if shape == "circle":
            Screen()
            title("circle")
            turtle.penup()
            turtle.setpos(0, -100)
            turtle.pendown()
            settings()
            turtle.circle(200)
            turtle.end_fill()
            mainloop()

        elif shape == "square":
            Screen()
            title("square")
            turtle.penup()
            turtle.setpos(-100, -100)
            turtle.pendown()
            settings()
            right(200)
            up(200)
            left(200)
            down(200)
            turtle.end_fill()

            mainloop()

# mini-game(soon)
    elif software == "/game":
        print("soon...")

    elif software == "/time":
# strftime shows date and time
        print(strftime("%Y/%m/%d %H:%M"))

    elif software == "/exit":
        break; exit()
#finish