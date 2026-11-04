package WriteandReadaBookObject;

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
		System.out.println("Book ID: " + bookId);
		System.out.println("Title: " + title);
		System.out.println("Author: " + author);
		System.out.println("Price: ₹" + price);
	}
}

public class WriteandReadaBookObject {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		try {

			System.out.print("Enter Book ID: ");
			int id = sc.nextInt();
			sc.nextLine();

			System.out.print("Enter Title: ");
			String title = sc.nextLine();

			System.out.print("Enter Author: ");
			String author = sc.nextLine();

			System.out.print("Enter Price: ");
			double price = sc.nextDouble();

			Book book = new Book(id, title, author, price);

			ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("book.dat"));

			oos.writeObject(book);
			oos.close();

			System.out.println("\nBook object written successfully.");

			ObjectInputStream ois = new ObjectInputStream(new FileInputStream("book.dat"));

			Book readBook = (Book) ois.readObject();
			ois.close();

			System.out.println("\nBook Details:");
			readBook.display();

			if (readBook.price > 500) {
				double discount = readBook.price * 0.10;
				double finalPrice = readBook.price - discount;

				System.out.println("\n10% Discount Applied");
				System.out.println("Discount: ₹" + discount);
				System.out.println("Final Price: ₹" + finalPrice);
			} else {
				System.out.println("\nNo discount applied.");
				System.out.println("Final Price: ₹" + readBook.price);
			}

		} catch (Exception e) {
			System.out.println("Error: " + e.getMessage());
		}

		sc.close();
	}
}
