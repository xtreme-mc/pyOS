from main import *

def generatePw(length):
    global char
    char = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(char, k=length))
    return password

def upgradePw(type):
    letters = string.ascii_letters
    num = string.digits
    punc = string.punctuation
    if not any(word in type for word in letters):
        print("your password should contain at least one letter.")
    elif not any(word in type for word in num):
        print("your password should contain at least one number.")
    elif not any(word in type for word in punc):
        print("your password should contain at least one special character.")
    elif len(type) < 12:
        print("your password should have at least 12 characters.")
    else:
        print("your password is okay!")
        quit(True)

try:
    print(f"generator for {user}")
    while True:
        action = input("type G to generate a random password.\ntype U to upgrade your current password.\n")
        action = action.lower()
        if action == "g":
            while True:
                try:
                    length = int(input("type length of the password: "))
                    break
                except ValueError:
                    continue
            password = generatePw(12)
            print(password)
            quit(True)
        elif action == "u":
            while True:
                upgrade = input("type your current password: ")
                upgradePw(upgrade)

except:
    quit(False)