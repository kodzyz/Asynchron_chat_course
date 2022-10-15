# python3 client.py
# virtualenv venv
# source venv/bin/activate
# pip install pyyaml

import yaml

with open('data.yaml') as f:
    f_content = yaml.safe_load(f)
    print(f_content)

# {'message': ['msg_1', 'msg_2', 'msg_3'], 'to': ['account_1', 'account_2', 'account_3']}
