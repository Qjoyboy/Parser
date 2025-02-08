import json

import psycopg2


class DBManager:

    def __init__(self, dbname, user, host, password):
        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = password


    def create_database(self):
        self.conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            host='localhost',
            password='123'
        )

        cur = self.conn.cursor()
        self.conn.autocommit=True

        cur.execute("DROP DATABASE IF EXISTS hhparser")
        cur.execute("CREATE DATABASE hhparser")

        cur.close()
        self.conn.close()

        self.conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            host=self.host,
            password=self.password
        )
        self.conn.autocommit = True

    def create_table_and_fill(self):
        query = f"""CREATE TABLE vacancies(
                vacancy_id serial primary key,
                name text,
                salary_from int,
                salary_to int,
                area text,
                employer text,
                description text,
                url text not null
                );
            """
        cur = self.conn.cursor()
        cur.execute(query)

        with open('saved_vacancies.json', encoding='utf-8') as f:
            json_data = json.load(f)
            query ="""INSERT INTO vacancies(name, salary_from, salary_to, area, employer, description, url)
                      VALUES(%s,%s,%s,%s,%s,%s,%s)"""
            for i in json_data:
                values = (i['name'], i['salary_from'],i['salary_to'], i['area'],i['employer'],i['description'],i['url'])
                cur.execute(query, values)
        cur.close()

    def print_vacancy(self, vacancy):
        """Форматированный вывод вакансии"""
        vacancy_id, title, salary_from, salary_to, city, company, description, link = vacancy
        salary_text = f"{salary_from}-{salary_to} руб." if salary_from and salary_to else "Не указана"

        print(f"""
               {title} ({company})
               Город: {city}
               Зарплата: {salary_text}
               Описание: {description[:50]}...
               Подробнее: {link}
               """)

    def get_all_vacancy(self):
        cur = self.conn.cursor()
        query = "select * from vacancies"
        cur.execute(query)
        res = cur.fetchall()
        cur.close()
        return res

    def get_avg_salary(self):
        """ Получает среднюю зарплату по всем вакансиям """
        with self.conn.cursor() as cur:
            query = """SELECT AVG((salary_from + salary_to) / 2) 
                       FROM vacancies
                       WHERE salary_from IS NOT NULL AND salary_to IS NOT NULL"""
            cur.execute(query)
            return cur.fetchone()[0]

    def get_vacancy_with_avg_salary(self, diff=10000):
        avg_salary = self.get_avg_salary()
        cur = self.conn.cursor()
        query = """SELECT * 
                   FROM vacancies 
                   WHERE ABS((salary_from + salary_to) / 2 - %s) <= %s"""
        cur.execute(query, (avg_salary, diff))
        res = cur.fetchall()
        cur.close()
        return res



    def get_vacancies_with_higher_salary(self):
        cur = self.conn.cursor()
        query = """select * from vacancies
                where (salary_from + salary_to) /2 >
                (select avg((salary_from+salary_to)/2) from vacancies)"""
        cur.execute(query)
        res = cur.fetchall()
        cur.close()
        return res

    def close_conn(self):
        self.conn.close()
