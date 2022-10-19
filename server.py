from socket import *
import time


# создаем соединение и ждем соединения от клиента
def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('localhost', 10000))
    s.listen(5)

    while True:
        client, addr = s.accept()
        print('Получаем запрос на соединение:', addr)
        timestr = time.ctime(time.time()) + '\n'
        client.send(timestr.encode('utf-8'))
        client.close()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)

# Получаем запрос на соединение: ('127.0.0.1', 43020)
# Получаем запрос на соединение: ('127.0.0.1', 58698)
# Получаем запрос на соединение: ('127.0.0.1', 51016)
