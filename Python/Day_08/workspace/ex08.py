class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __iter__(self):
        yield self.name
        yield self.city


def numbers(start=0, stop=0, step=1):
    n = start
    while True:
        yield n
        n += step
        if n >= stop:
            break

for n in numbers(1, 30, 2):
    print(n)

def fn1():
    print("hello")
    yield 100
    yield 200
    yield 300


x = fn1()
print(x)

for a in x:
    print(a)


p1 = Person('Vinod', 'Bangalore')
for x in p1:
    print(x)

