# python3 client.py
import json

with open('data.json') as f:
    objects = json.load(f)
    print('from obj: ', objects['action'])  # значение по ключу
    for s, c in objects.items():
        print(s, c)  # КЛЮЧ: ЗНАЧЕНИЕ

# from obj:  msg
# action msg
# time <unix timestamp>
# to account_name
# from account_name
# encoding ascii
# message message
