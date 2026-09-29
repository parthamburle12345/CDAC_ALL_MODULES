package assignment2;

import java.util.*;

public class SimpleCalculator {
	static double calculate(double num1, double num2, char operator) {

		if (operator == '+') {
			return num1 + num2;
		} else if (operator == '-') {
			return num1 - num2;
		} else if (operator == '*') {
			return num1 * num2;
		} else if (operator == '/') {
			if (num2 == 0) {
				System.out.println("Error: Division by zero is not allowed.");
				return 0;
			} else {
				return num1 / num2;
			}
		} else {
			System.out.println("Invalid operator.");
			return 0;
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		System.out.print("Enter first number: ");
		double num1 = sc.nextDouble();

		System.out.print("Enter second number: ");
		double num2 = sc.nextDouble();

		System.out.print("Enter operator (+, -, *, /): ");
		char operator = sc.next().charAt(0);

		double result = calculate(num1, num2, operator);

		System.out.println("Result = " + result);
	}

}
