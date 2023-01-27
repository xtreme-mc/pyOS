import time

print('''welcome to pyOS computer.
type /help for help.''')

while True:
    def run(software):
        print(software + " opened")
        
    software=input()

    if software == "/help":
        print('''Software commands:
/AI : opens the AI.
/calculator : opens the calculator.
/py-pip : how to install python libraries.
Other commands:
/help : list of commands.
/time : show date and time.
/exit : exit the program.''')

    if software == "/AI":
        print("opening AI...")
        time.sleep(1)
        run("AI")
        
        print("-what's your favorite game ?")
        favgame=input()
        time.sleep(1)
        
        def topic():
            topic=input()
            print(topic)
            time.sleep(1)
            print("-Wow I think It's amazing.")
            time.sleep(1)
            print("-I will try", favgame, "soon.")
        
        print("-do you really like", favgame, "?")
        answer=input()
        time.sleep(1)
        print(answer)

        if "yes" in answer:
            print("-So what's the topic of", favgame, "?")
            topic()

        else:
            print("please write a valid answer.")
            topic()

        time.sleep(1)
        print("-do you have any comments for the AI ?")
        comments=input()

        time.sleep(1)
        print("-thanks for your comments.")

    elif software == "/calculator": 
        print("opening calculator...")
        time.sleep(1)
        run("calculator")

        operation = input('''Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

        a = float(input("Enter your first number: "))
        b = float(input("Enter your second number: "))

        if operation == "+":
            print("{} + {} = ".format(a, b))
            print(a + b)

        elif operation == "-":
            print("{} - {} = ".format(a, b))
            print(a - b)

        elif operation == "*":
            print("{} * {} = ".format(a, b))
            print(a * b)

        elif operation == "/":
            print("{} / {} = ".format(a, b))
            print(a / b)

        else:
            print('''You have not typed a valid operator or syntax, 
            please run the calculator again by using /calculator.''')

    elif software == "/py-pip":
        file = open("README.md", "r")
        print(file.read())
        # "r" will read the file.

    elif software == "/time":
        print (time.strftime("%Y/%m/%d %H:%M"))

    elif software == "/exit":
        break