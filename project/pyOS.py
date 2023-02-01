# libraries and modules
from turtle import *
from time import *
from math import *
import random
import pygame

# main script
user = input("please input your name to start the OS: ")
print('''welcome to pyOS, {}.
type /help for help.'''.format(user))

while True:
    def run(app):
        print("opening {} for {}...".format(app, user))
        wait(1)
        print("{} opened successfully.".format(app))
    def quit(app):
        print("{} quited successfully.".format(app))
    def wait(seconds):
        sleep(seconds)

    software=input()

    if software == "/help":
        print('''commands for {}:
OS commands:
/ai : opens the game AI.
/calc : opens the calculator.
/pic : draws a circle in turtle.
other commands:
/help : list of commands.
/time : show date and time.
/exit : exit the program.'''.format(user))

    if software == "/ai":
        def topic():
            topic=input()
            print(topic)
            wait(1)
            print("-Wow I think It's amazing, {}.".format(user))
            wait(1)
            print("-I will try {} soon.".foramt(favgame))

        run("AI")
        
        print("-what's your favorite game, {} ?".format(user))
        favgame=input()
        wait(1)
        
        print("-do you really like {} ?".format(favgame))
        answer=input()
        wait(1)
        print(answer)

        if "yes" in answer:
            print("-So what's the topic of {} ?".format(favgame))
            topic()

        else:
            print("please write a valid answer.")
            topic()

        wait(1)
        print("-do you have any comments for the AI ?")
        comments=input()

        wait(1)
        print("-thanks for your comments, {}.".format(user))

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
                try:  
                    a = float(input("Enter your first number: "))
                    b = float(input("Enter your second number: "))
                except:
                    print("please use a float.")

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

            again = input("calculate again? y/n")
            if again == "n":
                quit("calculator")
                break

    elif software == "/pic":
        run("turtle")
        def settings():
            clear()
            bgcolor("brown")
            pen(pencolor="orange", fillcolor="yellow", pensize=10, speed=5)
            begin_fill()

        def right(go):
                setheading(90)
                forward(go)

        def left(go):
            setheading(270)
            forward(go)
            
            
        def down(go):
            setheading(180)
            forward(go)
            
        def up(go):
            setheading(0)
            forward(go)

        shape = input("input your shape: ")
        if shape == "circle":   
            Screen()
            title("circle")
            penup()
            setpos(0, -100)
            pendown()
            settings()
            circle(200)
            end_fill()
            mainloop()
        elif shape == "square":
            Screen()
            title("square")
            penup()
            setpos(-100, -100)
            pendown()
            settings()
            right(200)
            up(200)
            left(200)
            down(200)
            end_fill()
            
            mainloop()

    elif software == "/game":
        print("soon...")

    elif software == "/time":
# strftime can be used in a string : %Y, %m, d%, %H, %M, %p
        print(strftime("%Y/%m/%d %H:%M"))

    elif software == "/exit":
        break; exit()
#finish