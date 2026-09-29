filename = input('Enter filename to create: ')

with open(filename, mode='a') as f1:
    i = 1
    while True:
        name = input('Enter a name: (RETURN to quit) ')
        if not name:
            break
        f1.write(name + '\n')
        if i%3 == 0:
            f1.flush()
        i+=1
        
print('Bye!')