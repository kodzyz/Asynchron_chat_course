# python3 client.py
import csv

with open('data.csv') as f:
    #возможность изменения разделителя (if default не запятая)
    f_reader = csv.reader(f, delimiter="!")
    next(f_reader)
    for l in f_reader:
        print(l)

# ['kp1,Cisco,2960,Moscow']
# ['kp2,Cisco,2960,Novosoborsk']
# ['kp3,Cisco,2960,Kazan']
# ['kp4,Cisco,2960,Tomsk']

