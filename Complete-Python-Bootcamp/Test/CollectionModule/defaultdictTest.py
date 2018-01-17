from collections import defaultdict
d = defaultdict(object)
d['one']

for item in d:
    print(item)

print()

d = defaultdict(lambda: 0)
print(d['one'])
