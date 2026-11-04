package assignment2;

import java.util.*;

public class MobileDataUsage {
	static double calculateCharge(double dataUsed) {

		if (dataUsed <= 1) {
			return 50;
		} else if (dataUsed <= 5) {
			return 100;
		} else if (dataUsed <= 10) {
			return 200;
		} else {

			return 350;
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		System.out.print("Enter mobile number: ");
		long mobileNumber = sc.nextLong();

		System.out.print("Enter data used in GB: ");
		double dataUsed = sc.nextDouble();

		double charge = calculateCharge(dataUsed);

		System.out.println("\nMobile Number: " + mobileNumber);
		System.out.println("Data Used: " + dataUsed + " GB");
		System.out.println("Final Charge: ₹" + charge);
	}
}
