package abstraction;

public abstract class Vehicle {
	int vehicleNo;
	String Brand;
	int rentalRate;
	public Vehicle(int vehicleNo, String brand, int rentalRate) {
		this.vehicleNo = vehicleNo;
		Brand = brand;
		this.rentalRate = rentalRate;
		
	}
	
	void displayVehicleDetails() {
		System.out.println("Vehicle Number:"+ vehicleNo);
		System.out.println("Brand:" + Brand);
		System.out.println("Rental Rate:" + rentalRate);
		
	} 
	
	abstract void calculateRental(int days);	
}


class Car extends Vehicle{
	int numberOfSeats;
	double insuranceCharges;
	public Car(int vehicleNo, String brand, int rentalRate, int numberOfSeats, double insuranceCharges) {
		super(vehicleNo, brand, rentalRate);
		this.numberOfSeats = numberOfSeats;
		this.insuranceCharges = insuranceCharges;
	}
	@Override
	void calculateRental(int days) {
		double total = (rentalRate * days) + insuranceCharges;
	    System.out.println("Total Rental: " + total);
	}
	void displayCarDetails() {
	    System.out.println("Number of Seats: " + numberOfSeats);
	    System.out.println("Insurance Charges: " + insuranceCharges);
	}
	
	
	
		
}