package com.cdac;

public class BookManagement {

	public void addBook() {
		
	}

	
}
class Book{
private int bookid; // accessModifier datatype variableName or identifier
private String title;
private String author;
private boolean price;
public Book(int bookid, String title, String author, boolean price) {

	this.bookid = bookid;
	this.title = title;
	this.author = author;
	this.price = price;
}//para. constructor


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
public boolean isPrice() {
	return price;
}
public void setPrice(boolean price) {
	this.price = price;
}


public void display() {
	System.out.println("Book Id: "+ bookid);
	System.out.println("Title : "+ title);
	System.out.println("Price :"+ price);
	System.out.println("Author : "+ author);
}

}

