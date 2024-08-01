import random

'''
rock = 1
paper = -1
scissors = 0
'''

computer = random.choice([1, -1, 0])
user_input = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ")
dict = {"r": 1, "p": -1, "s": 0}
reversDict = {1: "Rock", -1:"Paper", 0:"Scissors"}

you = dict[user_input]


print(f"You chose {reversDict[you]}\nComputer chose {reversDict[computer]}")


if(computer==you):
    print("Its a draw")

else:
    if(computer == 1 and you ==-1):
        print("You Win!")

    elif(computer ==1 and you ==0):
        print("You Lose!")

    elif(computer ==-1 and you ==0):
        print("You Win!")

    elif(computer ==-1 and you ==1):
        print("You Lose!")

    elif(computer ==0 and you ==1):
        print("You Win!")

    elif(computer ==0 and you ==-1):
        print("You Lose!")

    else:
        print("Something went wrong!")
  