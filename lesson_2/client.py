# python3 client.py
import json

with open('data.json') as f:
    objects = json.loads(f.read())
    print(objects, type(objects))
    # {'action': 'msg', 'time': '<unix timestamp>', 'to': 'account_name', 'from': 'account_name', 'encoding': 'ascii', 'message': 'message'} <class 'dict'>
    print('data', objects['action'])  # data msg
