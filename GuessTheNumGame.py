#Objective Guess the Correct Number in as few attempts possible
import random
import sys

#Function declarations
def startGameSequence():
    secretNum = random.randint(1,10)
    print(secretNum)

    #prompts player to take a guess
    print("I am thinking of a number between 1 and 10.\nYou have 3 guesses.")
    playersGuess = input()


#Greeting Message 
print("Hello! What is your name?")
name = input()

print("It is nice to meet you " + name + "!")
print("Would you like to play a game? (Y/N)")
init = input()

#Conditional Flow Control
while init:
    if init == "Y" or "y":
        startGameSequence()
        break

    elif init == "N" or "n":
        sys.exit()

    elif init != "Y" or "N" or "y" or "n":
            print("Invalid Entry. Please enter a Y or N.")
            init = input()






