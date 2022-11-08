# python3 service.py

import logging

logging.basicConfig(filename="module.log",
                    filemode='w')  # filemode - самообновление файла

import functions  # после глоб.настр чтобы они успели примениться

log = logging.getLogger('service')
log.critical("Error in service")

# ---- терминал когда нет строки 5
# faced error in functions module
# Error in service

