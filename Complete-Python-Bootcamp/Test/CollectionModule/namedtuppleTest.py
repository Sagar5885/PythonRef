from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age=2, name='sammy', breed='Lab')

print(sam.age)
print(sam[0])