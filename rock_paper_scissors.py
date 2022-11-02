import random

choices = ["rock","paper","scissors"]

def GameStart():
    while True:
        print("welcome, we play rock, paper, scissors! Rock beats scissors, which beat paper that beats the rock.")
        a = input("pick a choice: rock, paper or scissors: ")
        b = random.choice(choices)
        print("I choose: " + b)

        if a == b:
            print("it is a draw!")
        elif (a == "rock" and b == "scissors") or (a == "scissors" and b == "paper") or (a == "paper" and b == "rock"):
            print("you win")
        else:
            print("I win")




GameStart()