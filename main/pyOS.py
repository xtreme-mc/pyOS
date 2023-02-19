# This project is created by Xtreme MC Studios.
# This is a simulator, not an Operating System.
# Visit us: https://youtube.com/@xtrememc8661.

from time import sleep, strftime
from random import choice
from math import sqrt, pi
import turtle as t

#username
while True:
    user = input("please input your name to start the OS: ")
    if user == "":
        print("please type a valid name.")
    else:
        print("starting...")
        sleep(1)
        print(f"welcome to pyOS, {user}.\ntype help for help.")
        break

#app icon
def icon():
    root = t.getcanvas()._root()
    root.iconbitmap("main\logo-pyOS.ico")

#run app
def run():
    print(f"opening {software} for {user}...")
    sleep(1)
    print(f"{software} opened successfully.")

#quit app
def quit():
    print(f"{software} quited successfully.")
    print("enter the name of app you want to open.\nneed help? type help.")

#app error
def error():
    print(f"an error occured in {software}.")
    print(f"quitting {software}...")
    sleep(1)
    quit()

while True:
    software=input()

#help
    if software == "help":
        print(f"commands for {user}:\nhelp : list of apps.\ncalc : open the calculator.\ndraw : draw a picture in another window.\ntime : show date and time.\nguess : guess the number.\nexit : exit the program.")

#calculator
    elif software == "calc": 
        run()
        
        while True:
            operation = input("Please type the math operation: +, -, *, /, sqrt or quit: ")

            if operation == "+": #add
                while True:
                    try:
                        a = float(input("Enter your first number: "))
                        b = float(input("Enter your second number: "))
                        print(f"{a} + {b} = {a + b}")
                        break
                    except:
                        print("please use a number.")

            elif operation == "-": #sub
                while True:
                    try:
                        a = float(input("Enter your first number: "))
                        b = float(input("Enter your second number: "))
                        print(f"{a} - {b} = {a - b}")
                        break
                    except:
                        print("please use a number.")

            elif operation == "*": #multiply
                while True:
                    try:
                        a = float(input("Enter your first number: "))
                        b = float(input("Enter your second number: "))
                        print(f"{a} * {b} = {a * b}")
                        break
                    except:
                        print("please use a number.")                

            elif operation == "/": #div
                while True:
                    try:
                        a = float(input("Enter your first number: "))
                        b = float(input("Enter your second number: "))
                        print(f"{a} / {b} = {a / b}")
                        break
                    except:
                        print("please use a number.")

            elif operation == "%": #mod
                while True:
                    try:
                        a = float(input("Enter your first number: "))
                        b = float(input("Enter your second number: "))
                        print(f"{a} % {b} = {a % b}")
                        break
                    except:
                        print("please use a number.")

            elif operation == "sqrt": #sqrt
                while True :
                    try:
                        c = float(input("Enter your number: "))
                        result = sqrt(abs(c))
                        print(f"√{c} = {result}")
                        break
                    except:
                        print("please use a number.")

            elif operation == "quit": #quit
                quit()
                break

            else: #invalid
                print(f"{user}, You have not typed a valid operator or syntax.")

#calculate again
            calc_again = input("calculate again? y/n: ")
            if calc_again == "n":
                quit()
                break

