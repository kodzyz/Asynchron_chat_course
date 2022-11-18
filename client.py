from socket import *

s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect(('localhost', 8888))  # Соединиться с сервером

while True:  # Постоянный опрос сервера
    tm = s.recv(1024)
    print("Текущее время: %s" % tm.decode('utf-8'))

s.close()

# ------терминал: python3 server.py <---> python3 client.py
# Текущее время: Thu Nov 17 22:43:38 2022
#
# Текущее время: Thu Nov 17 22:43:39 2022
#
# Текущее время: Thu Nov 17 22:43:39 2022
#
# Текущее время: Thu Nov 17 22:43:39 2022
#
# Текущее время: Thu Nov 17 22:43:39 2022
#
# Текущее время: Thu Nov 17 22:43:39 2022
