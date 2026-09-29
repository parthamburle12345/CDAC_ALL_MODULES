import subprocess
import json
import csv

books = []
filename = 'books.json'

def save_to_file():
    with open(filename, 'w') as file:
        json.dump(books, file)


def load_from_file():
    global books
    try:
        with open(filename) as file:
            books = json.load(file)
    except FileNotFoundError:
        pass

def menu():
    """
    Display a set of options to the user,
    accept the user's choice,
    do a basic validation
    if correct value, return the same
    else return -1
    """
    print("*** MAIN MENU ***")
    print("=================")
    print("0. Exit")
    print("1. Add a book record")
    print("2. View all books")
    print("3. Edit a book record")
    print("4. Delete a book")
    print("5. Export data as CSV")

    try:
        choice = int(input('Enter your choice: '))
        if choice < 0 or choice > 5:
            choice = -1
    except:
        choice = -1
        

    return choice

def add_book():
    b = {}
    print("Enter book details: ")

    while True:
        try:
            b["id"] = int(input("ID: "))
        except:
            user_input = input("Invalid value was entered. Enter 'r' to retry, any other key to go back to main menu.")

            if user_input != 'r':
                return
        else:
            break

    b['title'] = input("Title: ")
    b['author'] = input("Author: ")

    try:
        b['price'] = float(input("Price: "))
    except:
        print('Invalid value for price. Value was set to 0.0')
        b['price'] = 0

    books.append(b)
    save_to_file()


def view_books():
    print("-"*98)
    print(f"{"ID":^10} {"Title":<35} {"Author":<35} {"Price":>15}")
    print("-"*98)
    for b in books:
        print(f"{b['id']:^10} {b['title']:<35} {b['author']:<35} {b['price']:>15.2f}")
    print("="*98)


def edit_book():
    while True:
        try:
            book_id = int(input("Enter book id to edit: "))
        except:
            user_input = input("Invalid value was entered. Enter 'r' to retry, any other key to go back to main menu: ")

            if user_input != 'r':
                return
        else:
            break


    book_ids = [b["id"] for b in books] # list of books transformed into a list of ids
    if book_id not in book_ids:
        print("No such book. Try again.")
        return

    the_book = [b for b in books if b["id"]==book_id][0]
    _, title, author, price = the_book.values()

    _title = input(f'Title: ({title}) ')
    if _title == "":
        _title = title

    _author = input(f'Author: ({author}) ')
    if _author == "":
        _author = author

    _price = input(f'Price: ({price}) ')
    if _price == "":
        _price = price
    else:
        try:
            _price = float(_price)
        except:
            print("Invalid value for price. Remains unchanged.")
            _price = price

    the_book["title"] = _title
    the_book["author"] = _author
    the_book["price"] = _price

    print("The book is updated successfully!")
    save_to_file()


def delete_book():
    while True:
        try:
            book_id = int(input("Enter book id to delete: "))
        except:
            user_input = input("Invalid value was entered. Enter 'r' to retry, any other key to go back to main menu: ")

            if user_input != 'r':
                return
        else:
            break


    book_ids = [b["id"] for b in books] # list of books transformed into a list of ids
    if book_id not in book_ids:
        print("No such book. Try again.")
        return

    the_book = [b for b in books if b["id"]==book_id][0]
    print("Book found!")
    print(f"ID          : {the_book["id"]}")
    print(f"Title       : {the_book["title"]}")
    print(f"Author      : {the_book["author"]}")
    print(f"Price       : {the_book["price"]}")

    print()
    ans = input("Are you sure you want to delete this book? (yes/no): ")

    if ans.strip().lower() == "yes":
        books.remove(the_book)
        print("Book deleted successfully!")
    else:
        print("Book was not deleted!")
    save_to_file()


def export_as_csv():
    csv_filename = input('Enter filename to export: ')
    with open(csv_filename, mode='w', newline="", encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "title", "author", "price"])
        writer.writeheader()
        writer.writerows(books)
        print(f"Books data exported to '{csv_filename}' successfully.")

def main():
    load_from_file()
    while True:
        subprocess.call(["cls"], shell=True)
        user_choice = menu()

        if user_choice == 0:
            break

        if user_choice == 1:
            add_book()
        elif user_choice == 2:
            view_books()
        elif user_choice == 3:
            edit_book()
        elif user_choice == 4:
            delete_book()
        elif user_choice == 5:
            export_as_csv()
        else:
            print("Invalid choice! Please retry with valid value.")

        print()
        input("Hit RETURN/ENTER key  to continue")
    print("Bye!")


print("-" * 80)
main()