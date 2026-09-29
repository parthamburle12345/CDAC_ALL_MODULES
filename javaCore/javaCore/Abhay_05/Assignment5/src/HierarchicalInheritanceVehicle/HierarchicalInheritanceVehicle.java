package HierarchicalInheritanceVehicle;

class Vehicle {
	String vehicleNo;
	String brand;
	double price;

	static String dealerName = "ABC Motors";

	Vehicle(String vehicleNo, String brand, double price) {
		this.vehicleNo = vehicleNo;
		this.brand = brand;
		this.price = price;
	}

	void displayDetails() {
		System.out.println("Dealer Name : " + dealerName);
		System.out.println("Vehicle No  : " + vehicleNo);
		System.out.println("Brand       : " + brand);
		System.out.println("Price       : ₹" + price);
	}
}

class Car extends Vehicle {
	int numberOfDoors;
	String fuelType;

	Car(String vehicleNo, String brand, double price, int numberOfDoors, String fuelType) {

		super(vehicleNo, brand, price);
		this.numberOfDoors = numberOfDoors;
		this.fuelType = fuelType;
	}

	double calculateInsurance() {
		return price * 0.08;
	}

	void displayCarDetails() {
		displayDetails();
		System.out.println("Number of Doors : " + numberOfDoors);
		System.out.println("Fuel Type       : " + fuelType);
		System.out.println("Insurance (8%)  : ₹" + calculateInsurance());
		System.out.println("Final Price     : ₹" + (price + calculateInsurance()));
		System.out.println();
	}
}

class Bike extends Vehicle {
	int engineCC;
	boolean helmetIncluded;

	Bike(String vehicleNo, String brand, double price, int engineCC, boolean helmetIncluded) {

		super(vehicleNo, brand, price);
		this.engineCC = engineCC;
		this.helmetIncluded = helmetIncluded;
	}

	double calculateInsurance() {
		return price * 0.05;
	}

	void displayBikeDetails() {
		displayDetails();
		System.out.println("Engine CC       : " + engineCC);
		System.out.println("Helmet Included : " + helmetIncluded);
		System.out.println("Insurance (5%)  : ₹" + calculateInsurance());
		System.out.println("Final Price     : ₹" + (price + calculateInsurance()));
		System.out.println();
	}
}

public class HierarchicalInheritanceVehicle {
	public static void main(String[] args) {

		Car car1 = new Car("CAR101", "Toyota", 800000, 4, "Petrol");

		Car car2 = new Car("CAR102", "Hyundai", 950000, 4, "Diesel");

		Bike bike1 = new Bike("BIKE101", "Honda", 120000, 150, true);

		Bike bike2 = new Bike("BIKE102", "Yamaha", 180000, 200, true);

		System.out.println("CAR 1");
		car1.displayCarDetails();

		System.out.println("CAR 2");
		car2.displayCarDetails();

		System.out.println("BIKE 1");
		bike1.displayBikeDetails();

		System.out.println("BIKE 2");
		bike2.displayBikeDetails();
	}
}
