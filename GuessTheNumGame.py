#Objective Guess the Correct Number in as few attempts possible
import random
import sys

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

while init:
    if init == "Y":
        startGameSequence()
        break

    elif init == "N":
        sys.exit()

    elif init != "Y" or "N":
            print("Invalid Entry. Please enter a Y or N.")
            init = input()






