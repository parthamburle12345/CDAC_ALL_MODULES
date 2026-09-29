from vinutils import line
from pprint import pprint


line()

p1 = dict(name='Vinod', email='vinod@vinod.co', phones=['9731424784'])

# access the values using keys
print(f'{p1["name"] = }')
print(f'{p1["email"] = }')
print(f'{p1["phones"] = }')
# print(f'{p1["city"] = }')
print(f'{p1.get('city', 'City Unknown') = }')

# adding/updating entries using keys
p1["city"] = "Bangalore"
p1["email"] = "vinod@cyblore.com"

pprint(p1)
print(f'{p1.get('city') = }')