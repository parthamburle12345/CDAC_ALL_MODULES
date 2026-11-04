package examprep;

import java.util.ArrayList;
import java.util.Scanner;
public class BookManagement {
	ArrayList<Book >al=new ArrayList<>();
		// TODO Auto-generated constructor stub
	
	Scanner sc=new Scanner(System.in);
    
	public void addBook() {
		// TODO Auto-generated method stub
		System.out.println("Enter Book Id:");
		int id=sc.nextInt();

		System.out.println("Enter Title");
		String title=sc.next();

		System.out.println("Enter Price:");
		float price=sc.nextFloat();

		System.out.println("Author Name:");
		String author=sc.next();

		//al.add(b);
		Book b=new Book(id,title,price,author);
		al.add(b);
		
	}

	public void displayBook() {
		// TODO Auto-generated method stub
		if (al.isEmpty()){
			System.out.println("ArrayList is Empty");
	}
		else {
			for(Book c:al) {
				System.out.println(c.toString()); 			}
		}
	

}

	public void searchBook() {
		
		boolean found=false;
		if(al.isEmpty()) {
			System.out.println("No book is in ArrayList ");
		}
		else {
		  System.out.println("Enter book id:");
		  int id=sc.nextInt();
		  for(Book b1:al) {
			if(id==b1.getBookId()) {
				found=true;
				System.out.println(b1.toString()); 			}
		}
		if(found==false) {
			System.out.println("Book not found !");
		}
		
		}
		
	}


	public void updateBook() {

		boolean found=false;
		if(al.isEmpty()) {
			System.out.println("No itme in the ArrayList!");
		}else {
			System.out.println("Enter the book id which you want to update:");
			int id=sc.nextInt();
			for(Book b1:al) {
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
		boolean found=false;
		// TODO Auto-generated method stub
		if(al.isEmpty()) {
			System.out.println("ArrayList is Empty:");
		}else {
			System.out.println("Enter id book !");
			int id=sc.nextInt();
			for(int i=0;i<al.size();i++) {
				Book b=al.get(i);
				if(id==b.getBookId()) {
					al.remove(i);
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
	private int bookId;
	private String title;
	private float price;
	private String author;
	public Book(int bookId, String title, float price, String author) {
		super();s
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
	public void setAuthor(Strin	g author) {
		this.author = author;
	}
	@Override
	public String toString() {
		return "Book [bookId=" + bookId + ", title=" + title + ", price=" + price + ", author=" + author + "]";
	}
//	void displayBook() {
//		System.out.println("Book Id is: "+bookId);
//		System.out.println("Title of the book: "+title);
//		System.out.println("Price of the book: "+price);
//		System.out.println("Author Name :"+author);
//	}
	
}
