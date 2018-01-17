s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print(set1.difference(set2))
print(set1.union(set2))

print()
print({x:x**3 for x in range(5)})

l = [1,2,3,4]
print(l)
l.reverse()
print(l)

l = [3,4,2,5,1]
print(l)
l.sort()
print(l)