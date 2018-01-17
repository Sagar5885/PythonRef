lst = ['a','b','c']
for number, item in enumerate(lst):
    print(number)
    print(item)

list = [1, 2, 3, 4, 5, 6, 7, 8]
print()
for count,item in enumerate(list):
    if count>=5:
        break
    else:
        print(item)