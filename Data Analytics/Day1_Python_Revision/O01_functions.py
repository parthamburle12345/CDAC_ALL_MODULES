# HOF
import time

# def introspect_time(fnc):
#     def inner_fun(*arg,**kwargs):
#         start = time.time()
#         result = fnc(*arg,**kwargs)# callback
#         end = time.time()
#         print(f"Time Taken is {end - start}")
#         return result
#     return inner_fun

class introspect_time:
    def __init__(self,fnc):
        self.fnc = fnc

    def __call__(self, *args, **kwds):
        start = time.time()
        result = self.fnc(*args,**kwds)# callback
        end = time.time()
        print(f"Time Taken is Class : [ {end - start} ]")
        return result
        

# add_fun = introspect_time(add_fun)
@introspect_time
def add_fun(x,y):
    time.sleep(1)
    return x + y

# print_list = introspect_time(print_list)
@introspect_time
def print_list(lst):
    for index,item in enumerate(lst):
        time.sleep(0.25)
        print(f"{index} -> {item}",end="\t:\t")
    print()


# print("addfun ",add_fun.__name__)
# print("print_list ",print_list.__name__)

res1 = add_fun(10,20)
print("result add ",res1,sep="\t:\t")
print("_" * 60)

# lst1 = list(map(lambda x:x**3,filter(lambda x:x>4, range(1,11))))

lst = [x**2 for x in range(1,11) if x > 4]
print_list(lst)





 