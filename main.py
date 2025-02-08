from src.hh import HeadHunter
from utils.DBManager import DBManager

print("""Здравствуйте, это парсер вакансий с hh.ru.
Введите количество страниц которое хотите получить(на странице по 20 вакансий)""")
count = int(input("Введите целое число: "))

keyword = input('Введите ключевое слово по которому хотите вести поиск: ')

req = HeadHunter()
vacancies = req.get_vacancies(count, keyword)
org_vacancies = req.organize_vacancies(vacancies)
result = req.save_to_json(org_vacancies)

sql = DBManager('hhparser','postgres','localhost','123')

sql.create_database()
sql.create_table_and_fill()


while True:
    try:
        x = int(input("""0 - прекратить работу программы
        1 - вывести все вакансии
        2 - вывести среднюю зарплату
        3 - вывести вакансии с зп выше средней
        -> """))
        if x==0:
            break
        elif x==1:
            vacancies = sql.get_all_vacancy()
            for vacancy in vacancies:
                sql.print_vacancy(vacancy)
        elif x==2:
            vacancies = sql.get_vacancy_with_avg_salary()
            for vacancy in vacancies:
                sql.print_vacancy(vacancy)
        elif x==3:
            vacancies= sql.get_vacancies_with_higher_salary()
            for vacancy in vacancies:
                sql.print_vacancy(vacancy)
        else:
            print('Введите целое число')
    except ValueError:
        print('Введите целое число')




