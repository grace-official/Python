# Python introductory data structures
# Iterating over data

'''
numData = [1, 2, 3, 4, 5]

for thing in numData:
    print(thing)

for num in range(len(numData)):
    numData[num] += 1

print(numData)
'''

data = ['apple', 1, 'orange', 4, 'zoo', True, 'panda', 3.14]

for val in data:
    if isinstance(val, int):
        print(f"Num {val}")
    elif isinstance(val, str):
        print(f"String {val}")
    elif isinstance(val, bool):
        print(f"Bool {val}")
    elif isinstance(val, float):
        print(f"Float {val}")
