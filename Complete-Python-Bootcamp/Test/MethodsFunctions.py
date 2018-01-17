print('Volume of sphere: ')
def radius(r):
    return (4/3)*(3.14)*(r**3)

print('Volume of sphere with radius of 3: ',radius(3))

print()
print('No is in Range or not: ')
def range_check(n, low, high):
    if(n in range(low, high+1)):
        print('%s is in range' %str(n))
    else:
        print('number is not in range')
print(range_check(0, 1, 10))
#print('but 11 is not in range', range_check(11, 1, 10))

print()
print('Find no of upper and lower case letters from String: ')
def up_low(s):
    d = {'upper': 0, 'lower': 0}
    for c in s:
        if(c.isupper()):
            d['upper']+=1
        elif(c.islower()):
            d['lower']+=1
        else:
            pass
    print('Original String: ', s)
    print('No of upper case letters in give original string are: ', d['upper'])
    print('No of lower case letters in give original string are: ', d['lower'])
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

print()
print('unique list: ')
def unique_list(l):
    ld = []
    for e in l:
        if e not in ld:
            ld.append(e)
    return ld
list = [1,1,2,2,4,4,3,4,5,1,2,4,5,6]
print(unique_list(list))

print()
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print('Multiply list: ',multiply([1,2,3,-4]))

print()
def palindrome(s):
    s = s.replace(' ','')
    return s == s[::-1]
s = 'nurses run'
print("Check weather '%s' is palidrome or not: " %str(s))
print(palindrome(s))

print()
import string
def ispangram(strl, alphabet=string.ascii_lowercase):
    alphabet = set(alphabet)
    return alphabet <= set(strl.lower())
print("check pangram for 'The quick brown fox jumps over the lazy dog' : ")
print(ispangram('The quick brown fox jumps over the lazy dog', alphabet=string.ascii_lowercase))