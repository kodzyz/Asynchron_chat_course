# python3 client.py
import csv

data = [['hostname', 'vendor', 'model', 'location'],
        ['kp1', 'Cisco', '2960', 'Moscow, str'],
        ['kp2', 'Cisco', '2960', 'Novosoborsk, str'],
        ['kp3', 'Cisco', '2960', 'Kazan, str'],
        ['kp4', 'Cisco', '2960', 'Tomsk, str']]

with open('new_data.csv', 'w') as f:
    f_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, delimiter='!')  # разделителем будет - !
    for row in data:
        f_writer.writerow(row)

# "hostname"!"vendor"!"model"!"location"
# "kp1"!"Cisco"!"2960"!"Moscow, str"
# "kp2"!"Cisco"!"2960"!"Novosoborsk, str"
# "kp3"!"Cisco"!"2960"!"Kazan, str"
# "kp4"!"Cisco"!"2960"!"Tomsk, str"
