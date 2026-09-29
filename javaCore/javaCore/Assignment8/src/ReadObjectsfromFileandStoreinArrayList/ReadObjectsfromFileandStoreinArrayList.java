package ReadObjectsfromFileandStoreinArrayList;

import java.io.*;
import java.util.*;

class Book implements Serializable {
	private static final long serialVersionUID = 1L;

	int bookId;
	String title;
	String author;
	double price;

	Book(int bookId, String title, String author, double price) {
		this.bookId = bookId;
		this.title = title;
		this.author = author;
		this.price = price;
	}

	void display() {
		System.out.println("ID: " + bookId + " | Title: " + title + " | Author: " + author + " | Price: ₹" + price);
	}
}

public class ReadObjectsfromFileandStoreinArrayList {
	static ArrayList<Book> books = new ArrayList<>();
	static Scanner sc = new Scanner(System.in);
	static final String FILE_NAME = "books.dat";

	// Write multiple objects
	static void writeBooks() {
		try {
			System.out.print("Enter number of books: ");
			int n = sc.nextInt();
			sc.nextLine();

			ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(FILE_NAME));

			for (int i = 0; i < n; i++) {
				System.out.println("\nEnter details for Book " + (i + 1));

				System.out.print("Book ID: ");
				int id = sc.nextInt();
				sc.nextLine();

				System.out.print("Title: ");
				String title = sc.nextLine();

				System.out.print("Author: ");
				String author = sc.nextLine();

				System.out.print("Price: ");
				double price = sc.nextDouble();
				sc.nextLine();

				Book book = new Book(id, title, author, price);

				oos.writeObject(book);
			}

			oos.close();

			System.out.println("\nBooks written successfully.");

		} catch (IOException e) {
			System.out.println("Error writing books: " + e.getMessage());
		}
	}

	// Read objects into ArrayList
	static void readBooks() {
		books.clear();

		try {
			ObjectInputStream ois = new ObjectInputStream(new FileInputStream(FILE_NAME));

			while (true) {
				try {
					Book book = (Book) ois.readObject();
					books.add(book);
				} catch (EOFException e) {
					break;
				}
			}

			ois.close();

			System.out.println("Books loaded into ArrayList.");

		} catch (FileNotFoundException e) {
			System.out.println("File not found.");
		} catch (Exception e) {
			System.out.println("Error reading books: " + e.getMessage());
		}
	}

	// Display all books
	static void displayBooks() {
		if (books.isEmpty()) {
			System.out.println("No books available.");
			return;
		}

		System.out.println("\n===== ALL BOOKS =====");

		for (Book book : books) {
			book.display();
		}
	}

	// Search book
	static void searchBook() {
		System.out.print("Enter Book ID to search: ");
		int id = sc.nextInt();

		for (Book book : books) {
			if (book.bookId == id) {
				System.out.println("\nBook Found:");
				book.display();
				return;
			}
		}

		System.out.println("Book not found.");
	}

	// Update price
	static void updatePrice() {
		System.out.print("Enter Book ID: ");
		int id = sc.nextInt();

		for (Book book : books) {
			if (book.bookId == id) {
				System.out.print("Enter new price: ");
				double price = sc.nextDouble();

				book.price = price;

				System.out.println("Price updated successfully.");
				return;
			}
		}

		System.out.println("Book not found.");
	}

	// Delete book
	static void deleteBook() {
		System.out.print("Enter Book ID to delete: ");
		int id = sc.nextInt();

		Iterator<Book> iterator = books.iterator();

		while (iterator.hasNext()) {
			Book book = iterator.next();

			if (book.bookId == id) {
				iterator.remove();
				System.out.println("Book deleted successfully.");
				return;
			}
		}

		System.out.println("Book not found.");
	}

	// Display books above ₹500
	static void displayAbove500() {
		boolean found = false;

		System.out.println("\n===== BOOKS ABOVE ₹500 =====");

		for (Book book : books) {
			if (book.price > 500) {
				book.display();
				found = true;
			}
		}

		if (!found) {
			System.out.println("No books above ₹500.");
		}
	}

	// Find most expensive book
	static void mostExpensive() {
		if (books.isEmpty()) {
			System.out.println("No books available.");
			return;
		}

		Book expensive = books.get(0);

		for (Book book : books) {
			if (book.price > expensive.price) {
				expensive = book;
			}
		}

		System.out.println("\n===== MOST EXPENSIVE BOOK =====");
		expensive.display();
	}

	// Sort by price
	static void sortBooks() {
		Collections.sort(books, new Comparator<Book>() {
			@Override
			public int compare(Book b1, Book b2) {
				return Double.compare(b1.price, b2.price);
			}
		});

		System.out.println("Books sorted by price.");
		displayBooks();
	}

	// 8. Count books
	static void bookCount() {
		System.out.println("Total Number of Books: " + books.size());
	}

	// Average price
	static void averagePrice() {
		if (books.isEmpty()) {
			System.out.println("No books available.");
			return;
		}

		double total = 0;

		for (Book book : books) {
			total += book.price;
		}

		double average = total / books.size();

		System.out.println("Average Price: ₹" + average);
	}

	// Save updated ArrayList to file
	static void saveBooks() {
		try {
			ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(FILE_NAME));

			for (Book book : books) {
				oos.writeObject(book);
			}

			oos.close();

			System.out.println("Updated data saved successfully.");

		} catch (IOException e) {
			System.out.println("Error saving data: " + e.getMessage());
		}
	}

	// Read file again and display updated data
	static void readUpdatedData() {
		readBooks();

		System.out.println("\n===== UPDATED BOOK DETAILS =====");
		displayBooks();
	}

	public static void main(String[] args) {

		writeBooks();

		readBooks();

		int choice;

		do {
			System.out.println("\n===== BOOK MANAGEMENT =====");
			System.out.println("1. Display Books");
			System.out.println("2. Search Book");
			System.out.println("3. Update Book Price");
			System.out.println("4. Delete Book");
			System.out.println("5. Display Books Above ₹500");
			System.out.println("6. Find Most Expensive Book");
			System.out.println("7. Sort Books by Price");
			System.out.println("8. Display Book Count");
			System.out.println("9. Calculate Average Price");
			System.out.println("10. Save Updated Data");
			System.out.println("11. Exit");

			System.out.print("\nEnter your choice: ");
			choice = sc.nextInt();

			switch (choice) {

			case 1:
				displayBooks();
				break;

			case 2:
				searchBook();
				break;

			case 3:
				updatePrice();
				break;

			case 4:
				deleteBook();
				break;

			case 5:
				displayAbove500();
				break;

			case 6:
				mostExpensive();
				break;

			case 7:
				sortBooks();
				break;

			case 8:
				bookCount();
				break;

			case 9:
				averagePrice();
				break;

			case 10:
				saveBooks();
				readUpdatedData();
				break;

			case 11:
				System.out.println("Program ended.");
				break;

			default:
				System.out.println("Invalid choice.");
			}

		} while (choice != 11);

		sc.close();
	}
}
