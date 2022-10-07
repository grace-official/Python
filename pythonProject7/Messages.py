class ChatBot:

    # Constructor - sets up the initial state of my object
    def __init__(self):
        print('ChatBot has been created!')

    # Type 1 - No argument, no return
    def printMessage(self):
        print('Hello World!')

    # Type 2 - Argument, no return
    def sayHiToMe(self, name):
        print(f'Hello, {name}')

'''
    # Type 3 - No argument, return
    def SendSecretMessage(self):
        return 'do you think rats have tiny 7/11s?'

    # Type 4 - Argument and return
    def doMyHomework(self, numOne, numTwo):
        print("Ok, I'm happy to help with that")
        return numOne + numTwo
'''