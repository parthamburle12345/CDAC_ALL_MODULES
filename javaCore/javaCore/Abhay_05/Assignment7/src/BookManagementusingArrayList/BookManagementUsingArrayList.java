package BookManagementusingArrayList;

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
		System.out.println("-------------------------");
	}

}

public class BookManagementUsingArrayList {

	public static void main(String[] args) {

		ArrayList<Book> book = new ArrayList<>();
		Scanner sc = new Scanner(System.in);

		while (true) {
			System.out.println("Enter choice \n1. Add Book\r\n" + "2. Display All Books\r\n"
					+ "3. Search Book by ID\r\n" + "4. Update Book\r\n" + "5. Delete Book\r\n" + "6. Exit ");
			int a = sc.nextInt();

			switch (a) {
			case 1:
				System.out.print("Enter Book ID: ");
				int id = sc.nextInt();

				System.out.print("Enter Title: ");
				String title = sc.nextLine();

				System.out.print("Enter Author: ");
				String author = sc.nextLine();

				System.out.print("Enter Price: ");
				double price = sc.nextDouble();

				Book newBook = new Book(id, title, author, price);
				book.add(newBook); // add is used for adding the element.

				System.out.println("Book added successfully!");
				break;
			case 2:
				if (book.size() == 0) {
					System.out.println("No books available.");
				} else {
					System.out.println("\n===== All Books =====");

					for (int i = 0; i < book.size(); i++) {
						Book b = book.get(i);
						b.displayBook();
					}
				}
				break;
			case 3:
				System.out.print("Enter Book ID to search: ");
				int searchId = sc.nextInt();

				boolean found = false;

				for (int i = 0; i < book.size(); i++) {
					Book b = book.get(i);

					if (b.bookId == searchId) {
						System.out.println("\nBook Found:");
						b.displayBook();
						found = true;
						break;
					}
				}

				if (!found) {
					System.out.println("Book not found.");
				}
				break;
			case 4:
				System.out.print("Enter Book ID to update: ");
				int updateId = sc.nextInt();
//			sc.nextLine();

				boolean updated = false;

				for (int i = 0; i < book.size(); i++) {
					Book b = book.get(i);

					if (b.bookId == updateId) {

						System.out.print("Enter New Title: ");
						String newTitle = sc.nextLine();

						System.out.print("Enter New Author: ");
						String newAuthor = sc.nextLine();

						System.out.print("Enter New Price: ");
						double newPrice = sc.nextDouble();

						Book updatedBook = new Book(updateId, newTitle, newAuthor, newPrice);

						book.set(i, updatedBook);// set is used for update

						System.out.println("Book updated successfully!");
						updated = true;
						break;
					}
				}

				if (!updated) {
					System.out.println("Book not found.");
				}
				break;
			case 5:
				System.out.print("Enter Book ID to delete: ");
				int deleteId = sc.nextInt();

				boolean deleted = false;

				for (int i = 0; i < book.size(); i++) {
					Book b = book.get(i);

					if (b.bookId == deleteId) {
						book.remove(i); // remove is used for delete the element

						System.out.println("Book deleted successfully!");
						deleted = true;
						break;
					}
				}

				if (!deleted) {
					System.out.println("Book not found.");
				}
				break;

			case 6:
				System.out.println("Thank you for using Book Management System!");
				break;

			default:
				System.out.println("Invalid choice! Please try again.");

			}

		}
	}

}
