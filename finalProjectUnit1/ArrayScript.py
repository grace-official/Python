# List Creation
def ArrayOption():

    n = int(input("Enter the number of elements: \n"))
    l1 = list()
    # setting range
    for i in range(n):
        # adds the elements to list 1
        ele = int(input("Enter the numbers: \n"))
        l1.append(ele)

    # maths for lists
    s = sum(l1)
    Min = min(l1)
    Max = max(l1)
    avg = s / len(l1)

    print("Sum of numbers is: ", s)
    print("\nMinimum value is: ", Min)
    print("\nMaximum value is: ", Max)
    print("\nAverage is: ", avg)
