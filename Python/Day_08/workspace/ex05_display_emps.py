import sqlite3

with sqlite3.connect('emps.sqlite') as cn:
    cr = cn.cursor()
    cr.execute('SELECT * FROM EMPS')
    rows = cr.fetchall()
    for row in rows:
        id, name, dept, sal = row
        print(f'{id:^10}{name:<30}{dept:<30}{sal:15.2f}')