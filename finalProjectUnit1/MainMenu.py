# this is the main menu

from FinancesMenu import FinancesOption
from LoopMenu import LoopOption
from GradeCalculator import GradeOption
from PersonScript import classesOption
from CastScript import CastOption
from ArrayScript import ArrayOption

print("This it the main menu! please choose one of the following:\n")
userInput = int(input(" 1) Finances\n2) Loop games\n3) Grade Calculator\n4) ID"
" editor\n5) Casting program\n6) Custom arrays\n"))

if(userInput == 1):
    FinancesOption()

elif (userInput == 2):
    LoopOption()

elif(userInput == 3):
    GradeOption()

elif(userInput == 4):
    classesOption()

elif(userInput == 5):
    CastOption()

elif(userInput == 6):
    ArrayOption()

else:
    print("Not a valid option, please try again.")

