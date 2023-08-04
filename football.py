from main import *
import random

gk = "goalkeeper"
df = "defender"
mf = "midfielder"
fw = "forward"

barcelona = "FC Barcelona"
realmadrid = "Real Madrid CF"
seville = "Seville"
liverpool = "Liverpool FC"
mancity = "Manchester City"
manunited = "Manchester United"
arsenal = "Arsenal"
inter = "Internazionale"
paris = "Paris Saint-Germain"
bayern = "Bayern Munchen"

while True:
    team = input("choose your team: barcelona, realmadrid, seville, liverpool, mancity, manunited, arsenal, inter, paris, bayern\n")

    if team == "barcelona":
        team = barcelona
        break
    elif team == "realmadrid":
        team = realmadrid
        break
    elif team == "seville":
        team = seville
        break
    elif team == "liverpool":
        team = liverpool
        break
    elif team == "mancity":
        team = mancity
        break
    elif team == "manunited":
        team = manunited
        break
    elif team == "arsenal":
        team = arsenal
        break
    elif team == "inter":
        team = inter
        break
    elif team == "paris":
        team = paris
        break
    elif team == "bayern":
        team = bayern
        break
    else:
        print("please type a valid team.")

print("")
time.sleep(1)
print(f"your team is {team}\nleague starts!\nfirst 2 will be qualified to the semi-final.\nthe last 2 will be eliminated!\nthe others will play against each other to gain points.\nthe 2 with the most points qualify!\nlet's go!\n")
time.sleep(1)