package assignment3;

import java.util.*;

public class FindMaximumAndMinimum {

	public static int findMax(int[] arr) {
		int maxi = Integer.MIN_VALUE;

		for (int i = 0; i < arr.length; i++) {
			if (maxi < arr[i]) {
				maxi = arr[i];
			}
		}

		return maxi;
	}

	public static int findMin(int[] arr) {
		int mini = Integer.MAX_VALUE;

		for (int i = 0; i < arr.length; i++) {
			if (mini > arr[i]) {
				mini = arr[i];
			}
		}

		return mini;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the size of the array ");
		int n = sc.nextInt();
		int[] arr = new int[n];

		System.out.println("Enter the array ");

		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}

		int maxi = findMax(arr);
		int mini = findMin(arr);

		System.out.println("Maximum number is : " + maxi);
		System.out.println("Minimum number is : " + mini);

	}

}
