# Sales Tax Calculator

'''
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
'''

def calculate_sales_tax(tax_rate, item_price):
    """
    Calculates the sales tax and final price for an item given the tax rate and the price of the item.

    Parameters:
    tax_rate (float): The tax rate for the item, as a decimal.
    item_price (float): The price of the item.

    Returns:
    tuple: A tuple containing the sales tax and final price, rounded to the nearest cent.
    """
    try:
        tax_rate = float(tax_rate)
        item_price = float(item_price)
    except ValueError:
        return (0, 0)

    real_tax_rate = tax_rate / 100
    sales_tax = round(real_tax_rate * item_price, 2)
    final_price = round(item_price + sales_tax, 2)

    return (sales_tax, final_price)

    print("\n~~~~~~~~~~calculating~~~~~~~~~~")
    print("The price of your item is: ${:,.2f}".format(item_price))
    print("The price of tax is: ${:,.2f}".format(real_tax_rate))
    print("The price of your sales tax is: ${:,.2f}".format(sales_tax))
    print("The price of your item plus tax is: ${:,.2f}".format(final_price))

input_str = input("Enter the tax rate and price of the item, separated by a comma: \n")
tax_rate, item_price = input_str.split(',')
calculate_sales_tax(tax_rate, item_price)
