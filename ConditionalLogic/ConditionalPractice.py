# Python Conditional Logic
# if, elif (Else If), and else

age = int(input('How Old Are You?'))

if age < 1 or age > 100:
    print('Incorrect age value.. please try again.')
elif age >= 0 and age < 20:
    # This Content Will Run
    print('You Are Still Young, Congrats!!')
elif age < 42:
    print('You Are Not Yet Middle Aged.')
else:
    print('You Are Old!')
