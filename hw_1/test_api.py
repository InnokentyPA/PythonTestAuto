# Получение постов

import requests
import yaml

S = requests.Session()

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    address = data['address2']

def test_rest(user_login):
    print(S.get(url=address, headers={'X-Auth-Token': user_login}).json())
