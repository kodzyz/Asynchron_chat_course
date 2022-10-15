# python3 client.py
import csv

with open('data.csv') as f:
    f_reader = csv.reader(f)
    next(f_reader)
    for l in f_reader:
        print(l)

# ['kp1', 'Cisco', '2960', 'Moscow']
# ['kp2', 'Cisco', '2960', 'Novosoborsk']
# ['kp3', 'Cisco', '2960', 'Kazan']
# ['kp4', 'Cisco', '2960', 'Tomsk']
