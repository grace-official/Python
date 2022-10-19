# guessing game
import random

def GuessOption():

    # program picks a num between 1-100
    randomNumber = random.randint(1, 100)
    guess = 0
    # determines if your guess was right
    while guess != randomNumber:
        guess = int(input("Guess a number between 1 and 100! : \n"))

        if (guess < randomNumber):
            print("That guess is too low, try again!")
        elif (guess > randomNumber):
            print("That's too high! Try again!")
        else:
            print("You win!")
