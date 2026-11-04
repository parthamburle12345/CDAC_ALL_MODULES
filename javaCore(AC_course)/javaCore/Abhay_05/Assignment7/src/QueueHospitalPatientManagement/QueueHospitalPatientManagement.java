package QueueHospitalPatientManagement;

import java.util.*;

public class QueueHospitalPatientManagement {
	public static void main(String[] args) {
		Queue<String> patients = new LinkedList<>();
		Scanner sc = new Scanner(System.in);

		int choice;

		while (true) {
			System.out.println("\n--- Hospital Patient Management ---");
			System.out.println("1. Add Patient");
			System.out.println("2. Treat Patient");
			System.out.println("3. View Next Patient");
			System.out.println("4. Display Waiting Patients");
			System.out.println("5. Exit");
			System.out.print("Enter your choice: ");
			choice = sc.nextInt();
			sc.nextLine();

			switch (choice) {
			case 1:
				System.out.print("Enter patient name: ");
				String patient = sc.nextLine();
				patients.offer(patient);
				System.out.println("Patient added to waiting queue.");
				break;

			case 2:
				if (!patients.isEmpty()) {
					System.out.println("Treating patient: " + patients.poll());
				} else {
					System.out.println("No patients waiting.");
				}
				break;

			case 3:
				if (!patients.isEmpty()) {
					System.out.println("Next patient: " + patients.peek());
				} else {
					System.out.println("No patients waiting.");
				}
				break;

			case 4:
				if (patients.isEmpty()) {
					System.out.println("No patients waiting.");
				} else {
					System.out.println("Waiting Patients: " + patients);
				}
				break;

			case 5:
				System.out.println("Exiting program...");
				break;

			default:
				System.out.println("Invalid choice.");
			}

		}

	}
}
