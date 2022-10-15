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
    json_string = json.dumps(data)
    f.write(json_string)

# {"action": "msg", "to": "account_name", "from": "account_name", "encoding": "ascii", "message": "message"}
