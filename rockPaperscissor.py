import random

userChoice = input("choose rock or paper or scissor: ")

rps = ["rock", "paper", "scissor"]
randNum = random.randint(0,3)

# Computer section
compChoice = rps[randNum]

#Compare
print("You choose: ", userChoice)
print("computer choose: ", compChoice) 

# rock vs compChoice
if userChoice == rps[0]:
    if compChoice == rps[0]:
        print("DRAW")
    elif compChoice == rps[1]:
        print("COMP WINS")
    else:
        print("YOU WIN")
        # paper vs compChoice
elif userChoice == rps[1]:
    if compChoice == rps[0]:
        print("COMP WINS")
    elif compChoice == rps[1]:
        print("DRAW")
    else:
        print("YOU WIN")
        # scissor vs compChoice
else:
    if compChoice == rps[0]:
        print("COMP WINS!")
    elif compChoice == rps[1]:
        print("YOU WIN!")
    else:
        print("DRAW")




