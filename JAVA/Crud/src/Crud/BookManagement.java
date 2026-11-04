package Crud;

import java.util.ArrayList;
import java.util.Scanner;

public class BookManagement {

	ArrayList<Book > ali = new ArrayList<>();
	Scanner sc = new Scanner(System.in);
	
	public void addBook() {
		System.out.println("Enter book Id:");
		int id = sc.nextInt();
		
		System.out.println("Enter title:");
		String title = sc.next();
		
		System.out.println("Enter Price:");
		float price = sc.nextFloat();
		
		System.out.println("Author Name:");
		String author = sc.next();
		
		Book b = new Book(id,title,price,author);
		ali.add(b);
	}

	public void displayBook() {
		if(ali.isEmpty()) {
			System.out.println("Array List is empty.");
		}
		else {
			for(Book c:ali) {
				System.out.println(c.toString());
			}
		}
		
	}

	public void searchBook() {
		boolean found = false;
		if(ali.isEmpty()) {
			System.out.println("Array list is empty.");
		}
		else {
			System.out.println("Enter book Id:");
			int id = sc.nextInt();
			
			for (Book c:ali) {
				if(id == c.getBookId()) {
					found = true;
					System.out.println(c.toString());
					break;
				}
			}
		if (found == false) {
			System.out.println("Book not found !");
		}
		}
	}

	
	public void updateBook() {
		// TODO Auto-generated method stub
		boolean found=false;
		if(ali.isEmpty()) {
			System.out.println("No itme in the ArrayList!");
		}
		else {
			System.out.println("Enter the book id which you want to update:");
			int id=sc.nextInt();
			for(Book b1:ali) {
				if(id==b1.getBookId()) {
					sc.nextLine();
					System.out.println("Enter title name of the book ");
					String t=sc.nextLine();
					b1.setTitle(t);
					System.out.println("Enter the price of book");
					float price=sc.nextFloat();
					b1.setPrice(price);
					sc.nextLine();
					System.out.println("Enter the author :");
					String author=sc.nextLine();
					b1.setAuthor(author);
					found=true;
					System.out.println(b1.toString()); 
;				}
			}if(found==false) {
				System.out.println("Book is not found ");
			}
		}
	}

	public void deleteBook() {
		boolean found = false;
		
		if(ali.isEmpty()) {
			System.out.println("array list is empty.");
		}
		else {
			System.out.println("enetr book id to be deleted:");
			int id = sc.nextInt();
			
			for(int i=0;i<ali.size();i++) {
				Book b = ali.get(i);
				
				if(id == b.getBookId()) {
					ali.remove(i);
					found = true;
					System.out.println("Book deleted from araay list");
				}
				
			if(found == false) {
				System.out.println("Book not found!");
			}
				
			}
		}
	}

	
	
	
}
	
	
class Book{
	private int bookId;
	private String title;
	private float price;
	private String author;
	
	public Book(int bookId, String title, float price, String author) {
		this.bookId = bookId;
		this.title = title;
		this.price = price;
		this.author = author;
	}

	public int getBookId() {
		return bookId;
	}

	public void setBookId(int bookId) {
		this.bookId = bookId;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public float getPrice() {
		return price;
	}

	public void setPrice(float price) {
		this.price = price;
	}

	public String getAuthor() {
		return author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	@Override
	public String toString() {
		return "Book [bookId=" + bookId + ", title=" + title + ", price=" + price + ", author=" + author + "]";
	}
	
	
	
}
	
