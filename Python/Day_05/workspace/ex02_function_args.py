from vinutils import line

line()


def greet(name='friend', city='your city'):
    return f"Hello, {name}! How's weather in {city}?"


msg = greet('Vishal', 'Delhi')
print(msg)

msg = greet('Vishal')
print(msg)

msg = greet()
print(msg)

msg = greet('Naveen')
print(msg)

msg = greet(city='Bangalore')
print(msg)

p1 = dict(name='Vinod', city='Bangalore')
# to unpack a dict, we have to use **
print(greet(**p1))

p2 = ['Vinay', 'Hassan']
# to unpack a tuple or list, we have to use *
print(greet(*p2))
