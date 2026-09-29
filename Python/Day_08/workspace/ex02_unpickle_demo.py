import pickle
from myclasses import Employee

filename = 'employees'

with open(filename, 'rb') as file:
    data = pickle.load(file)

print(f'{type(data) = }')
print(f'{type(data[0]) = }')
print()

for emp in data:
    print(emp)