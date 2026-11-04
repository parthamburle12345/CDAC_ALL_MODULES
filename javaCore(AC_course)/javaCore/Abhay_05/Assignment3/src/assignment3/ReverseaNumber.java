package assignment3;

import java.util.*;

public class ReverseaNumber {

	public static int reverse(int a) {
		int temp = a;
		int sum = 0;
		while (temp != 0) {
			int rem = temp % 10;
			sum = sum * 10 + rem;
			temp = temp / 10;
		}
		return sum;
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the number");
		int a = sc.nextInt();
		int result = reverse(a);

		System.out.println("reverse number is :" + result);
	}
}
