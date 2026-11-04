package HAS_ARelationship;

class Book {
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

	void displayBookDetails() {
		System.out.println("Book ID     : " + bookId);
		System.out.println("Title       : " + title);
		System.out.println("Author      : " + author);
		System.out.println("Price       : ₹" + price);
	}
}

class Library {
	String libraryName;
	String location;

	Book book;

	static int totalBooks = 0;

	Library(String libraryName, String location, Book book) {
		this.libraryName = libraryName;
		this.location = location;
		this.book = book;

		totalBooks++;
	}

	void displayDetails() {
		System.out.println("Library Name : " + libraryName);
		System.out.println("Location     : " + location);

		System.out.println("\nBook Details:");
		book.displayBookDetails();

		System.out.println();
	}
}

public class HAS_ARelationship {
	public static void main(String[] args) {

		Book book1 = new Book(101, "Java Programming", "James Gosling", 550);

		Book book2 = new Book(102, "Python Basics", "Guido van Rossum", 450);

		Book book3 = new Book(103, "Data Structures", "Mark Allen Weiss", 600);

		Book book4 = new Book(104, "OOPs with C++", "Sumita Arora", 1200);

		Library library1 = new Library("Central Library", "Chennai", book1);

		Library library2 = new Library("City Library", "Coimbatore", book2);

		Library library3 = new Library("Knowledge Library", "Madurai", book3);

		Library library4 = new Library("Central Library", "Lucknow", book4);

		System.out.println("LIBRARY 1");
		library1.displayDetails();

		System.out.println("LIBRARY 2");
		library2.displayDetails();

		System.out.println("LIBRARY 3");
		library3.displayDetails();

		System.out.println("LIBRARY 4");
		library4.displayDetails();

		System.out.println("Total Books in Libraries : " + Library.totalBooks);
	}
}
