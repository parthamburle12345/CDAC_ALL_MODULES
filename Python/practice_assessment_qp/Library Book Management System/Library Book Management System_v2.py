"""
DELIMITED FLAT-FILE CATALOG MANAGEMENT SYSTEM
Coursework: Python Systems Programming | Focus: Text File Handling
"""

FILE_PATH = "books.txt"


def add_book_entry(catalog: list[dict], next_id: int) -> int:
    """Prompts user for book details, appends new dict, returns updated ID counter."""
    try:
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        genre = input("Enter genre: ").strip()

        if not title or not author or not genre:
            print("Title, author, and genre cannot be empty.")
            return next_id

        price = float(input("Enter price: "))
        if price <= 0.0:
            print("Price must be greater than 0.")
            return next_id

        copies = int(input("Enter copies: "))
        if copies < 0:
            print("Copies must be an integer >= 0.")
            return next_id

        next_id += 1
        book = {
            "id": next_id,
            "title": title,
            "author": author,
            "genre": genre,
            "price": price,
            "copies": copies
        }
        catalog.append(book)
        print("Book added successfully.")
        return next_id

    except ValueError:
        print("Invalid numerical value. Please try again.")
        return next_id


def render_catalog(catalog: list[dict]) -> None:
    """Displays formatted tabular catalog or single-record card when count == 1."""
    if len(catalog) == 0:
        print("No books available.")
        return

    if len(catalog) == 1:
        b = catalog[0]
        print("----------------------------------------")
        print(f"ID       : {b['id']}")
        print(f"Title    : {b['title']}")
        print(f"Author   : {b['author']}")
        print(f"Genre    : {b['genre']}")
        print(f"Price    : {b['price']:.2f}")
        print(f"Copies   : {b['copies']}")
        print("----------------------------------------")
    else:
        print("-" * 90)
        print(f"{'ID':^5}{'Title':<25}{'Author':<25}{'Genre':<15}{'Price':>10}{'Copies':>8}")
        print("-" * 90)
        for b in catalog:
            print(f"{b['id']:^5}{b['title']:<25}{b['author']:<25}{b['genre']:<15}{b['price']:>10.2f}{b['copies']:>8}")
        print("-" * 90)


def query_books(catalog: list[dict], search_term: str) -> list[dict]:
    """Returns filtered list matching ID or case-insensitive title/author substring."""
    if search_term.isdigit():
        book_id = int(search_term)
        return [b for b in catalog if b["id"] == book_id]
    else:
        term = search_term.lower()
        return [b for b in catalog if term in b["title"].lower() or term in b["author"].lower()]


def modify_book_details(catalog: list[dict], book_id: int) -> bool:
    """Updates price and copies for the specified book ID; returns success status."""
    for b in catalog:
        if b["id"] == book_id:
            try:
                price = float(input("Enter new price: "))
                if price <= 0.0:
                    print("Price must be greater than 0.")
                    return False

                copies = int(input("Enter new copies: "))
                if copies < 0:
                    print("Copies must be an integer >= 0.")
                    return False

                b["price"] = price
                b["copies"] = copies
                print("Book details updated successfully.")
                return True

            except ValueError:
                print("Invalid numerical value.")
                return False

    print(f"No book found with ID {book_id}.")
    return False


def delete_book(catalog: list[dict]) -> None:
    """Prompts for explicit confirmation (y/n) before removing the record dictionary."""
    try:
        book_id = int(input("Enter book ID to delete: "))
        for b in catalog:
            if b["id"] == book_id:
                confirm = input("Are you sure you want to delete this book? (y/n): ").strip().lower()
                if confirm == "y":
                    catalog.remove(b)
                    print("Book deleted successfully.")
                else:
                    print("Delete operation cancelled.")
                return

        print(f"No book found with ID {book_id}.")
    except ValueError:
        print("Invalid book ID.")


def sync_catalog_to_file(filepath: str, catalog: list[dict]) -> None:
    """Serializes each book dictionary into pipe-delimited strings in write mode."""
    try:
        with open(filepath, "w") as file:
            for b in catalog:
                line = f"{b['id']}|{b['title']}|{b['author']}|{b['genre']}|{b['price']:.2f}|{b['copies']}\n"
                file.write(line)
        print("Catalog saved successfully.")
    except Exception as e:
        print(f"Error while saving catalog: {e}")


def load_catalog_from_file(filepath: str) -> list[dict]:
    """Parses books.txt line-by-line using split('|') and reconstructs dictionary list."""
    new_catalog: list[dict] = []
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            data = line.split("|")
            book = {
                "id": int(data[0]),
                "title": data[1],
                "author": data[2],
                "genre": data[3],
                "price": float(data[4]),
                "copies": int(data[5])
            }
            new_catalog.append(book)
    return new_catalog


def menu() -> int:
    """Interactive CLI menu loop controller."""
    print("\n*** LIBRARY BOOK MANAGEMENT SYSTEM ***")
    print("======================================")
    print("1. Add Book")
    print("2. View Catalog")
    print("3. Search Books")
    print("4. Update Details")
    print("5. Delete Book")
    print("6. Save to File")
    print("7. Load from File")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= 8:
            return choice
    except ValueError:
        pass
    return -1


def main() -> None:
    # Handle missing books.txt on initial load using try-except FileNotFoundError
    try:
        catalog = load_catalog_from_file(FILE_PATH)
        print(f"Loaded catalog from '{FILE_PATH}'.")
    except FileNotFoundError:
        print(f"'{FILE_PATH}' not found on initial load. Initializing with sample seed records.")
        catalog = [
            {"id": 1, "title": "Python Programming", "author": "John Zelle", "genre": "Technical", "price": 650.00, "copies": 15},
            {"id": 2, "title": "Clean Code", "author": "Robert Martin", "genre": "Technical", "price": 950.00, "copies": 8},
            {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "price": 350.00, "copies": 20},
            {"id": 4, "title": "Sapiens", "author": "Yuval Noah Harari", "genre": "History", "price": 550.00, "copies": 12},
            {"id": 5, "title": "Cosmos", "author": "Carl Sagan", "genre": "Science", "price": 480.00, "copies": 6}
        ]

    next_id = max((b["id"] for b in catalog), default=0)

    while True:
        choice = menu()

        match choice:
            case 1:
                next_id = add_book_entry(catalog, next_id)

            case 2:
                render_catalog(catalog)

            case 3:
                search_term = input("Enter Book ID, Title, or Author: ").strip()
                results = query_books(catalog, search_term)
                if results:
                    render_catalog(results)
                else:
                    print("No matching books found.")

            case 4:
                try:
                    book_id = int(input("Enter book ID to update: "))
                    modify_book_details(catalog, book_id)
                except ValueError:
                    print("Invalid book ID.")

            case 5:
                delete_book(catalog)

            case 6:
                sync_catalog_to_file(FILE_PATH, catalog)

            case 7:
                try:
                    catalog = load_catalog_from_file(FILE_PATH)
                    next_id = max((b["id"] for b in catalog), default=0)
                    print(f"Catalog loaded successfully from '{FILE_PATH}'.")
                except FileNotFoundError:
                    print(f"'{FILE_PATH}' file not found.")
                except Exception as e:
                    print(f"Error while loading catalog: {e}")

            case 8:
                print("Exiting program...")
                break

            case _:
                print("Invalid choice. Please retry.")


if __name__ == "__main__":
    main()
