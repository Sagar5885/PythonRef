
print('Advance Numbers')
print(hex(14))
print(bin(14))
print(pow(2,3,5))
print(abs(-1))
print(round(3.4549454, 2))


print()
s = 'advance string'
print(s)
print(s.capitalize())
print(s.center(20, 'z'))
print(s.isalpha())
print(s.split('n'))
print(s.partition('n'))


print()
print('Advance Set: ')
s = set()
s.add(1)
s.add(2)
s.add('Sagar')

print(s)
s.clear()
print(s)
s = {1, 2}
sc = s.copy()
s.add(4)
print(sc)
print(s)
print(s.difference(sc))
s.difference_update(sc)
print(sc)
s.add(3)
print(s.intersection(sc))
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
print(s3.isdisjoint(s2))
print(s1.isdisjoint(s2))
print(s1.issubset(s2))
print(s2.issuperset(s1))
print(s1.symmetric_difference(s2))
print(s1.union(s2))


print()
print('Advance Dictionary: ')
print()
d = {'k1':1,'k2':2}
print('Dictionary Comprehensions: ')
print({x:x**2 for x in range(10)})
for i in d.items():
    print(i)
for k in d.keys():
    print(k)
for v in d.values():
    print(v)
# print(d.viewitems())
# print(d.viewkeys())
# print(d.viewvalues())



print()
print('Advance List: ')
l = [1,2,3]
l.append(4)
l.append(4)
print(l)
print(l.count(4))
l.extend([5,6,7,8,4])
print(l)
print(l.index(4))
l.pop()
print(l)
l.remove(4)
print(l)
l.reverse()
print(l)
l.sort()
print(l)