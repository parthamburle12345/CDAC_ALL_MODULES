package vehicleRental;



public class VehicleMain {

	public static void main(String[] args) {
//		Vehicle v = new Vehicle(123, "TVS", 2300);
//		v.calculateRental();
		Car c = new Car(12345, "audi" , 5000, 5 , 1500);
		c.calculateRental();
		
		Bike b = new Bike(0, null, 0, 0, 0);
		b.calculateRental();
	}
	
}
