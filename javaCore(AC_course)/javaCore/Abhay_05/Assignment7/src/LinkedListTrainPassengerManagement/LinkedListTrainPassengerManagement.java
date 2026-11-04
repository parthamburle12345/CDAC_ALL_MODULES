package LinkedListTrainPassengerManagement;

import java.util.*;

public class LinkedListTrainPassengerManagement {
	public static void main(String[] args) {
		LinkedList<String> passengers = new LinkedList<>();
		Scanner sc = new Scanner(System.in);

		int choice;

		while (true) {
			System.out.println("\n--- Train Passenger Management ---");
			System.out.println("1. Add Passenger at Beginning");
			System.out.println("2. Add Passenger at End");
			System.out.println("3. Remove First Passenger");
			System.out.println("4. Remove Last Passenger");
			System.out.println("5. Search Passenger");
			System.out.println("6. Display Passengers");
			System.out.println("7. Exit");
			System.out.print("Enter your choice: ");
			choice = sc.nextInt();
			sc.nextLine();

			switch (choice) {
			case 1:
				System.out.print("Enter passenger name: ");
				String firstPassenger = sc.nextLine();
				passengers.addFirst(firstPassenger);
				System.out.println("Passenger added at beginning.");
				break;

			case 2:
				System.out.print("Enter passenger name: ");
				String lastPassenger = sc.nextLine();
				passengers.addLast(lastPassenger);
				System.out.println("Passenger added at end.");
				break;

			case 3:
				if (!passengers.isEmpty()) {
					System.out.println("Removed passenger: " + passengers.removeFirst());
				} else {
					System.out.println("No passengers available.");
				}
				break;

			case 4:
				if (!passengers.isEmpty()) {
					System.out.println("Removed passenger: " + passengers.removeLast());
				} else {
					System.out.println("No passengers available.");
				}
				break;

			case 5:
				System.out.print("Enter passenger name to search: ");
				String searchName = sc.nextLine();

				if (passengers.contains(searchName)) {
					System.out.println("Passenger found.");
				} else {
					System.out.println("Passenger not found.");
				}
				break;

			case 6:
				if (passengers.isEmpty()) {
					System.out.println("No passengers available.");
				} else {
					System.out.println("Passengers: " + passengers);
				}
				break;

			case 7:
				System.out.println("Exiting program...");
				break;

			default:
				System.out.println("Invalid choice.");
			}

		}
	}
}
