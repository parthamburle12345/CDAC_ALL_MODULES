def create_hello(name=None, city=None):

    x = 100
    y = 200

    if name == None:
        name = 'friend'

    if city == None:
        city = 'your city'

    def hello():
        msg = f'Hello, {name}, how is weather in {city}'
        print(msg)

    return hello


fun1 = create_hello('Vinod')
fun1()