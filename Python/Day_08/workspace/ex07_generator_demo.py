def fibo(pos):
    # print('start of fibo....')
    a, b = -1, 1
    for index in range(pos):
        # print(f'inside the loop {index = }')
        c = a + b
        a, b = b, c
        yield c
        # print('continuing the loop...')


#------------------------------

f10 = fibo(5)
print(f'{type(f10) = }')
# print('{f10 = }')
# print(next(f10))
# print(next(f10))
# print(next(f10))
# print(next(f10))
# print(next(f10))
# print(next(f10))

for i in f10:
    print(i)
