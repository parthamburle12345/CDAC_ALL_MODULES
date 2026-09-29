package assignment2;

import java.util.*;

public class ElectricityBillCalculation {

	static double calculateBill(int unit) {
		double bill = 0.00;
		if ((unit > 0) && (unit <= 100)) {
			bill = unit * 2;
		} else if (unit > 100 && unit <= 200) {
			bill = unit * 3;
		} else if (unit > 200 && unit <= 300) {
			bill = unit * 5;
		} else {
			bill = unit * 7;
		}
		return bill;
	}

	public static void main(String[] args) {

		int unit;
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter unit");
		unit = sc.nextInt();
		System.out.println("Electicity bill is " + calculateBill(unit));
	}

}
