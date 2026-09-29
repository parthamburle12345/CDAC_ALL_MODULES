package assignment3;

import java.util.*;

public class CountEvenandOddNumbers {
	public static int evenNo(int[] arr, int n) {
		int count = 0;
		for (int i = 0; i < n; i++) {
			if (arr[i] % 2 == 0)
				count++;
		}
		return count;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the size of the array ");
		int n = sc.nextInt();
		int[] arr = new int[n];

		System.out.println("Enter the array ");

		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		int even = evenNo(arr, n);
		int oddn = n - even;

		System.out.println("Even no in array :" + even);
		System.out.println("Odd no in array :" + oddn);
	}
}
