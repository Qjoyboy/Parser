import json

import requests
class HeadHunter:

    def __init__(self, per_page=50, page=0):
        self.per_page = per_page
        self.page = page

    def get_vacancies(self):
        pass
r = requests.get('https://api.hh.ru/vacancies')
res = r.json()['items']

for i in range(len(r.json()['items'])):
    salary = res[i]['salary']

    salary_from = None
    salary_to = None

    if salary is not None:
        salary_from = res[i]['salary']['from']
        salary_to = res[i]['salary']['to']

    vacancy_inf = {
        'name': res[i]['name'],
        'salary_from': salary_from,
        'salary_to': salary_to,
        'area': res[i]['area']['name'],
        'employer': res[i]['employer']['name'],
        'url': res[i]['url'],
        'description': res[i]['snippet']['responsibility'][:40] + '...'
    }
    print(json.dumps(vacancy_inf, indent=4, ensure_ascii=False))