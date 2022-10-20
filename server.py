from socket import *
import time


# UDP соединение
def main():
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # слушаем несколько источников
    s.bind(('localhost', 10000))

    while True:
        data = s.recv(128)  # получаем сообщение
        decoded_data = data.decode('utf-8')  # декодируем
        print(decoded_data)  # принтим


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)

# python3 server.py
# Сообщение - №0
# Сообщение - №1
# Сообщение - №2
# ...
# Сообщение - №995
# Сообщение - №996
# Сообщение - №997
# Сообщение - №998
# Сообщение - №999

