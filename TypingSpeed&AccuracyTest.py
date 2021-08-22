# This program asks the user to type a given word 5 times as fast as possible and tracks time taken and errors
import matplotlib.pyplot as plot
import time, random
import requests as req

def startTyping():
    times = []
    mistakes = 0
    while len(times) < 5:

        start = time.time()
        wordAttempt = input("Type the word: ")
        end = time.time()
        timeElapsed = end - start
        times.append(timeElapsed)
        if (wordAttempt.lower() != word):
            mistakes += 1

    return times, mistakes

# Dictionary Source
r = req.get("https://www.mit.edu/~ecprice/wordlist.10000") 

# Converting returned string into a list
wordsList = r.text.split() 

# Random word selection
word = wordsList[random.randint(0, len(wordsList))]

print("Your goal is to type the word, " + word + " 5 times as fast as you can. \nReady to begin (y/n)?")

while(True):
    gameBool = input().lower()
    if(gameBool == "y"):
        timeTaken, mistakesMade = startTyping()
        print("You have made " + str(mistakesMade) + " mistake(s). \nLets see how well you performed.")
        break 

    elif(gameBool == "n"):
        quit()
    
    else:
        print("Invalid response. Acceptable inputs: (y/n)")
    

# Plotting Data
x = [1,2,3,4,5]
y = timeTaken
legend = ["1", "2", "3", "4", "5"]
plot.plot(x,y)
plot.xticks(x, legend)
plot.ylabel("Time in seconds (s)")
plot.xlabel("Attempts")
plot.title("Typing Evolution")
plot.show()