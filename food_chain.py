"""

Interactive game with the computer - food chain

The food chain diagram was created based on the photo:
http://uwscienceexplorers.weebly.com/uploads/4/5/3/7/45373667/802b37fe8e9d0814cc5e63fae3fb5e14-orig_orig.jpg

The game consists in selecting an animal that is above the food chain from the available data fields. If the
given animal is the highest, enter the phrase "None", otherwise the player scores 0 points. After collecting
the predetermined 5 points, the game asks the player if he wants to continue the game. Depending on the entered 
name, the program responds by writing to the terminal whether a point has been scored or not

The data acquisition itself has been performed to read from the file. The program is responsible for the correct
reading of data from a file with the ".csv" extension. For its operation, it uses the csv module, which implements
classes to read and write tabular data in CSV format. It allows programmers to say, “write this data in the format
preferred by Excel,” or “read data from this file which was generated by Excel,” without knowing the precise 
details of the CSV format used by Excel.

The game, thanks to the use of a file from which data about animals are loaded, makes it fully modifiable. You can 
add animals making even more different game scenarios.

"""

import csv # The csv module implements classes to read and write tabular data in CSV format. 
import random # Probably the most widely known tool for generating random data in Python is its random module, which uses the Mersenne Twister PRNG algorithm as its core generator.
from animal import *

global foodChain # creating a global variable
foodChain = [] # array of all animals in the food chain 

def readFromDataBase(filePath):
    """
    The method which is using the imported 'csv' library   

    Parameters
    ----------
    filePath : str
        The path to a file containing all animals with their level and specie

    Return
    ----------
    Nothing
        
    """ 
    with open(filePath, newline = '') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',') # extraction of data separated by a delimiter = ','
        for line in reader:
            animal = Animal(line[0],line[1],line[2],line[3]) # reading line from an attached csv file
            foodChain.append(animal) # appending an array

def printAllImportedAnimals():
    """
    Parameters
    ----------
    None

    Return
    ----------
    Prints out all names of loaded animals on the terminal
        
    """ 
    concatenatedStr = "Available animals to choose from: \nLevel 0: "
    currrentAnimalLevel = foodChain[0].getLevel() # saving the level of the first animal to print
    for i in range(0, len(foodChain)):
        if foodChain[i].getLevel() != currrentAnimalLevel: # checking if the level of the animal in the loop has changed
            currrentAnimalLevel = foodChain[i].getLevel() 
            concatenatedStr += "\nLevel " + str(currrentAnimalLevel) + ": " # if so go to new line
        concatenatedStr += foodChain[i].getName()
        if i != (len(foodChain)-1):
            concatenatedStr += ", " # comma separation
    print(concatenatedStr) # printing out concatenated str

def drawRandomAnimal():
    """
    The method which is using the imported 'random' library (uses pseudo-random numbers)

    Parameters
    ----------
    None

    Return
    ----------
    Random animal generated with a pseudorandom number generator from an array of animals
        
    """ 
    numOfRandomAnimal = random.randint(0,(len(foodChain)-1)) # drawing a number from the closed range [0, the number of animals loaded from the file]
    randomAnimal = foodChain[numOfRandomAnimal] # getting animal from the array on position with index numOfRandomAnimal
    return randomAnimal # returns Animal object

if __name__ == "__main__": # __name__ == “main” is used to execute code
    readFromDataBase("./data_base.csv") # passing a file path as an argument
    print('-' * 120) # printing one hundred and twenty times '-'
    """ Writing greetings and instructions to the terminal """
    print("Welcome to the food chain game!!!")
    print("The game is about guessing which animal is higher in the food chain hierarchy")
    print("If drawn animal is at the top of the hierarchy, the user must enter 'None' to get point")
    print("The game has started, to win you need to get 5 points")
    print("Please watch out for upper/lower case and whitespace characters")
    print('-' * 120)
    print('*' * 120) # printing one hundred and twenty times '*'
    printAllImportedAnimals()
    print('*' * 120)
    
    roundCounter = 1
    counter = 0 # variable counting points
    while True: # Infinite loop that can be stopped by the user
        while counter < 5: # loop as long as the number of points is less than 5
            randomAnimal = drawRandomAnimal() # generating a random animal
            print("Please guess which animal is higher in the food chain than: [" + randomAnimal.getName() + "], by entering its name:")
            name = None # pre-allocation
            try:
                name = input() # getting input from the user
            except:
                print("Wrong characters entered, or an illegal key sequence was pressed") # notification of misspelled characters
                continue # restarting the round
            if name == "":
                print("Wrong characters entered, or an illegal key sequence was pressed") # notification of misspelled characters
                continue
            
            flag = False # flag checking whether a given input is in the consumers
            consumers = randomAnimal.getConsumers()
            for element in consumers:
                if element == name: # str comparison
                    flag = True # if an identical name is found, set a flag

            if flag:
                counter += 1 # incrementing counter
                print("+++ Congratulations, you guessed it!, your current score is: " + str(counter)) # notification in case of success
                print("Chosen animal was a: " + randomAnimal.getSpecie() + ", with a level in food chain of: " + str(randomAnimal.getLevel()))
            else: 
                print("!!! I'm sorry but that's the wrong answer, please try again in the next turn, your current score is: " + str(counter)) # notification in case of loss

        print('#' * 120) # printing one hundred and twenty times '*'
        print("Well done, you won! Do you want to continue (if so, press (y / Y), if not, press any other key")
        try:
            key = input() # character responsible for interrupting the game
            if(key=="Y" or key=="y"):
                print("\n\n\n")
                counter = 0 
                print("Starting new round with number: " + str(roundCounter))
                roundCounter += 1
                print('#' * 120)
                continue # continue iterating if the user wants to continue playing
            else:
                break # break the loop if the user does not want to continue playing
        except:
            print("Wrong characters entered, or an illegal key sequence was pressed") # notification of misspelled characters
            break # break the loop if the user entered any wrong input