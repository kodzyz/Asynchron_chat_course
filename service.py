# python3 service.py

import logging

# глобальные переменные в логере для вывода данных
logging.basicConfig(format='%(levelname)-10s %(module)s -- %(asctime)s:  %(message)s')

import functions  # после глоб.настр чтобы они успели примениться

log = logging.getLogger('amm')

# настройка handler
handler = logging.FileHandler('amm.log')
# изменение переменных вывода у определенного логера
formater = logging.Formatter('%(levelname)-10s %(message)s')
handler.setFormatter(formater)

log.addHandler(handler)

log.critical("Error in service")





