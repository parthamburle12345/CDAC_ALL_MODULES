package abstraction;

public class VehicleMain {
	public static void main(String[] args) {
		Car c = new Car(101, "Tata", 2000, 5, 500);
		
		c.displayVehicleDetails();
		c.displayCarDetails();
		c.calculateRental(3);
	}
}
