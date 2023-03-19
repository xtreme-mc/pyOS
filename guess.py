from main import *

def num_choice():
    t.clear()
    t.hideturtle()
    t.penup()
    t.write("loading...", align="center", font=("Arial", 48, "normal"))
    sleep(2)
    t.clear()
    t.goto(0, 50)

    while True:
        num = range(11)
        ran_num = random.choice(num)
        diff = t.textinput("enter difficulty...", "easy, normal, hard, quit")
        diff = diff.lower()

        if diff == "easy":
            attempts = 8
            break
        elif diff == "normal":
            attempts = 5
            break
        elif diff == "hard":
            attempts = 3
            break
        elif diff == "quit":
            quit(True)
        else:
            continue

    while attempts > 0:
        try:
            answer = int(t.textinput("guess number", f"enter a number between 0-10 ({attempts} attempts left)"))
        except ValueError:
            t.clear()
            t.goto(0, 50)
            t.write("please type a number.", align="center", font=("Arial", 16, "normal"))
        
        if answer < ran_num:
            attempts -= 1
            t.clear()
            t.goto(0, 50)
            t.write(f"too low. {attempts} attempts left.", align="center", font=("Arial", 16, "normal"))
        elif answer > ran_num:
            attempts -= 1
            t.clear()
            t.goto(0, 50)
            t.write(f"too high. {attempts} attempts left.", align="center", font=("Arial", 16, "normal"))
        elif answer == ran_num:
            t.clear()
            t.goto(0, 50)
            t.write(f"you win! the number was {ran_num}", align="center", font=("Arial", 16, "normal"))
            t.mainloop()
            break

    t.clear()
    t.goto(0, 50)
    t.write(f"you lose... the number was {ran_num}", align="center", font=("Arial", 16, "normal"))
    t.mainloop()        

try:
    icon()
    t.setup(width=500, height=400)
    t.title(f"guess for {user}")
    num_choice()
    quit(True)
except:
    quit(False)