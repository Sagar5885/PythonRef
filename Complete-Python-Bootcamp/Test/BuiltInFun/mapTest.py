def fernht(T):
    return (9.0/5)*T + 32
temp = [0, 22.5, 40, 100]
print(list(map(fernht, temp)))

#or Single line bellow
print(list(map(lambda T: (9/5)*T + 32, temp)))