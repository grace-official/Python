#menu for the loops
from highLow import HighLowOption
from GuessingGame import GuessOption

def LoopOption():
    # this is a sub menu for the loop themed scripts
    print("Thank you for selecting Loop Programs! please choose one of the following:\n")
    userInput = int(input(" 1) high Low\n 2) Guessing Game \n"))

    if (userInput == 1):
        HighLowOption()

    elif (userInput == 2):
        GuessOption()

    else:
        print("Not a valid option, please try again.")
