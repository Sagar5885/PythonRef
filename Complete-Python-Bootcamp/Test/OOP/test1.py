class Sample(object):
    pass

x = Sample()

print(type(x))

class Dog(object):

    species = 'mammal'

    def __init__(self, breed, name, fur=True):
        self.breed = breed
        self.name = name
        self.fur = fur

sam = Dog(breed='Lab', name='Sammy', fur=False)
print(sam.breed)
print(sam.name)
print(sam.species)
print(sam.fur)