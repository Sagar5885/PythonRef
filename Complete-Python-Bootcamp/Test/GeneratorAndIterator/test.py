def gencubes(n):
    for i in range(n):
        yield i**3;

list = gencubes(10)

for i in list:
    print(i)

print()

def genFibo(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a+b

for i in genFibo(10):
    print(i)


print()
def simpleGen():
    for x in range(3):
        yield x
g = simpleGen()

while True:
    print(next(g))