
def main():
    print("This is a program to understand `print` function")

    name, city = 'Vinod', 'Bangalore'
    print(name + ' lives in ' + city + '.')

    temp = 22
    print('In ' + city + ', temperature today is ' + str(temp) + ' degrees')
    print(f'In {city}, temperature today is {temp} degrees')
    print('In %s, temperature today is %d degrees' % (city, temp))
    print('In {0}, temperature today is {1} degrees'.format(city, temp))

    print(f'{name=}')
    print(f'{city=}')
    print(f'{temp=}')

    print(name)
    print(city)
    print(temp)
   

main()

