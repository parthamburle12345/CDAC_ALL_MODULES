package Inheritance_Overriding_TravelBookingSystem;

class TravelBooking {
	int bookingId;
	String passengerName;
	String source;
	String destination;
	double distance;

	TravelBooking(int bookingId, String passengerName, String source, String destination, double distance) {
		this.bookingId = bookingId;
		this.passengerName = passengerName;
		this.source = source;
		this.destination = destination;
		this.distance = distance;
	}

	double calculateFare() {
		return 0;
	}

	void displayDetails() {
		System.out.println("Booking ID: " + bookingId);
		System.out.println("Passenger Name: " + passengerName);
		System.out.println("Source: " + source);
		System.out.println("Destination: " + destination);
		System.out.println("Distance: " + distance + " km");
	}
}

class BusBooking extends TravelBooking {
	String busType;
	int seatNumber;

	BusBooking(int bookingId, String passengerName, String source, String destination, double distance, String busType,
			int seatNumber) {
		super(bookingId, passengerName, source, destination, distance);
		this.busType = busType;
		this.seatNumber = seatNumber;
	}

	@Override
	double calculateFare() {
		double rate;

		if (busType.equalsIgnoreCase("AC")) {
			rate = 3.0;
		} else {
			rate = 2.0;
		}

		return distance * rate;
	}

	void displayDetails() {
		super.displayDetails();
		System.out.println("Bus Type: " + busType);
		System.out.println("Seat Number: " + seatNumber);
		System.out.println("Bus Fare: ₹" + calculateFare());
	}
}

class TrainBooking extends TravelBooking {
	String trainNumber;
	String coachType;

	TrainBooking(int bookingId, String passengerName, String source, String destination, double distance,
			String trainNumber, String coachType) {
		super(bookingId, passengerName, source, destination, distance);
		this.trainNumber = trainNumber;
		this.coachType = coachType;
	}

	@Override
	double calculateFare() {
		double rate;

		if (coachType.equalsIgnoreCase("AC")) {
			rate = 2.5;
		} else {
			rate = 1.5;
		}

		return distance * rate;
	}

	void displayDetails() {
		super.displayDetails();
		System.out.println("Train Number: " + trainNumber);
		System.out.println("Coach Type: " + coachType);
		System.out.println("Train Fare: ₹" + calculateFare());
	}
}

public class TravelBookingSystem {

	public static void main(String[] args) {

		BusBooking bus = new BusBooking(101, "Rahul", "Chennai", "Bangalore", 350, "AC", 12);

		TrainBooking train = new TrainBooking(102, "Priya", "Chennai", "Hyderabad", 630, "12603", "AC");

		System.out.println(" BUS BOOKING ");
		TravelBooking booking;

		booking = bus;
		booking.displayDetails();
		System.out.println("Fare using parent reference: ₹" + booking.calculateFare());

		System.out.println("\n TRAIN BOOKING ");

		booking = train;
		booking.displayDetails();
		System.out.println("Fare using parent reference: ₹" + booking.calculateFare());
	}
}