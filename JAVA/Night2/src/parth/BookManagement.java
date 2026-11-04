package parth;

import java.util.ArrayList;
import java.util.Scanner;

public class BookManagement {
	ArrayList<Book>ali = new ArrayList<>();
	Scanner sc = new Scanner(System.in);
	
	public void addBook() {
		System.out.println("Enter a book Id:");
		int id=sc.nextInt();
		
		System.out.println("Enter Title:");
		String title=sc.next();
		
		System.out.println("Enter Price:");
		float price=sc.nextFloat();
		
		System.out.println("Enter Author Name:");
		String author=sc.next();
		
		Book b=new Book(id,title,author,price);
		ali.add(b);
	}

	public void displayBook() {
		if(ali.isEmpty()) {
			System.out.println("ArrayList is Empty");
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
			System.out.println("No book is ArrayList.");
		}else {
			System.out.println("Enter book id:");
			int id = sc.nextInt();
			for (Book b1:ali)
				if (id == b1.getBookid()) {
					found = true;
					System.out.println(b1.toString());
		}
		if(found == false) {
			System.out.println("Book not found!");
		}
	}
		
	}

	public void updateBook() {
		
		boolean found=false;
		if(ali.isEmpty()) {
			System.out.println("No itme in the ArrayList!");
		}else {
			System.out.println("Enter the book id which you want to update:");
			int id=sc.nextInt();
			for(Book b1:ali) {
				if(id==b1.getBookid()) {
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
					}
			}if(found==false) {
				System.out.println("Book is not found ");
			}
		}
}

	public void deleteBook() {
		boolean found=false;
		// TODO Auto-generated method stub
		if(ali.isEmpty()) {
			System.out.println("ArrayList is Empty:");
		}else {
			System.out.println("Enter id book !");
			int id=sc.nextInt();
			for(int i=0;i<ali.size();i++) {
				Book b=ali.get(i);
				if(id==b.getBookid()) {
					ali.remove(i);
					found=true;
					System.out.println("Book deleted from arraylist:");
				}
			}if(found==false) {
				System.out.println("Book is Not Found");
			}
		}
	}
}
	



class Book{
	
	private int bookid;
	private String title;
	private String author;
	private float price;
	public Book(int bookid, String title, String author, float price) {
		this.bookid = bookid;
		this.title = title;
		this.author = author;
		this.price= price;
	}
	public int getBookid() {
		return bookid;
	}
	public void setBookid(int bookid) {
		this.bookid = bookid;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getAuthor() {
		return author;
	}
	public void setAuthor(String author) {
		this.author = author;
	}
	public float isPrice() {
		return price;
	}
	public void setPrice(float price) {
		this.price = price;
	}
	
	public void display() {
		System.out.println("Book Id: "+ bookid);
		System.out.println("Title : "+ title);
		System.out.println("Price :"+ price);
		System.out.println("Author : "+ author);
	}
}

