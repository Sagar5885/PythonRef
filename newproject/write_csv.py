import csv

with open('test1Res1.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['res1'])
