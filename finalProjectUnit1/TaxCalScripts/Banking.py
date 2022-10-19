# bank balance checker
def BankOption():
    # getter for bank balance
    totalBalance = float(input("Enter your bank balance below: \n"))

    # Item value
    itemPrice = float(input("Enter the price of the item you wish to buy: \n"))

    # calculating the amount you can purchase
    totalAmount = totalBalance / itemPrice

    print("\n~~~~~~~~~~calculating~~~~~~~~~~")
    print("The amount of items you can buy is: {:,.2f}".format(totalAmount))

