import re

split_term = '@'

str1 = 'My email address is: sagar@example.com'

print(re.split(split_term, str1))

print()
print('Find All re func: ')
print(re.findall('match', 'match this color with current match of class BTW findall is case sensitive'))