package assignment3;

import java.util.Scanner;

public class SimpleCalculator {

	public static double calculator(float num1, float num2, char ch) {
		if (ch == '+')
			return num1 + num2;
		else if (ch == '-')
			return num1 - num2;
		else if (ch == '*')
			return num1 * num2;
		else if (ch == '/')
			return num1 / num2;
		else
			return num1 % num2;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the large no. :");
		float n1 = sc.nextFloat();
		System.out.println("Enter the smaller no. :");
		float n2 = sc.nextFloat();
		System.out.println("Enter the operator: ");
		char ch = sc.next().charAt(0);

		double result = calculator(n1, n2, ch);
		System.out.println(n1 + " " + ch + " " + n2 + " = " + result);
	}
}
