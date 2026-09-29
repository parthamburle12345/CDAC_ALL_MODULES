from pprint import pprint
from vinutils import line

line()
def main():
    emps = [
        "1928,Kumar,ADMIN,32000",
        "9383,Harish Rao,ACCOUNTING,42000",
        "8178,James,TRAINING,33000",
        "7442,Krihna Kumar,ADMIN,33000",
        "8273,Ramesh Iyer,ACCOUNTING,35000",
    ]

    emps_dict = {
        emp.split(',')[0]: emp.split(',')[1:]
        for emp in emps
    }

    while True:
        emp_id = input('Enter employee id to search (press RETURN to quit): ')

        if emp_id=='':
            break

        print(emps_dict.get(emp_id, "No employee found for this id"))

main()
