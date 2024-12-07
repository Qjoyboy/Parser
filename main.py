import json

import requests

r = requests.get('https://api.hh.ru/vacancies')
res = r.json()['items']
for i in range(len(r.json()['items'])):
    data = res[i]['snippet']['responsibility'][:40]
    print(data)