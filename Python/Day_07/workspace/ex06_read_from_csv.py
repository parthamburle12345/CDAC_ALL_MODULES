import csv


filename = 'workspace/customers.csv'

with open(filename, mode='r', encoding='utf-8') as csv_file:
    # for row in csv.reader(csv_file):
    #     print(row)
    for row in csv.DictReader(csv_file):
        print(row)

    