import logging

# python3 test.py

# базовая настройка

# запись в один журнал
logging.basicConfig(level=logging.DEBUG, filename="app.log")  # запись в файл

# вызываем вывод сообщения дефолтного логгера
logging.info('info')  # 20
logging.critical('critical')  # 50

log = logging.getLogger("app")  # создаем свой логгер
log.setLevel(logging.DEBUG)  # уст. уровень
log.info('Hello world from app logger')  # записываем сообщение от него
