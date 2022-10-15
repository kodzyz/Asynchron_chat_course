# python3 client.py
import csv

with open('data.csv') as f:
    f_reader = csv.DictReader(f)  # должен быть headers
    for row in f_reader:
        print(row)

#-csv
# hostname,vendor,model,location
# kp1,Cisco,2960,Moscow
# kp2,Cisco,2960,Novosoborsk
# kp3,Cisco,2960,Kazan
#kp4,Cisco,2960,Tomsk

#-DictReader
# {'hostname': 'kp1', 'vendor': 'Cisco', 'model': '2960', 'location': 'Moscow'}
# {'hostname': 'kp2', 'vendor': 'Cisco', 'model': '2960', 'location': 'Novosoborsk'}
# {'hostname': 'kp3', 'vendor': 'Cisco', 'model': '2960', 'location': 'Kazan'}
# {'hostname': 'kp4', 'vendor': 'Cisco', 'model': '2960', 'location': 'Tomsk'}


