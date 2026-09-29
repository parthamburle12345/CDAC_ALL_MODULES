import pickle
from myclasses import Employee

if __name__ == '__main__':
    # means, this script is being run/executed; not imported
    filename = 'employees' # extension for any file is optional
    employees = [
        Employee(id=123, name='Ramesh', dept='ADMIN', salary=44000),
        Employee(id=436, name='Rajesh', dept='ACCOUNTING', salary=48000),
        Employee(id=764, name='Kishore', dept='ADMIN', salary=47000),
    ]
    with open(filename, 'wb') as file:
        pickle.dump(employees, file)
        print(f"Employees data saved into a binary file `{filename}`")

