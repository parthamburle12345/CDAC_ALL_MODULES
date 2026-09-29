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

    def __iadd__(self, value):
        if type(value) is str:
            self.name += value
        elif type(value) in (int, float):
            self.salary += value
        return self     # mandatory for any __iXXX__ functions

    def __add__(self, value):
        if type(value) is str:
            result = self.name + value
        elif type(value) in (int, float):
            result = self.salary + value
        return result

    def __str__(self):
        return f'Employee(id={self.id!r}, name={self.name!r}, dept={self.dept!r}, salary={self.salary!r})'

#-------------------------------------
print('-'*80)
e1 = Employee('Ramesh', 45000, 'SALES')
print(e1)

print(e1 + ' Iyer')
print(e1 + 4000)
e1 += ' Iyer'   # e1.__iadd__(' Iyer')
e1 += 5000


print(e1)