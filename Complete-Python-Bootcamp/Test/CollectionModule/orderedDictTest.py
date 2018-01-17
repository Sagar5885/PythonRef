print('Normal Dictionary: ')
d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k,v in d.items():
    print(k, v)

print()

from collections import OrderedDict
d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k,v in d.items():
    print(k, v)


print()
print('Dictionaries are equal? ')

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)

print()
print('Dictionaries are equal? ')

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'


d2 = OrderedDict()

d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)