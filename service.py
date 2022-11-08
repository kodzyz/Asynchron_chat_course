# python3 service.py

import logging

# глобальные переменные в логере для вывода данных
logging.basicConfig(filename="module.log",
                    filemode='w', format='%(levelname)-10s %(module)s -- %(asctime)s:  %(message)s')

import functions  # после глоб.настр чтобы они успели примениться

log = logging.getLogger('app1')
log.critical("Error in service")

# ---- терминал когда нет строки 5
# faced error in functions module
# Error in service

