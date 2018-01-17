import functools

list = [47,11,42,13]
print('Fid max no from list using reduce and lambda: ',functools.reduce(lambda a,b: a if (a>b) else b, list))
print('Total all no from list using reduce and lambda: ',functools.reduce(lambda a,b: a+b, list))
