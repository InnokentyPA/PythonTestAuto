# Отправка поста

import requests
import yaml

S = requests.Session()

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    address = data['address2']
    
def test_post(user_login):
    print(S.post(url=address, headers={'X-Auth-Token': user_login}, data = {'title' : data['titlee'],
     'description' : data['descriptionn'], 'content' : data['contentt']}).json())