# Python exception handling - try/except

# 1. Generic

goodInput = False
while (not goodInput):
    try:
        num = int(input("Enter a Number: \n"))
        print(f'You entered {num}')
        goodInput = True
    except:
        # stops the error
        print('you typed in something dumb')

# 2. ValueError (string to int)



# 3. type error



