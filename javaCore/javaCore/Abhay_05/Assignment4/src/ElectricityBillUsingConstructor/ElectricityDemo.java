package ElectricityBillUsingConstructor;

public class ElectricityDemo {
	public static void main(String[] args) {

		ElectricityBill e1 = new ElectricityBill(1001, "Ravi", 250);

		ElectricityBill e2 = new ElectricityBill(1002, "Rahul", 80);

		ElectricityBill e3 = new ElectricityBill(1003, "Amit", 150);

		ElectricityBill e4 = new ElectricityBill(1004, "Harsh", 300);

		ElectricityBill e5 = new ElectricityBill(1005, "Abhay", 400);

		e1.display();
		e1.calculateBill();

		e2.display();
		e2.calculateBill();

		e3.display();
		e3.calculateBill();

		e4.display();
		e4.calculateBill();

		e5.display();
		e5.calculateBill();
	}
}
