# the person class
class Person:
    def __init__(self, n, a, f):
        self.name = n
        self.age = a
        self.FavQuote = f

    def sayName(self):
        print("My name is ", self.name)

    def sayAge(self):
        print("My age is ", self.age)

    def sayFaveQuote(self):
        print("My favourite quote is ", self.FavQuote)


