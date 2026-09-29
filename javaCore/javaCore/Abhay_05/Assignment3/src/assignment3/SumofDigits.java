package assignment3;

import java.util.Scanner;

public class SumofDigits {
	public static int sumofdigit(int a) {
		int temp = a;
		int sum = 0;
		while (temp != 0) {
			int rem = temp % 10;
			sum = sum + rem;
			temp = temp / 10;
		}
		return sum;
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number");
		int a = sc.nextInt();
		int result = sumofdigit(a);

		System.out.println("sum of a number is :" + result);
	}
}
