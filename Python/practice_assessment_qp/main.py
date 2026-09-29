import json
import csv


customers = [
    {"id" :1, "name": "Harish", "city": "Bangalore"},
    {"id" :2, "name": "Mahesh", "city": "Bangalore"},
    {"id" :3, "name": "Santosh", "city": "Chennai"},
    {"id" :4, "name": "Naveen", "city": "Mumbai"},
]

#------------------------------------------------------------------

def menu():
    print("""
    0. Exit
    1. Add customer record
    2. View all customers
    3. Export customer data as JSON
    4. Export customer data as CSV
    5. Export customer data to text file (semicolon delimited)
    """)

    try:
        return int(input("Enter your choice: "))
    except:
        return -1

#------------------------------------------------------------------

def display_customers():
    if not customers:
        print("No customer data found. Please add some.")
        return

    if len(customers) == 1:
        cid, name, city = customers[0].values()
        print("1 customer found. Their details: ")
        print(f"Id          : {cid}")
        print(f"Name        : {name}")
        print(f"City        : {city}")
        print("-" * 50)
        return

    print("-"*60)
    print(f"{"ID":^5}"
          f"{"Name":<25}"
          f"{"City":<30}")
    print("-"*60)
    for c in customers:
        cid, name, city = c.values()
        print(f"{cid:^5}"
            f"{name:<25}"
            f"{city:<30}")
    print("-"*60)

#------------------------------------------------------------------

def export_to_json_file():
    try:
        filename = input("Enter JSON filename: ")
        with open(filename, "wt") as file:
            json.dump(customers, file, indent=3)
    except Exception as err:
        print("Something went wrong")
        print("System error message - " + err)

#------------------------------------------------------------------

def export_to_csv_file():
    try:
        filename = input("Enter CSV filename: ")
        with open(filename, "wt") as file:
            writer = csv.DictWriter(file, ["id", "name", "city"], lineterminator="\n")
            writer.writeheader()
            writer.writerows(customers)
    except Exception as err:
        print("Something went wrong")
        print("System error message - " + err)

#------------------------------------------------------------------

def export_to_text_file():
    try:
        filename = input("Enter text filename: ")
        with open(filename, "wt") as file:
            for c in customers:
                cid, name, city = c.values()
                file.write(f"{cid};{name};{city}\n")
    except Exception as err:
        print("Something went wrong")
        print("System error message - " + err)
#------------------------------------------------------------------

def main():
    while True:
        match menu():
            case 0:
                break
            case 1:
                ...
            case 2:
                display_customers()
            case 3:
                export_to_json_file()
            case 4:
                export_to_csv_file()
            case 5:
                export_to_text_file()
                            
            case _:
                print("Invalid choice!")

#------------------------------------------------------------------

if __name__ == '__main__':
    main()