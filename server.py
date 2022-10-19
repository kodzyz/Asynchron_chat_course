from socket import *
import time

# инициализация сокета
s = socket(AF_INET, SOCK_STREAM)
# привязка к порту
s.bind(('localhost', 10000))
# режим ожидания запросов
s.listen(5)  # не более 5 клиентов

# пока программа работает мы должны принимать новых клиентов
while True:
    client, addr = s.accept()  # ожидание подключения клиента
    print('Получаем запрос на соединение:', addr)
    timestr = time.ctime(time.time()) + '\n'  # формируем сообщение для клиента - текущее время
    client.send(timestr.encode('utf-8'))  # кодируем сообщение
    client.close()
