package ProductBillUsingParameterizedConstructor;

public class Product {
	int productId;
	String productName;
	double price;
	int quantity;

	Product(int id, String name, double p, int quant) {
		productId = id;
		productName = name;
		price = p;
		quantity = quant;
	}

	void display() {
		System.out.println("Product ID : " + productId);
		System.out.println("Product Name : " + productName);
		System.out.println("Price : " + price);
		System.out.println("Quantity : " + quantity);
	}

	void calculateBill() {

		double total = price * quantity;
		double discount;

		if (total > 10000) {
			discount = total * 0.10;
		} else {
			discount = 0;
		}

		double finalAmount = total - discount;

		System.out.println("Total Amount : " + total);
		System.out.println("Discount : " + discount);
		System.out.println("Final Amount : " + finalAmount);
		System.out.println();
	}

}
