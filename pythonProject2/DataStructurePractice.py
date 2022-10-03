# Python introductory data structures
# Heterogeneous (allow diverse data types)

# ITERABLE

# type 1: LISTS [] (ordered, changable, allows duplicates)

'''
data = [1,2,3,4,5]
print(data)
print(type(data))
print(len(data))
data.remove(3)
print(data)
'''

'''
data = [1,5,7,2,54,8,9,3]
print(data)
data.sort(reverse = True)
print(data)
'''
'''
data = ['apple', 'orange', 'zoo', 'panda', 'aardvark', 'mouse']
print(data)
data.sort()
print(data)
print(data.index('mouse'))
'''


# Type 2: TUPLES (ordered, unchangeable, allows duplicates)

'''
dataTuple = (1, 2, 3, 4, 5)
print(dataTuple)
print(type(dataTuple))
'''

# Type 3: SET {} (unordered, semi-changeable, no duplicates)

dataSet = {1, 2, 3, 4, 5}
print(dataSet)
