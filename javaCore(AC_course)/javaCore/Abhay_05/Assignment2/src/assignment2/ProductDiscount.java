package assignment2;

import java.util.*;

public class ProductDiscount {
	static double calculateFinalPrice(double price) {
		double discount;

		if (price >= 10000) {
			discount = price * 0.20;
		} else if (price >= 5000) {
			discount = price * 0.10;
		} else if (price >= 2000) {
			discount = price * 0.05;
		} else {
			discount = 0;
		}

		return price - discount;
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int productId;
		String productName;
		double price, finalPrice;

		System.out.print("Enter Product ID: ");
		productId = sc.nextInt();

		sc.nextLine();
		System.out.print("Enter Product Name: ");
		productName = sc.nextLine();

		System.out.print("Enter Price: ");
		price = sc.nextDouble();

		finalPrice = calculateFinalPrice(price);

		System.out.println("\n Product Details ");
		System.out.println("Product ID: " + productId);
		System.out.println("Product Name: " + productName);
		System.out.println("Original Price: ₹" + price);
		System.out.println("Final Price: ₹" + finalPrice);
	}
}
