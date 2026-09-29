from sys import getsizeof

max_limit = 1000000
l1 = [x**2 for x in range(1,max_limit)]
g1 = (x**2 for x in range(1,max_limit))
# print("sizeof(l1)",getsizeof(l1),"Type",type(l1),sep="\t:\t")
# print("sizeof(g11)",getsizeof(g1),"Type",type(g1),sep="\t:\t")

# print("sum(l1)",sum(l1),sep="\t:\t")
# print("sum(g1)",sum(g1),sep="\t:\t")
# print(l1)

# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
print("_" * 60)

def surabhi():
    print("Apple")
    yield 100
    print("Orange")
    yield 200
    print("Pine")
    yield 300

result = surabhi()

print(type(result))

print(next(result))
print(result.__next__())
print(result.__next__())
# print(result.__next__()) # stopiteration 
print("_" * 60)

for x in surabhi():
    print(x)