#draw shapes
    elif software == "draw":
        run()
        icon()
        t.title(f"draw for {user}")
        
        def shape_cir(): #circle
            dm = 200
            ray = dm / 2
            s = ray * ray * pi
            out = dm * pi

            t.clear()
            t.bgcolor("brown")
            t.pencolor("orange")
            t.fillcolor("yellow")
            t.speed(3)
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.begin_fill()
            t.circle(dm)
            t.end_fill()
            print(f"user: {user}\nshape: {shape}\nsurface: {s}\ndiameter: {dm}\noutline: {out}")

        def shape_squ(): #square
            line = 200
            s = line * line
            dm = line * sqrt(2)
            out = line * 4

            t.clear()
            t.bgcolor("brown")
            t.pencolor("orange")
            t.fillcolor("yellow")
            t.speed(3)
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.begin_fill()
            for i in range(4):
                t.fd(line)
                t.lt(90)
            t.end_fill()
            print(f"user: {user}\nshape: {shape}\nsurface: {s}\ndiameter: {dm}\nlateral: {line}\noutline: {out}")

        def shape_tri(): #triangle
            type = "equilateral"
            base = 200
            ht = base * (sqrt(3)/2)
            s = base * ht / 2
            out = base * 3

            t.clear()
            t.bgcolor("brown")
            t.pencolor("orange")
            t.fillcolor("yellow")
            t.speed(3)
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.begin_fill()
            for i in range(3):
                t.fd(200)
                t.lt(120)
            t.end_fill()
            print(f"user: {user}\nshape: {shape}\nsurface: {s}\ntype: {type}\nbase: {base}\nheight: {ht}\noutline: {out}")

        def shape_rec(): #rectangle
            ht = 400
            width = 200
            s = ht * width
            dm =  sqrt(ht*ht + width*width)
            out = (width+ht) * 2

            t.clear()
            t.bgcolor("brown")
            t.pencolor("orange")
            t.fillcolor("yellow")
            t.speed(3)
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.begin_fill()
            for i in range(2):
                t.fd(400)
                t.lt(90)
                t.fd(200)
                t.lt(90)
            t.end_fill()
            print(f"user: {user}\nshape: {shape}\nsurface: {s}\ndiameter: {dm}\nheight: {ht}\nwidth: {width}\noutline: {out}")

        try:
            while True:
                shape = t.textinput("Enter your shape" ,"Type quit to exit:")

                if shape == "circle":
                    shape_cir()

                elif shape == "square":
                    shape_squ()

                elif shape == "triangle":
                    shape_tri()

                elif shape == "rectangle":
                    shape_rec()         

                elif shape == "quit": #quit
                    t.bye()
                    quit()
                    break

                else: #invalid
                    t.clear()
                    t.penup()
                    t.goto(0, 50)
                    t.write("please type a valid shape.", align = "center", font = ("Arial", 16, "normal"))

                t.goto(0,0)
                t.penup()
                draw_again = t.textinput("draw again ?", "type y/n:")
                if draw_again == "n":
                    t.bye()
                    quit()
                    break

        except:
            t.bye()
            error()
            quit()

#guess
    elif software == "guess":
        def num_choice():
            t.title(f"VIP Guess for {user}")
            icon()

            t.clear()
            t.hideturtle()
            t.bgcolor("brown")
            t.pencolor("yellow")
            t.penup()
            t.write("Loading...", align="center", font=("Arial", 16, "normal"))
            sleep(2)
            t.clear()
            t.goto(0, 50)

            while True:
                num = range(11)
                ran_num = choice(num)
                diff = t.textinput("Enter difficulty...", "easy/normal/hard/insane/impossible")

                if diff == "easy":
                    attempts = 8
                    break
                
                elif diff == "normal":
                    attempts = 5
                    break

                elif diff == "hard":
                    attempts = 3
                    break

                elif diff == "insane":
                    attempts = 2
                    break

                elif diff == "impossible":
                    attempts = 1
                    break

                else:
                    t.write("Please type a difficulty.", align="center", font=("Arial", 16, "normal"))
            
            while True:
                try:
                    answer = int(t.textinput("Guess number...", f"Enter a number between 0-10 ({attempts} attempts left)"))
                except:
                    t.clear()
                    t.goto(0, 50)
                    t.write("Please type a number.", align="center", font=("Arial", 16, "normal"))
                
                if answer < ran_num:
                    attempts -= 1
                    t.clear()
                    t.goto(0, 50)
                    t.write(f"Too low. {attempts} attempts left.", align="center", font=("Arial", 16, "normal"))

                elif answer > ran_num:
                    attempts -= 1
                    t.clear()
                    t.goto(0, 50)
                    t.write(f"Too high. {attempts} attempts left.", align="center", font=("Arial", 16, "normal"))

                elif answer == ran_num:
                    t.clear()
                    t.goto(0, 50)
                    t.write(f"You win! The number was {ran_num}", align="center", font=("Arial", 16, "normal"))
                    t.mainloop()
                    break

                if attempts == 0:
                    t.clear()
                    t.goto(0, 50)
                    t.write(f"You lose... The number was {ran_num}", align="center", font=("Arial", 16, "normal"))
                    t.mainloop()
                    break         
            
        try:
            run()
            num_choice()
            quit()

        except:
            error()

#time
    elif software == "time":
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

        try:
            run()
            clock()
            quit()
        except:
            error()

#exit OS
    elif software == "exit":
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