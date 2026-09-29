from functools import partial
def fun(a,b,c,x):
    return a+b+c+x

print(fun(1,2,3,4))

g = partial(fun,10,20,30)

print(g(100))
print(g(200))
print(g(300))

print("_" * 60)

def greet(msg):
    def inner(sep):
        def inner_most(name):
            return f"{msg}{sep}{name}"
        return inner_most
    return inner

# Currying
res_sep_1 = greet("Happy Deebawali")
res_name_1 = res_sep_1("===>>>")
print(res_name_1("Krish Srikanth"))
print(res_name_1("Ravi Ashwin"))
print(res_name_1("Dinesh karthick"))
print("_" * 60)

res_sep_2 = greet("Happy Deepavali")
res_name_2 = res_sep_2("===>>>")
print(res_name_2("Srinath"))
print(res_name_2("prasad"))
print(res_name_2("rahul"))
print("_" * 60)


res_sep_2 = greet("Happy Diwali")
res_name_2 = res_sep_2("===>>>")
print(res_name_2("Sewag"))
print(res_name_2("Sachin"))
print(res_name_2("Yuvi"))
print("_" * 60)




