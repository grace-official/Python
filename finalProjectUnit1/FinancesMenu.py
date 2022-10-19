# menu for finances
from Banking import BankOption
from TaxCalculator import TaxOption

def FinancesOption():
    # this is a sub menu for Finances themed scripts
    print("Thank you for selecting finances! please choose one of the following:\n")
    userInput = int(input(" 1) Banking\n 2) Tax Calculator \n"))

    if(userInput == 1):
        BankOption()

    elif (userInput == 2):
        TaxOption()

    else:
        print("Not a valid option, please try again.")
