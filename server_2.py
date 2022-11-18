# -------- Эхо-сервер, обрабатывающий "одновременно" несколько клиентов -------
# Обработка клиентов осуществляется функцией select
# 0:50

import select
from socket import socket, AF_INET, SOCK_STREAM


def read_requests(r_clients, all_clients):
    """ Чтение запросов из списка клиентов
    """
    responses = {}  # Словарь ответов сервера вида {сокет: запрос}

    for sock in r_clients:  # проверяются клиенты которые нам написали
        try:
            data = sock.recv(1024).decode('utf-8')  # получаем от них сообщение
            responses[sock] = data  # полученое сообщение add в dict - Словарь
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)
    return responses


def write_responses(requests, w_clients, all_clients):  # w_clients - клиенты которые ждут сообщения
    """ Эхо-ответ сервера клиентам, от которых были запросы
    """
    for sock in w_clients:
        if sock in requests:
            try:
                # Подготовить и отправить ответ сервера
                resp = requests[sock].encode('utf-8')
                # Эхо-ответ сделаем чуть непохожим на оригинал
                sock.send(resp.upper())  # сообщение будет в верхнем регистре
            except:  # Сокет недоступен, клиент отключился
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


def mainloop():
    """ Основной цикл обработки запросов клиентов
    """
    address = ('', 8888)
    clients = []

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(0.2)  # Таймаут для операций с сокетом
    while True:
        try:
            conn, addr = s.accept()  # Проверка подключений
        except OSError as e:
            pass  # timeout вышел
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)
        finally:
            # Проверить наличие событий ввода-вывода
            wait = 1  # 10
            r = []  # add тех, кто нам написал и выполнится ф-я read_requests ->68
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass  # Ничего не делать, если какой-то клиент отключился

            requests = read_requests(r, clients)  # Сохраним запросы клиентов ->68 = dict
            if requests:  # если dict не пустой  if {} -> False,  if {1:'123'} -> True
                write_responses(requests, w,
                                clients)  # Выполним отправку ответов клиентам -> выполнится ф-я write_responses


print('Эхо-сервер запущен!')
mainloop()
