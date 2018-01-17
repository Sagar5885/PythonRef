print('Zip for List')
x = [1,2,3]
y = [4,5,6]

dict = zip(x,y)
for d in dict:
    print(d)

print('Zip for Dictionary')
d1 = {'a':1,'b':2}
d2 = {'c':4,'d':5}

d1d2 = zip(d1, d2)
for d in d1d2:
    print(d)

#print(zip(d2,d1.itervalues()))

def switcharoo(d1, d2):
    dout = {}

    for d1key,d2val in zip(d1, d2):
        dout[d1key] = d2val

    return dout

dictr = switcharoo(d1, d2)
for d in dictr:
    print(dictr[d])