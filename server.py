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
        decoded_data = data.decode('utf-8')
        print('Было получено сообщение от клиента: ', decoded_data)
        if decoded_data == 'close':
            client.close()
            return  # потому что нет смысла что то отправлять
        msg = 'Я сервер: Ваше сообщение получено'
        client.send(msg.encode('utf-8'))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)

# Получаем запрос на соединение: ('127.0.0.1', 50718)
# Было получено сообщение от клиента:  close
# (venv) dk@dk-ThinkPad-Edge-E540:~/PycharmProjects/Asynchron_chat/chat_lesson$