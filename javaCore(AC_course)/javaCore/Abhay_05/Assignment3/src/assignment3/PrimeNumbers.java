package assignment3;

import java.util.Scanner;

public class PrimeNumbers {

	public static int primeNo(int num) {
		int a = num;
		for (int i = 2; i <= a / 2; i++) {
			if (num % i == 0) {
				return -1;
			}
		}
		return num;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the Number: ");
		int num = sc.nextInt();
		for (int i = 2; i <= num; i++) {
			int result = primeNo(i);
			if (result == i)
				System.out.println("prime No is " + result);

		}
	}
}

