import logging

# python3 test.py

# базовая настройка

# запись в один журнал
logging.basicConfig(level=logging.DEBUG)  # настройка для всех логеров уровня 10

# создает логер глобально на уровне библиотеки
logging.info('info')  # 20
logging.critical('critical')  # 50
# ----- сообщения INFO, CRITICAL видим:
# INFO:root:info
# CRITICAL:root:critical

logger = logging.getLogger()  # по умолчанию 'root'
# logger.setLevel(logging.CRITICAL)  # тут меняем уровень с 10 на 50

logger.info('hi I\'m message')  # и пытаемся записать сообщение с уровенем 20 -> и не видим все что ниже
# ------ без 18 строчки
# INFO:root:hi I'm message
