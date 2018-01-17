class Animal(object):

    def __init__(self):
        print('Animal Created')

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')

    def whoAmI(self):
        print('Dog')

    def bark(self):
        print('woof')

d = Dog()

print(d)
print(d.whoAmI())
print(d.eat())
print(d.bark())