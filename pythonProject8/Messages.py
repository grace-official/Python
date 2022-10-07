class ChatBot:
    # Class variable - this will have the same value for EVERY OBJECT
    myName = 'PlaceHolder'

    def __init__(self, aiName):
        #print('ChatBot has been created!')
        self.aiName = aiName # instance variable

    def printMyName(self):
        # print(myName)
        print('No name yet... ')

    def printAiName(self):
        print(self.aiName)

    def rememberMyName(self, name):
        ChatBot.myName = name

