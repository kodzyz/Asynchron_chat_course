import logging

# python3 test.py

# базовая настройка

# запись в один журнал
logging.basicConfig(level=logging.DEBUG)  # настройка для всех логеров

# создает логер глобально на уровне библиотеки
logging.info('info')
logging.critical('critical')
# -------------- под капотом сделает так
# logger = logging.getLogger('root')
# logger.info('info')
# -------------- выведет в терминал
# INFO:root:info
# CRITICAL:root:critical

# создает логер вручную
log = logging.getLogger('app')  # создаем или получаем логер имя = 'app', по дефолту имя = 'root'

# log.setLevel(logging.CRITICAL)  # уровень критические ошибки, значение 50
# log.critical('critical from app')  # CRITICAL:app:critical from app - вывод в терминал

# log.setLevel(logging.CRITICAL)
# log.info('critical from app')  # ничего не отобразит потому что это самый высокий уровень 50, у 'info' значение 20

log.setLevel(logging.DEBUG)  # отладочная инфо, значение 10
log.info('critical from app')  # INFO:app:critical from app -> видим все уровни выше => 20, 30, 40, 50

