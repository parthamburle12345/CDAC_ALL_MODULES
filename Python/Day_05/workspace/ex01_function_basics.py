from vinutils import line

line()


def greet(name, city):

    if name.strip() == '':
        return f'Hello, friend!'
    
    return f'Hello, {name}! How\'s weather in {city}?'


the_message = greet('James', 'Dallas')
print(the_message)

the_message = greet(city='Shivamogga', name='Naveen')
print(the_message)

the_message = greet('   ', 'Dallas')
print(the_message)
