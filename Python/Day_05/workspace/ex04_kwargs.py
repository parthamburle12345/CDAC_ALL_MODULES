from vinutils import line

line()

def test(**kwargs):
    print(f'{type(kwargs)=}')
    print(f'{kwargs=}')
    print()


test(name='Vinod', city='Bangalore')
test(name='Vinod', email='vinod@vinod.co')
test(n=100, m=400, graph=True)