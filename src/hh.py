import json

import requests

class HeadHunter:

    def __init__(self, per_page=20, page=0):
        self.per_page = per_page
        self.page = page


    _base_url = 'https://api.hh.ru/vacancies'
    def get_vacancies(self, count=2):
        vacancies = []

        for page in range(count):
            params = {
                'per_page': self.per_page,
                'page': self.page
            }
            response = requests.get(self._base_url, params=params)

            if response.status_code != 200:
                print(f'Ошибка {response.status_code}')
                break

            res = response.json().get('items',[])
            vacancies.extend(res)

        return vacancies

    def organize_vacancies(self, got_vac):
        res = got_vac
        vacancies = []
        for i in range(len(res)):
            salary = res[i]['salary']
            snippet = res[i]['snippet']
            desc = None
            salary_from = None
            salary_to = None

            if salary is not None:
                salary_from = res[i]['salary']['from']
                salary_to = res[i]['salary']['to']

            if snippet['responsibility'] is not None:
                desc = snippet['responsibility'][:40]

            vacancy_inf = {
                'name': res[i]['name'],
                'salary_from': salary_from,
                'salary_to': salary_to,
                'area': res[i]['area']['name'],
                'employer': res[i]['employer']['name'],
                'description': f'{desc}...',
                'url': res[i]['url'],
            }
            vacancies.append(vacancy_inf)
        return vacancies

    def save_to_json(self, vacancies):
        self.vacancies = vacancies
        with open('../saved_vacancies.json', 'w', encoding='utf-8') as file_obj:
            json.dump(vacancies, file_obj, indent=4, ensure_ascii=False)

req = HeadHunter()
x1 = req.get_vacancies(2)
x = req.organize_vacancies(x1)
result = req.save_to_json(x)
print(result)
