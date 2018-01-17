for line in open('test.txt'):
    if(line.__contains__('test')):
        print(line)
    elif(line.__contains__('jest')):
        print(line.__add__(' jest line'))
    else:
        print('Not valid')

l = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10]

print()
for i in l:
    if(i%2 == 0):
        print(i)


print()
l2 = [(2,4), (3,6), (4,8)]
for tup in l2:
    print(tup)

print()
for (t1,t2) in l2:
    print(t1)
    print(t2)

print()
d={'k1':1, 'k2':2, 'k3':3}
for k in d:
    print(k)

print()
print('iterate d')
for k,v in d.items():
    print(k)
    print(v)

print()
x = 0
while(x<10):
    print('Current x val: ', x)
    x+=1
else:
    print('We are done!')

print()
x = range(1,10)
for e in x:
    if(e%2 != 0):
        print(e)

print()
st = 'Print only the words that start with s in this sentence'
result = []
for elistst in st.split(' '):
    if(elistst.__contains__('s')):
        result.append(elistst)
print(result)

print()
print('Comprehensive list')
lst = [x for x in range(50) if x%3 == 0]
print(lst)