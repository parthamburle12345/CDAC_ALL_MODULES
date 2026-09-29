class Employee:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.salary = kwargs.get("salary")
        self.dept = kwargs.get("dept")

    def __str__(self):
        return f'Employee details: Id={self.id}, Name={self.name!r}, Salary={self.salary!r} and Department={self.dept!r}'

    def __repr__(self):
        return f'Employee(id={self.id!r}, name={self.name!r}, dept={self.dept!r}, salary={self.salary!r})'
