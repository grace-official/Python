# casting program

def CastOption():
    # getters for data
    dataInput = type(input("please enter the data you want to convert: \n"))
    userInput = int(input("Select the type you wish to convert to: \n 1) String\n 2) Bool\n 3) float\n 4) int\n"))

    # converters
    if userInput < 0 or userInput >= 5:
        print("invalid input, please try again")

    elif(userInput == 1):
        print("OK! That is now a String!")
        dataInput = str
        print(dataInput)

    elif(userInput == 2):
        dataInput = True
        print("OK! That is now a Boolean!")
        print(dataInput)

    elif(userInput == 3):
        dataInput = float
        print("OK! That is now a Float!")
        print(dataInput)

    elif(userInput == 4):
        dataInput = int
        print("OK! That is now an Int!")
        print(dataInput)

