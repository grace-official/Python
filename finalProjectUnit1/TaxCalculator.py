# Sales Tax Calculator
def TaxOption():
    # getter for tax
    countryTax = float(input("Enter your countries tax below: \n"))

    # Item value
    itemPrice = float(input("Enter the price of the item you're calculating: \n"))

    # real tax number
    realTax = countryTax / 100

    # tax calculations
    salesTax = realTax * itemPrice

    # calculating final price
    finalPrice = itemPrice + salesTax

    print("\n~~~~~~~~~~calculating~~~~~~~~~~")
    print("The price of your item is: ${:,.2f}".format(itemPrice))
    print("The price of tax is: ${:,.2f}".format(realTax))
    print("The price of your sales tax is: ${:,.2f}".format(salesTax))
    print("The price of your item plus tax is: ${:,.2f}".format(finalPrice))

