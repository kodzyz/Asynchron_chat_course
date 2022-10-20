from socket import *
import time


# создаем соединение и ждем соединения от клиента
def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('localhost', 10000))
    s.listen(5)

    client, addr = s.accept()
    print('Получаем запрос на соединение:', addr)

    while True:
        # получаем данные от клиента
        data = client.recv(100000)  # ожидаем получение байт данных
        print('Было получено сообщение от клиента: ', data.decode('utf-8'))
        msg = 'Я сервер: Ваше сообщение получено'
        client.send(msg.encode('utf-8'))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)

# Получаем запрос на соединение: ('127.0.0.1', 42836)
# Было получено сообщение от клиента:  hi
# Было получено сообщение от клиента:  hi hi