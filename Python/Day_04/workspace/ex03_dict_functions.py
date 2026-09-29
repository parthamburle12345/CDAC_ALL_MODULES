from vinutils import line
from pprint import pprint


line()
p1 = dict(name='Vinod', 
          email='vinod@vinod.co', 
          phones=['9731424784'],
          city='Bangalore',
          title='Mr.')

# all keys
for key in p1.keys():
    print(key)
line()
for key in p1:
    print(key)

# all values
line()
for val in p1.values():
    print(val)

# key/value pairs
line()
for kv in p1.items():
    print(kv)
line()

for k, v in p1.items():
    print(f'{k} --> {v}')

line()
# deleting the last entry
k, v = p1.popitem()
print(f"deleted the key {k} with value {v}")
print(p1)

print(f"{p1.pop("email") = }")