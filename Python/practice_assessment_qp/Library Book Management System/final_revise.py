def menu() -> int:
    print("*" * 60)
    print("=====================================================")
    print(
        "1. Add Book \n  2. View Catalog  \n  3. Search Books  \n  4. Update Details  \n  5. Delete Book  \n  6. Save to File  \n  7. Load from File  \n  8. Exit"
    )

    try:
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 8:
            choice = -1
    except ValueError:
        print("Invalid choice.")
        choice = -1
    return choice

# ================================================================================
def add_book_entry(catalog: list[dict], next_id: int) -> int:
    try:
        title = input("Enter title: ").title().strip()
        if title == "":
            print("Title cannot be empty.")
            return next_id

        author = input("Enter author: ").title().strip()
        if author == "":
            print("Author cannot be empty.")
            return next_id

        genre = input("Enter genre: ").title().strip()
        if genre == "":
            print("Genre cannot be empty.")
            return next_id

        price = float(input("Enter price: "))
        if price <= 0.0:
            print("Price must be greater than 0.0.")
            return next_id

        copies = int(input("Enter number of copies: "))
        if copies < 0:
            print("Copies cannot be negative.")
            return next_id

        book = {
            "id": next_id,
            "title": title,
            "author": author,
            "genre": genre,
            "price": price,
            "copies": copies,
        }

        catalog.append(book)
        print(f"Book record successfully added with ID: {next_id}")
        return next_id + 1

    except ValueError:
        print(
            "Invalid numerical value. Please enter correct numeric values for price and copies."
        )
        return next_id
# ================================================================================
def print_one_book(book: dict) -> None:
    print("----------------------------------------")
    print(f"ID       : {book['id']}")
    print(f"Title    : {book['title']}")
    print(f"Author   : {book['author']}")
    print(f"Genre    : {book['genre']}")
    print(f"Price    : {book['price']:.2f}")
    print(f"Copies   : {book['copies']}")
    print("----------------------------------------")
# ================================================================================
def print_many_books(book_list: list[dict]) -> None:
    print("-" * 90)
    print(
        f"{'ID':^5}"
        f"{'Book Title':<25}"
        f"{'Author Name':<22}"
        f"{'Genre':<15}"
        f"{'Price':>10}"
        f"{'Copies':>8}"
    )
    print("-" * 90)

    for book in book_list:
        print(
            f"{book['id']:^5}"
            f"{book['title']:<25}"
            f"{book['author']:<22}"
            f"{book['genre']:<15}"
            f"{book['price']:>10.2f}"
            f"{book['copies']:>8}"
        )

    print("-" * 90)
# ================================================================================
def render_catalog(catalog: list[dict]) -> None:
    if len(catalog) == 0:
        print("No records found.")
        return
    if len(catalog) == 1:
        print_one_book(catalog[0])
    else:
        print_many_books(catalog)
# ================================================================================
def query_books(catalog: list[dict], search_term: str) -> list[dict]:
    result = []
    term = search_term.strip().lower()
    for book in catalog:
        if (
            term == str(book["id"])
            or term in book["title"].lower()
            or term in book["author"].lower()
        ):
            result.append(book)
    return result
# ================================================================================


def modify_book_details(catalog: list[dict], book_id: int) -> bool:
    """Updates price and copies for the specified book ID; returns success status."""
    book = None
    for item in catalog:
        if item["id"] == book_id:
            book = item
            break

    if book is None:
        print(f"Book with ID {book_id} not found.")
        return False

    try:
        # Update Price
        price_input = input(f"Enter new unit price ({book['price']}): ").strip()
        if price_input == "":
            price = book["price"]
        else:
            price = float(price_input)
            if price <= 0.0:
                print("Price must be greater than 0.0.")
                return False

        # Update Stock Copies
        copies_input = input(
            f"Enter new stock copies ({book['copies']}): "
        ).strip()
        if copies_input == "":
            copies = book["copies"]
        else:
            copies = int(copies_input)
            if copies < 0:
                print("Copies must be a non-negative integer.")
                return False

        # Apply Updates
        book["price"] = price
        book["copies"] = copies

        print(f"Book details updated successfully for ID {book_id}.")
        return True

    except ValueError:
        print("Invalid numerical input. Please enter valid numeric values.")
        return False


# ================================================================================


def sync_catalog_to_file(filepath: str, catalog: list[dict]) -> None:
    try:
        with open(filepath, "w") as file:
            for book in catalog:
                file.write(
                    f"{book['id']}|{book['title']}|{book['author']}|{book['genre']}|{book['price']:.2f}|{book['copies']}\n"
                )
        print(f"Catalog successfully saved to {filepath}.")
    except Exception as err:
        print("Something went wrong")
        print(f"System error message - {err}")


# ================================================================================


def load_catalog_from_file(filepath: str) -> list[dict]:
    """Parses books.txt line-by-line using split('|') and reconstructs dictionary list."""
    catalog = []
    try:
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split("|")
                if len(parts) == 6:
                    book = {
                        "id": int(parts[0]),
                        "title": parts[1],
                        "author": parts[2],
                        "genre": parts[3],
                        "price": float(parts[4]),
                        "copies": int(parts[5]),
                    }
                    catalog.append(book)

        print(f"Catalog successfully loaded from {filepath}.")

    except FileNotFoundError:
        print(f"File '{filepath}' not found. Initializing with empty catalog.")
    except ValueError:
        print("Corrupted record format or invalid numeric data found in file.")
    except Exception as e:
        print(f"Error loading catalog: {e}")

    return catalog


# ================================================================================


def delete_book_entry(catalog: list[dict], book_id: int) -> bool:
    """Prompts for explicit confirmation (y/n) before removing the record dictionary."""
    book = None
    for item in catalog:
        if item["id"] == book_id:
            book = item
            break

    if book is None:
        print(f"Book with ID {book_id} not found.")
        return False

    confirm = (
        input(
            f"Are you sure you want to delete '{book['title']}' (ID: {book_id})? (y/n): "
        )
        .strip()
        .lower()
    )

    if confirm == "y":
        catalog.remove(book)
        print("Book deleted successfully.")
        return True
    else:
        print("Delete operation cancelled.")
        return False


# ================================================================================


def main():
    catalog = []
    next_id = 1
    filepath = "books.txt"

    while True:
        choice = menu()

        match choice:
            case 1:
                next_id = add_book_entry(catalog, next_id)

            case 2:
                render_catalog(catalog)

            case 3:
                search_term = input(
                    "Enter search term (ID, Title, or Author): "
                )
                results = query_books(catalog, search_term)
                render_catalog(results)

            case 4:
                try:
                    book_id = int(input("Enter Book ID to modify: "))
                    modify_book_details(catalog, book_id)
                except ValueError:
                    print("Invalid ID. Please enter an integer.")

            case 5:
                try:
                    book_id = int(input("Enter Book ID to delete: "))
                    delete_book_entry(catalog, book_id)
                except ValueError:
                    print("Invalid ID. Please enter an integer.")

            case 6:
                sync_catalog_to_file(filepath, catalog)

            case 7:
                catalog = load_catalog_from_file(filepath)
                if catalog:
                    next_id = max(book["id"] for book in catalog) + 1

            case 8:
                print("Terminating program...")
                break

            case _:
                print("Invalid choice. Please retry.")


# ================================================================================
if __name__ == "__main__":
    main()