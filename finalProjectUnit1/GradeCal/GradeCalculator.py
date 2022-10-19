def GradeOption():
    for i in range(0, 100):

        # getting grade percentage
        grade = int(input("What is your grade percentage? \n"))

        # determines letter grade
        if grade < 0 or grade > 100:
            print("Uhh.. I don't think that's possible. Please try again. \n")

        elif grade <= 100 and grade >= 86:
            print("Congrats! you are getting an A!")

        elif grade <= 85 and grade >= 73:
            print("Doing good! you are getting a B!")

        elif grade <= 72 and grade >= 67:
            print("You are getting a C+, could be better, but still good!")

        elif grade <= 66 and grade >= 60:
            print("You are getting a C, better start studying!")

        elif grade <= 59 and grade >= 50:
            print("Uh Oh! You're getting a C-!")

        elif grade <= 49 and grade >= 0:
            print("Oh No! You're Failing!  :(")

        else:
            break

