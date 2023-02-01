from turtle import *
import time
import math
import random
import pygame

user = input("please input your name to start the OS: ")
print(user)

print('''welcome to pyOS, {}.
type /help for help.'''.format(user))

while True:
    def run(app):
        print("opening {} for {}...".format(app, user))
        wait(1)
        print("{} opened successfully.".format(app))
    def wait(seconds):
        time.sleep(seconds)

    software=input()

    if software == "/help":
        print('''OS commands:
/ai : opens the game AI.
/calc : opens the calculator.
/pic : draws a circle in turtle.
Other commands:
/help : list of commands.
/time : show date and time.
/exit : exit the program.''')

    if software == "/ai":
        def topic():
            topic=input()
            print(topic)
            wait(1)
            print("-Wow I think It's amazing.")
            wait(1)
            print("-I will try {} soon.".foramt(favgame))

        print("opening AI...")
        wait(1)
        run("AI")
        
        print("-what's your favorite game ?")
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
        print("-thanks for your comments.")

    elif software == "/calc": 
        print("opening calculator...")
        wait(1)
        run("calculator")
        
        while True:

            operation = input('''Please type the math operation you'd like to complete:
+ : addition
- : subtraction
* : multiplication
/ : division
% : modulo
sqrt : square root''')

            if operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == "%":
                a = float(input("Enter your first number: "))
                b = float(input("Enter your second number: "))

                if operation == "+":
                    print("{} + {} = ".format(a, b))
                    try:
                        print(a + b)
                    except:
                        print("please use a number.")

                elif operation == "-":
                    print("{} - {} = ".format(a, b))
                    try:
                        print(a - b)
                    except:
                        print("please use a number.")

                elif operation == "*":
                    print("{} * {} = ".format(a, b))
                    try:
                        print(a * b)
                    except:
                        print("please use a number.")                

                elif operation == "/":
                    print("{} / {} = ".format(a, b))
                    try:
                        print(a / b)
                    except:
                        print("please use a number.")

                elif operation == "%":
                    print("{} % {} = ".format(a,b))
                    try:
                        print(a % b)
                    except:
                        print("please use a number.")

            elif operation == "sqrt":
                x = float(input("Enter your number: "))

                print("sqrt({}) = ".format(x))
                print(math.sqrt(x))
            
            else:
                print('''You have not typed a valid operator or syntax, 
please run the calculator again by using /calc.''')

    elif software == "/pic":
        run("turtle")

        Screen()
        title("Pictures")
        setpos(0, -100)
        clear()
        bgcolor("brown")
        pen(pencolor="orange", fillcolor="yellow", pensize=10, speed=5)
        begin_fill()
        circle(200)
        end_fill()
        mainloop()
    
    elif software == "/game":
        print("soon...")

    elif software == "/time":
        print(time.strftime("%Y/%m/%d %H:%M"))

    elif software == "/exit":
        break; exit()