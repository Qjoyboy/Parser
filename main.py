# import json
#
# import requests
#
# r = requests.get('https://api.hh.ru/vacancies')
# res = r.json()['items']
# for i in range(len(r.json()['items'])):
#     data = res[i]['snippet']['responsibility'][:40]
#     print(data)
import json
from xml.etree.ElementTree import indent

with open('saved_vacancies.json', encoding='utf-8') as f:
    json_data = json.load(f)
    count =0
    for i in json_data:
        count+=1
    print(count)