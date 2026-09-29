import sqlite3

filename = 'emps.sqlite'
sql_cmd = 'INSERT INTO EMPS(NAME, DEPARTMENT, SALARY) VALUES (?, ?, ?)'

with sqlite3.connect(filename) as conn:
    cur = conn.cursor()
    while True:
        print("Enter employee details: ")
        name = input('Name      : ')
        dept = input('Department: ')
        salary = input('Salary    : ')

        print(sql_cmd)
        cur.execute(sql_cmd, (name, dept, salary))
        ans = input("Do you wish to add one more? yes/no [NO] ")

        if ans.strip().upper() in ('', 'NO'):
            break
    conn.commit()

print("Bye!")