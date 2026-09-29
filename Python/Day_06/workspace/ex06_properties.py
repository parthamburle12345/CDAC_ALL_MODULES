import vinutils, re

vinutils.line()

class InvalidMarksException(Exception): pass
class InvalidSubjectException(Exception): pass

class Student:
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__subject = kwargs.get('subject')
        self.__marks = kwargs.get('marks')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, marks):
        if type(marks) not in (int, float):
            raise InvalidMarksException('Marks must be a number')

        if marks < 0 or marks > 100:
            raise InvalidMarksException('Marks must be between 0 and 100')
        
        self.__marks = marks


    # getter for subject
    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        if not isinstance(value, str):
            raise InvalidSubjectException('Subject must be a string')

        pattern = re.compile(r'^(physics|maths|chemistry)$', re.IGNORECASE)
        if not pattern.search(value):
            raise InvalidSubjectException('Subject must be one of Physics, Maths and Chemistry')

        self.__subject = value.upper()


    def __str__(self):
        return f'Student(name={self.__name!r}, subject={self.__subject!r}, marks={self.__marks!r})'


def main():
    s1 = Student(name='Ravi', subject='Physics', marks=34.9)
    print(s1)
    s2 = Student()

    s2.name = 'Kishan'
    s2.marks = 35    # calls the setter corresponding to this property
    s2.subject = '123'

    print(s2)


main()