filename = input('Enter a filename to read from: ')
try:
    f1 = open(filename)

    # print('The  first line in the file:')
    # print(f1.readline())

    print('Here is the content of the file:')
    print('-'* 50)
    print(f1.read())

    f1.close()

except FileNotFoundError:
    print(f'There is no such file - {filename}')
