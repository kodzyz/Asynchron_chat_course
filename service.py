# python3 service.py

import logging

# типы handler

logging.basicConfig(filename='ann.log', format='%(levelname)-10s %(module)s -- %(asctime)s:  %(message)s')

import functions

log = logging.getLogger('ann')

# настройка handler
handler = logging.StreamHandler()
log.addHandler(handler)

log.critical("Error in service")

#------терминал
# Error in service




