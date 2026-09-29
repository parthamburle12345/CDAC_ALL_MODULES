from vinutils import line

line()

class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.city = kwargs.get('city')

    def print(self):
         print(f'Name          : {self.name}')
         print(f'City          : {self.city}')


class Employee(Person):
    def __init__(self, **kwargs):
            # invoke super/base/parent class __init__
            super().__init__(**kwargs)
            # Person.__init__(self, **kwargs)
            self.department = kwargs.get('department')
            self.salary = kwargs.get('salary')

    # method overriding
    def print(self):
         print("========== EMPLOYEE ==========")
         super().print()
         print(f'Department    : {self.department}')
         print(f'Salary        : {self.salary}')

#==================================
p1 = Person(name='Ramesh', city='Chennai')
# print(dir(p1))

e1 = Employee(name='Suresh', city='Jaipur', department='ADMIN', salary=55000)
# print(dir(e1))
# print(e1.__dict__)
e1.print()