def fib(n):
    curr = 1
    prev = 0
    index = 1
    yield prev
    while index < n:
        yield curr
        prev, curr = curr, prev + curr
        index += 1


for num in fib(10):
    print(num,end="\t:\t")
print()

