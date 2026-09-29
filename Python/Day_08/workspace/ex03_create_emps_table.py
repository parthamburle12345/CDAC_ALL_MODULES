from sqlite3 import connect

filename = 'emps.sqlite'

sql_cmd = '''CREATE TABLE EMPS(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME VARCHAR(50) NOT NULL,
DEPARTMENT VARCHAR(100) DEFAULT 'ADMIN',
SALARY DOUBLE DEFAULT 25000
)'''

with connect(filename) as conn:
    cur = conn.cursor()
    cur.execute(sql_cmd)

print(f'Table EMPS created successfully in the sqlite file `{filename}`')