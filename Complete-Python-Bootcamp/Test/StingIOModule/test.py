from io import StringIO

message = 'This is just a normal string.'
f = StringIO(message)

print(f.read())

f.write('This is Sagar writing in StringIO')

print(f.seek(0))
print(f.read())