import re

text = 'This is a string with term1, but it does not have the other term.'

patterns = ['term1', 'term2']
re.search('hello', 'hello world!')

for pattern in patterns:
    print('Searching for "%s" in: \n"%s"' % (pattern, text))

    if re.search(pattern, text):
        print('\n')
        print('Match was found. \n')
    else:
        print('\n')
        print('No match found. \n')

match = re.search(patterns[0], text)
print(match.start())
print(match.end())