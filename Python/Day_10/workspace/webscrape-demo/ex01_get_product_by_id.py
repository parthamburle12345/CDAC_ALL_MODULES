import requests
from requests import Response


base_url = 'https://fakestoreapi.com'

products_url = f'{base_url}/products/'
carts_url = f'{base_url}/carts/'
users_url = f'{base_url}/users/'

product_id = int(input('Enter product id: '))

resp:Response = requests.get(f'{products_url}{product_id}')

if resp.status_code == 200:
    p = resp.json()
    print(f'Product found for id {product_id}')
    print(f'Name            : {p.get('title')}')
    print(f'Price           : ${p.get('price')}')
    print(f'Category        : {p.get('category')}')
    rating = p.get('rating', {})
    print(f'Rating          : {rating.get('rate')} fron {rating.get('count')} customers')

else:
    print(f'No product found for id {product_id}')