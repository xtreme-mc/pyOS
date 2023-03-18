from main import *

software = "guess"
def num_choice():
    t.title(f"guess for {user}")
    icon()
    t.clear()
    t.hideturtle()
    t.bgcolor("brown")
    t.pencolor("yellow")
    t.penup()
    t.write("Loading...", align="center", font=("Arial", 48, "normal"))
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

    while attempts > 0:
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

        t.clear()
        t.goto(0, 50)
        t.write(f"You lose... The number was {ran_num}", align="center", font=("Arial", 16, "normal"))
        t.mainloop()        

try:
    num_choice()
    quit(True)
except:
    quit(False)