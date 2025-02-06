import psycopg2

conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    host='localhost',
    password='123'
)
cur = conn.cursor()
conn.autocommit = True

cur.execute("DROP DATABASE IF EXISTS hhparser")
cur.execute("CREATE DATABASE hhparser")

cur.close()
conn.close()

conn = psycopg2.connect(
    dbname='hhparser',
    user='postgres',
    host='localhost',
    password='123'
)
cur = conn.cursor()

sql1 = f"""CREATE TABLE vacancies(
        vacancy_id int primary key,
        title varchar(40)
        )
        """
cur.execute(sql1)
cur.execute(f"""INSERT INTO vacancies(vacancy_id, title) VALUES(1, 's')""")
print('Created')
cur.close()
conn.close()

