'''
menu = {"Burger", "Fries", "Pop", "Pancakes"}

for food in menu:
    print(food)
'''

'''
for num in range(99, 0, -1):
    print(str(num) + " Bottles of beer on the wall," + str(num) + " bottles of beer, Take one down and pass it around...")
'''

'''
limit = 100
while 1 < 2:
    limit-=1
    print("Hello! This will run " + str(limit) + (" times!") )
    if(limit == 0):
        break

print("Loop Finished")
'''

goodInput = False

while not goodInput:
    userInput = int(input("1) Start Game  \n2) Load Game  \n3) Quit Game"))
    if(userInput == 1):
        print("Game Started!")
        goodInput = True
    elif(userInput == 2):
        print("Game Loaded!")
        goodInput = True
    elif(userInput == 3):
        print("Bye!")
        goodInput = True
    else:
        print("Invalid Input, Please try again!")
