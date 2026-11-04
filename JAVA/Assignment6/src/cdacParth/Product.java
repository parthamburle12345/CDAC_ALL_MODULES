package cdacParth;

import java.util.Scanner;

public class Product {

	int productID;
	String productName;
	float price;
	
	public Product(int productID, String productName, float price) {
		this.productID = productID;
		this.productName = productName;
		this.price = price;
	}
	
	double calculatePrice() {
		return price;
		
	}
	
	double calculatePrice(int quantity) {
		return quantity * price;
		
	}
	
	double calculatePrice(int quantity, double discount) {
	    double total = quantity * price;
	    double discountAmount = total * discount / 100;
	    return total - discountAmount;
	}



	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter Product ID:");
		int productID = sc.nextInt();
		
		sc.nextLine();

		System.out.println("Enter Product Name:");
		String productName = sc.nextLine();
		
		System.out.println("Enter Product Price:");
		float price = sc.nextFloat();
		
		Product p = new Product(productID, productName, price);
	
		System.out.println("Product ID: " + p.productID);
		System.out.println("Product Name: " + p.productName);
		System.out.println("Product Price: Rs. " + p.price);

		System.out.println("Price of one product: Rs. "+ p.calculatePrice());

		System.out.println("Total price for 3 products: Rs. "+ p.calculatePrice(3));

		System.out.println("Total price for 3 products after 10% discount: Rs. "+ p.calculatePrice(3, 10));
	}
}
