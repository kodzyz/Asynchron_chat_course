from socket import *


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 10000))
    msg = 'Привет, сервер'.encode('utf-8')
    s.send(msg)  # отправка данных на сервер
    tm = s.recv(1024)  # получение от сервера
    s.close()
    print("Сообщение от сервера: ", tm.decode('utf-8'))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)

# Сообщение от сервера:  Привет, клиент
