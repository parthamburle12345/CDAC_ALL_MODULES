package ProductBillUsingParameterizedConstructor;

public class ProductDemo {
	public static void main(String[] args) {

		Product p1 = new Product(101, "Laptop", 50000, 2);
		Product p2 = new Product(102, "Mobile", 20000, 1);
		Product p3 = new Product(103, "Keyboard", 1500, 2);

		p1.display();
		p1.calculateBill();

		p2.display();
		p2.calculateBill();

		p3.display();
		p3.calculateBill();
	}
}
