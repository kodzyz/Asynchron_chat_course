import csv

with open('data.csv') as f:
    f_reader = csv.reader(f)
    print((f_reader, type(f_reader)))  # итератор # (<_csv.reader object at 0x7fa70ad6beb0>, <class '_csv.reader'>)
    print(next(f_reader))  # первая строка # ['hostname', 'vendor', 'model', 'location']
    print(type(next(f_reader)))  # <class 'list'>



