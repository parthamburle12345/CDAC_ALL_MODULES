package vehicleRental;

public class Vehicle {
	int vehicle;
	String brand;
	double baseRate;
	
	public Vehicle(int vehicle, String brand, double baseRate) {
		this.vehicle = vehicle;
		this.brand = brand;
		this.baseRate = baseRate;
	}
	
	public void calculateRental() {
		//double price = baseRate * 100;
	}
 }

class Car extends Vehicle{
	int numberOfDays;
	double insuranceCharge;
	
	public Car(int vehicle, String brand, double baseRate, int numberOfDays, double insuranceCharge) {
		super(vehicle, brand, baseRate);
		this.numberOfDays = numberOfDays;
		this.insuranceCharge = insuranceCharge;
	}

	@Override
	public void calculateRental() {
		super.calculateRental();
			double price = insuranceCharge * numberOfDays; // formulas by own and printed bass
			System.out.println("Rental charges: " + price);
		
		
	}
}
	
class Bike extends Vehicle{
	
	int numberOfDays;
	double helmateCharge;
	
	public Bike(int vehicle, String brand, double baseRate, int numberOfDays, double helmateCharge) {
		super(vehicle, brand, baseRate);
		this.numberOfDays = numberOfDays;
		this.helmateCharge = helmateCharge;
	}

	@Override
	public void calculateRental() {
		super.calculateRental();
		double rentalAmount = (numberOfDays*baseRate) + helmateCharge;
		System.out.println("Rental Amount : "+ rentalAmount);
	
	}
	
}


	
	
	
