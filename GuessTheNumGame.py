#Objective Guess the Correct Number in as few attempts possible

import random

#Function declarations
def startGameSequence():
    secretNum = random.randint(1,10)
    print("I am thinking of a number between 1 and 10.")

#Greeting Message 
print("Hello! What is your name?")

name = input()

print("It is nice to meet you " + name + "!")
print("Would you like to play a game? (Y/N)")

init = input()

if init == "Y":
    startGameSequence()

elif init == "N":
    exit()

elif init == "":
    print("Invalid Entry. Please enter a Y or N.")






