"""
Product Inventory Management System
"""

products = [ 
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10}, 
    {"id": 3, "name": "Smartphone", "category": "Electronics", "price": 20000, "quantity": 25} ,
    {"id": 4, "name": "Smartphone", "category": "Electronics", "price": 17800, "quantity": 12} ,
    {"id": 5, "name": "Smartphone", "category": "Electronics", "price": 31000, "quantity": 3} ,
    {"id": 2, "name": "Chair", "category": "Furniture", "price": 1500, "quantity": 50} ,
    {"id": 6, "name": "Smartphone", "category": "Electronics", "price": 200000, "quantity": 2} ,
] 

counter = len(products)


def menu():
    menu_text = '''1. Add Product 
2. View All Products 
3. Search Product 
4. Update Product 
5. Delete Product 
6. Exit '''

    print('**** Product Inventory Management System ****')
    print(menu_text)
    try:
        choice = int(input('Enter your choice: '))
    except:
        choice = -1

    return choice


def add_product():
    global counter

    try:
    
        name = input("enter a name:").strip()
        if name == "":
            print("name is not entered.")
            return

        category = input("enter category:")
        if category == "":
            print("enter valid category:")
            return

        price = float(input('Price: '))
        if price <= 0:
            print('Price must be > 0')
            return
        
        quantity = int(input('Quantity: '))
        if quantity < 0:
            print('Quantity must be >= 0')
            return
         

        products.append(dict(id=counter+1, name=name, category=category, price=price, quantity=quantity)) 
        counter+=1

    except  ValueError:
        print("retry with numerical value:") 


#-------------------------------------------------------------------------------

def print_one_product(p):
    pid, name, category, price, quantity = p.values()    
    print('---- Product Details ----')
    print(f'ID          : {pid}')
    print(f'Name        : {name}')
    print(f'Category    : {category}')
    print(f'Price       : {price}')
    print(f'Quantity    : {quantity}')
    print('-'*50) 

#-------------------------------------------------------------------------------

def print_many_products(product_list):
    print('-'*60)
    print(f'{'ID':^5}{'Name':<20}{'Category':<20}{'Price':>10}{'Qty':>5}')
    print('-'*60)
    for p in product_list:
        pid, name, category, price, quantity = p.values()
        print(f'{pid:^5}{name:<20}{category:<20}{price:>10.2f}{quantity:>5}')
    print('-'*60)

#-------------------------------------------------------------------------------

def search_product():
    try:
        print("enter id:")
        print("enter name:")
        choice = int(input("enter your choice 1 or 2:"))

        if choice == 1:
            pid = int(input("enter if od product to be search:"))
            search_product_by_id(pid)
        elif choice == 2:
            search_product_by_name()
        else:
            print("invalid choice.try again.")

    except:
        print("try again with integer value:")
    

#-------------------------------------------------------------------------------------

def view_products():
    if len(products) == 0:
        print("No products in the inventory. Please add first.")
    elif len(products) == 1:
        print_one_product(products[0])
    else:
        print_many_products(products)

#-------------------------------------------------------------------------------------

def search_product_by_id(pid):
    result = []
    for p in products:
        if p["id"] == pid:
            result.append(p)
            
    if not result:
        print(f'No product found for id {pid}')
        return None

    print_one_product(result[0])
    return result[0]
#-----------------------------------------------------------------------------------
def update_product():
    
    try:
        pid = int(input("Enter id of product to update: "))

        p = search_product_by_id(pid)

        if p is None:
            return

        name = input("Enter new name: ").strip()
        category = input("Enter new category: ").strip()
        price = float(input("Enter new price: "))
        quantity = int(input("Enter new quantity: "))

        p["name"] = name
        p["category"] = category
        p["price"] = price
        p["quantity"] = quantity

        print("Product updated successfully!")

    except ValueError:
        print("Please enter valid values.")


#-----------------------------------------------------------------------------------

def search_product_by_name():
    name=input("enter a name:")
    result=[]

    for p in products:
        if p["name"] == name:
            result.append(p)
    if not result:
        print(f"{name} not found")
        return    
    
    if len(result) == 1:
        print_one_product(result[0])
    else:
        print_many_products(result)


#-------------------------------------------------------------------------------

def delete_product():
    try:
        pid = int(input("enter number to be deleted:"))
        p = search_product_by_id(pid)
        if p is None:
            return
        ans = input("are you sure want to delete product(yes/no)?").lower()

        if ans == 'y':
            products.remove(p)
            print("product deleted succesfully.")
    except :
        print('Invalid type of value for product id. Try again with an integer.')


#-----------------------------------------------------------------------------------
def main():
    while True:
        choice = menu()

        match choice:
            case 1:
                add_product()
            case 2:
                view_products()
            case 3:
                search_product()
            case 4:
                update_product()
            case 5:
                delete_product()
            case 6:
                break
            case _:
                print('Invalid choice. Please retry.')


if __name__ == '__main__':
    main()