
class Parent:

    def __init__(self, age):
        print("Parent class created!")
        self.age = age
        self.FavIntro = 'Sample text'

    def sayFavIntro(self):

        print(self.FavIntro)

    def sayJoke(self):

        print('joke')

class Child(Parent):

    def __init__(self, age):
        super().__init__(age)
        print("Child created")
        self.age = age
        self.favIntro = 'hello'

    def sayJoke(self):
        print("no.")

parent = Parent(45)

child = Child(15)

parent.sayFavIntro()
child.sayFavIntro()