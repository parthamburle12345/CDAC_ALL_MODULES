import sqlite3

empid = int(input('Enter employee id to search: '))

with sqlite3.connect('emps.sqlite') as cn:
    cr = cn.cursor()
    cr.execute('SELECT * FROM EMPS WHERE ID=?', (empid,))
    emp = cr.fetchone()
    if not emp:
        print(f'No employee found for id {empid}')
    else:
        _, name, dept, sal = emp
        print("Employee found!")
        print(f"Name      : {name}")
        print(f"Department: {dept}")
        print(f"Salary    : {sal}")