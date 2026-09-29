'''
Develop a context manager
1. context manager work with "with" statements
'''

class CA:
    def __init__(self):
        print("self",id(self))
       
    def fun(self):
        print("fun")

    def __enter__(self):
        print("Enter")

    def __exit__(self, exc_type, exc, tb):
        print("Exit")

# obj = CA()
# print(id(obj))

obj1 = CA()
with obj1:
    obj1.fun()
    # print(id(obj1))
    
