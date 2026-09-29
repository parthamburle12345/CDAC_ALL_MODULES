package MethodOverloading_FoodDeliveryBill;

class FoodOrder {

	double calculateBill(double foodPrice) {
		return foodPrice;
	}

	double calculateBill(double foodPrice, int quantity) {
		return foodPrice * quantity;
	}

	double calculateBill(double foodPrice, int quantity, double deliveryCharge) {
		return (foodPrice * quantity) + deliveryCharge;
	}
}

public class FoodDeliveryBill {
	public static void main(String[] args) {

		FoodOrder order = new FoodOrder();

		double bill1 = order.calculateBill(250.0);

		double bill2 = order.calculateBill(150.0, 3);

		double bill3 = order.calculateBill(200.0, 2, 50.0);

		System.out.println("Bill for single item: ₹" + bill1);
		System.out.println("Bill for quantity: ₹" + bill2);
		System.out.println("Bill including delivery: ₹" + bill3);
	}
}
