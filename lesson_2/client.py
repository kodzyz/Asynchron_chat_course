# python3 client.py
import json

data = {
    "action": "msg",
    "to": "account_name",
    "from": 1,
    "encoding": ["utf-8", "ascii"],
    "message": "message"
}

with open('new_data.json', 'w') as f:
    json.dump(data, f, sort_keys=True, indent=4)

with open('new_data.json') as f:
    data = json.load(f)
    for k, v in data.items():
        print(k, v, type(v))

# action msg <class 'str'>
# encoding ['utf-8', 'ascii'] <class 'list'>
# from 1 <class 'int'>
# message message <class 'str'>
# to account_name <class 'str'>
