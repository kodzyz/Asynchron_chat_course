# python3 client.py
# virtualenv venv
# source venv/bin/activate
# pip install pyyaml

import yaml

action_list = ['msg1', 'msg2', 'msg3']
to_list = ['account1', 'account2', 'account3']

data_to_uml = {'action': action_list, 'to': to_list}

with open('new_data.yaml', 'w') as f:
    yaml.dump(data_to_uml, f, default_flow_style=True)
