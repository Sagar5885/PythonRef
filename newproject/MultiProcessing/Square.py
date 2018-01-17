from multiprocessing import Pool

Squares = []

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        Squares = p.map(f, [1, 2, 3, 4, 5])

for xx in Squares:
    print(xx)