import csv

with open('test1.csv') as csvfile:
    readCSV = csv.reader(csvfile)

    product_ids = []

    for raw in readCSV:
        product_id = raw[0]

        product_ids.append(product_id)

    print(product_ids)