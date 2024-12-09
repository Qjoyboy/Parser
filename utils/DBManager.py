import psycopg2

conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    host='localhost',
    password='123'
)
cur = conn.cursor()
conn.autocommit = True

cur.execute("DROP DATABASE postgres")
sql = "CREATE DATABASE hhparser"
cur.execute(sql)

print('Created')
sql1 = f"""CREATE TABLE vacancies(
        name varchar(40)
        """
cur.execute(sql1)
cur.close()
conn.close()
#
#
# class DBManager:
#
#     def __init__(self, host, database, user, password):
#         self.host = host
#         self.database = database
#         self.user = user
#         self.password = password
#
#     def conn_to_db(self):
#         return psycopg2.connect(dbname=self.database, user=self.user, host=self.host, password=self.password)
#
#     def create_database(self):
#         conn = psycopg2.connect(
#             dbname=self.database,
#             user=self.user,
#             host=self.host,
#             password=self.password
#         )
#         cursor = conn.cursor()
#
#         conn.autocommit=True
#
#         sql = ("CREATE DATABASE hhparser")
#
#         cursor.execute(sql)
#         cursor.close()
#         conn.close()
# dbname = 'hhparser'
# host = '127.0.0.1'
# password = '123'
# user = 'gon'
# x = DBManager(dbname, user, host, password)
# x.create_database()
# x.conn_to_db()





