# python3 client.py
import json

data = {
    "action": "msg",
    "to": "account_name",
    "from": "account_name",
    "encoding": "ascii",
    "message": "message"
}

with open('new_data.json', 'w') as f:
    json.dump(data, f, sort_keys=True, indent=4)  # sort_keys - пересортирует ключи по алфавиту, indent - отступ
#
# {
#   "action": "msg",
#   "encoding": "ascii",
#   "from": "account_name",
#   "message": "message",
#   "to": "account_name"
# }
