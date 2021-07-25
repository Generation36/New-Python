#Objective Guess the Correct Number in as few attempts possible
import random
import sys

#Function declarations
def startGameSequence():
    secretNum = random.randint(1,10)
    print(secretNum)

    #prompts player to take a guess
    print("I am thinking of a number between 1 and 10.\nYou have 3 guesses.")
    numGuesses = 3
    for x in range (0,3):
        playersGuess = input()

        if playersGuess == secretNum:
            print("Congratulations! You guessed the right number!")

        elif playersGuess != secretNum:
            numGuesses -= 1;
            print("I'm sorry, try again.\nYou have " + str(numGuesses) +" left.")
            
            if numGuesses == 0:
                print("I'm sorry you lost. Better luck next time.")

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

    else:
        print("Invalid Entry. Please enter a Y or N.")
        init = input()






