import datetime

t = datetime.time(5, 25, 1)
print(t)
print(t.hour)
print(t.minute)

print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

today = datetime.date.today()
print(today)
print(today.timetuple())
