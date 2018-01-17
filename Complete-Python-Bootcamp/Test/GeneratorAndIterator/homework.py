def genSquare(n):
    for i in range(n):
        yield i**2;
for i in genSquare(10):
    print(i)

print()
import random
random.randint(1,10)

def genRandHighLow(a, b, n):
    for i in range(n):
        yield random.randint(a,b)
for i in genRandHighLow(2, 8, 10):
    print(i)


print()
s = 'hello'
sc = iter(s)
for i in s:
    print(next(sc))


print()
my_list = [1,2,3,4,5]
gencomp = (item for item in my_list if item > 3)
for item in gencomp:
    print(item)