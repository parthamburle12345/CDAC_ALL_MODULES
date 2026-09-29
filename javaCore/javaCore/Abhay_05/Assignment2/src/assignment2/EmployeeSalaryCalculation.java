package assignment2;

import java.util.Scanner;

public class EmployeeSalaryCalculation {
	static double calculateSalary(double basicSalary) {
		double hra;

		if (basicSalary >= 50000) {
			hra = basicSalary * 20 / 100;
		} else {
			hra = basicSalary * 10 / 100;
		}

		return basicSalary + hra;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		System.out.print("Enter basic salary: ");
		double basicSalary = sc.nextDouble();

		double finalSalary = calculateSalary(basicSalary);

		System.out.println("Final Salary = " + finalSalary);
	}
}
