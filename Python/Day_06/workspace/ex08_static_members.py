class Employee:
    id_counter = 0
    allowed_depts = ['ADMIN', 'SYSTEMS', 'PRODUCTION', 'SALES']

    def __init__(self, name=None, salary=15000, dept='ADMIN'):
        self.id = Employee.id_counter + 1
        self.name = name
        self.salary = salary
        if dept not in Employee.allowed_depts:
            dept = 'ADMIN'
        self.dept = dept

        Employee.id_counter += 1

    def __str__(self):
        return f'Employee(id={self.id!r}, name={self.name!r}, dept={self.dept!r}, salary={self.salary!r})'


#-----------------------------------

Employee.id_counter = 1000

e1 = Employee()
e1.id_counter = 2000    # creates a new variable called id_counter with in the object space for e1

e1.allowed_depts.append('MARKETING')


e2 = Employee('Scott', 45000, 'SYSTEMS')
e3 = Employee('Martin', 45000, 'MARKETING')

print('-'*80)
print(e1)
print(e2)
print(e3)

print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)

print(Employee.__dict__)