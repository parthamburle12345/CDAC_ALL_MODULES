package assignment3;

import java.util.Scanner;

public class MultiplicationTable {
	public static int multi(int n, int i) {
		int product = n * i;
		return product;

	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the table No: ");
		int n = sc.nextInt();
		for (int i = 1; i <= 10; i++) {
			int result = multi(n, i);
			System.out.println(n + " * " + i + " = " + result);
		}
	}
}
