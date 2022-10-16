import csv

with open('data.csv') as f:
    f_reader1 = csv.reader(f)
    # Полученный итератор можно преобразовать в список
    #print(list(f_reader1))
    # [['hostname', 'vendor', 'model', 'location'],
    #  ['kp1', 'Cisco', '2960', 'Moscow'],
    #  ['kp2', 'Cisco', '2960', 'Novosoborsk'],
    #  ['kp3', 'Cisco', '2960', 'Kazan'],
    #  ['kp4', 'Cisco', '2960', 'Tomsk']]

    f_reader2 = csv.DictReader(f)
    for row in f_reader2:
        # Можно выводить содержимое отдельных столбцов.
        print(row['hostname'], ['model'])

# kp1 ['model']
# kp2 ['model']
# kp3 ['model']
# kp4 ['model']
