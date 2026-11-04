package Inheritance_Overriding_VehicleRentalSystem;

class Vehicle {
	String vehicleNumber;
	String brand;
	double rentPerDay;

	Vehicle(String vehicleNumber, String brand, double rentPerDay) {
		this.vehicleNumber = vehicleNumber;
		this.brand = brand;
		this.rentPerDay = rentPerDay;
	}

	double calculateRental(int days) {
		return rentPerDay * days;
	}

	void displayDetails() {
		System.out.println("Vehicle Number: " + vehicleNumber);
		System.out.println("Brand: " + brand);
		System.out.println("Rent Per Day: ₹" + rentPerDay);
	}
}

class Car extends Vehicle {
	int numberOfSeats;
	double insuranceCharge;

	Car(String vehicleNumber, String brand, double rentPerDay, int numberOfSeats, double insuranceCharge) {

		super(vehicleNumber, brand, rentPerDay);
		this.numberOfSeats = numberOfSeats;
		this.insuranceCharge = insuranceCharge;
	}

	@Override
	double calculateRental(int days) {
		return (rentPerDay * days) + insuranceCharge;
	}

	void displayDetails() {
		super.displayDetails();
		System.out.println("Number of Seats: " + numberOfSeats);
		System.out.println("Insurance Charge: ₹" + insuranceCharge);
	}
}

class Bike extends Vehicle {
	int helmetCount;
	double maintenanceCharge;

	Bike(String vehicleNumber, String brand, double rentPerDay, int helmetCount, double maintenanceCharge) {

		super(vehicleNumber, brand, rentPerDay);
		this.helmetCount = helmetCount;
		this.maintenanceCharge = maintenanceCharge;
	}

	@Override
	double calculateRental(int days) {
		return (rentPerDay * days) + maintenanceCharge;
	}

	void displayDetails() {
		super.displayDetails();
		System.out.println("Helmet Count: " + helmetCount);
		System.out.println("Maintenance Charge: ₹" + maintenanceCharge);
	}
}

public class VehicleRentalSystem {
	public static void main(String[] args) {

		Car car = new Car("TN01AB1234", "Toyota", 2000, 5, 500);

		Bike bike = new Bike("TN02XY5678", "Honda", 800, 2, 200);

		int carDays = 3;
		int bikeDays = 4;

		System.out.println(" CAR DETAILS ");
		car.displayDetails();
		System.out.println("Number of Days: " + carDays);
		System.out.println("Total Rental Amount: ₹" + car.calculateRental(carDays));

		System.out.println("\n BIKE DETAILS ");
		bike.displayDetails();
		System.out.println("Number of Days: " + bikeDays);
		System.out.println("Total Rental Amount: ₹" + bike.calculateRental(bikeDays));
	}

}
