str = 'How long are the words in this phrase'

def word_lengths(phrase):
    return list(map(lambda l: len(l), phrase.split()))

print(word_lengths(str))




print()
import functools
list = [3,4,3,2,1]

def digits_to_num(digits):
    return functools.reduce(lambda a,b: (a*10)+b, digits)

print(digits_to_num(list))




print()
def filter_words(word_list, letter):
    return filter(lambda s: s[0] == letter, word_list)
l = ['hello','are','cat','dog','ham','hi','go','to','heart']
listr = filter_words(l,'h')
for l in listr:
    print(l)





print()
def concatenate(L1, L2, connector):
    return [word1+connector+word2 for (word1, word2) in zip(L1,L2)]
dictr = concatenate(['A','B'],['a','b'],'-')
for d in dictr:
    print(d)




print()
def d_List(L):
    return {key:value for value,key in enumerate(L)}
dictr2 = d_List(['a','b','c'])
for d in dictr2:
    print(d, dictr2[d])




print()
def count_match_index(L):
    return len([num for count,num in enumerate(L) if num == count])
print(count_match_index([0,2,2,1,5,5,6,10]))




