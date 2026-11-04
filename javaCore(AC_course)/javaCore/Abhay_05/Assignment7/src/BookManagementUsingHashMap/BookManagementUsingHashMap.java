package BookManagementUsingHashMap;

import java.util.*;

class Book {

	int bookId;
	String title;
	String author;
	double price;

	public Book(int bookId, String title, String author, double price) {
		this.bookId = bookId;
		this.title = title;
		this.author = author;
		this.price = price;
	}

	void displayBook() {
		System.out.println("Book ID : " + bookId);
		System.out.println("Title   : " + title);
		System.out.println("Author  : " + author);
		System.out.println("Price   : " + price);
		System.out.println();
	}
}

public class BookManagementUsingHashMap {
	public static void main(String[] args) {

		HashMap<Integer, Book> books = new HashMap<>();
		Scanner sc = new Scanner(System.in);

		while (true) {

			System.out.println("\n Book Management System ");
			System.out.println("1. Add Book");
			System.out.println("2. Display All Books");
			System.out.println("3. Search Book by ID");
			System.out.println("4. Update Book");
			System.out.println("5. Delete Book");
			System.out.println("6. Exit");
			System.out.print("Enter your choice: ");

			int choice = sc.nextInt();

			switch (choice) {

			case 1:
				System.out.print("Enter Book ID: ");
				int id = sc.nextInt();
				sc.nextLine();

				System.out.print("Enter Title: ");
				String title = sc.nextLine();

				System.out.print("Enter Author: ");
				String author = sc.nextLine();

				System.out.print("Enter Price: ");
				double price = sc.nextDouble();

				Book newBook = new Book(id, title, author, price);

				// putIfAbsent() adds the book only if ID does not already exist
				if (books.putIfAbsent(id, newBook) == null) {
					System.out.println("Book added successfully!");
				} else {
					System.out.println("Book ID already exists!");
				}

				break;

			case 2:
				if (books.isEmpty()) {
					System.out.println("No books available.");
				} else {

					System.out.println("\n===== All Books =====");

					// entrySet() gives both key and value
					for (Map.Entry<Integer, Book> entry : books.entrySet()) {

						Book b = entry.getValue();
						b.displayBook();
					}
				}

				break;

			case 3:
				System.out.print("Enter Book ID to search: ");
				int searchId = sc.nextInt();

				if (books.containsKey(searchId)) {

					Book b = books.get(searchId);

					System.out.println("\nBook Found:");
					b.displayBook();

				} else {
					System.out.println("Book not found.");
				}

				break;

			case 4:
				System.out.print("Enter Book ID to update: ");
				int updateId = sc.nextInt();
				sc.nextLine();

				if (books.containsKey(updateId)) {

					System.out.print("Enter New Title: ");
					String newTitle = sc.nextLine();

					System.out.print("Enter New Author: ");
					String newAuthor = sc.nextLine();

					System.out.print("Enter New Price: ");
					double newPrice = sc.nextDouble();

					Book updatedBook = new Book(updateId, newTitle, newAuthor, newPrice);

					// put() replaces the existing value
					books.put(updateId, updatedBook);

					System.out.println("Book updated successfully!");

				} else {
					System.out.println("Book not found.");
				}

				break;

			case 5:
				System.out.print("Enter Book ID to delete: ");
				int deleteId = sc.nextInt();

				if (books.containsKey(deleteId)) {

					// remove() removes the book using its key
					books.remove(deleteId);

					System.out.println("Book deleted successfully!");

				} else {
					System.out.println("Book not found.");
				}

				break;

			case 6:
				System.out.println("Thank you for using Book Management System!");

				sc.close();
				return;

			default:
				System.out.println("Invalid choice! Please try again.");
			}
		}
	}

}
