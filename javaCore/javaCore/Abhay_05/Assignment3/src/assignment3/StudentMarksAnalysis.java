package assignment3;

import java.util.*;

public class StudentMarksAnalysis {
	public static int findMaxMarks(int[] arr) {
		int maxi = Integer.MIN_VALUE;

		for (int i = 0; i < arr.length; i++) {
			if (maxi < arr[i]) {
				maxi = arr[i];
			}
		}

		return maxi;
	}

	public static int findMinMarks(int[] arr) {
		int mini = Integer.MAX_VALUE;

		for (int i = 0; i < arr.length; i++) {
			if (mini > arr[i]) {
				mini = arr[i];
			}
		}

		return mini;
	}

	public static int totalMarks(int[] arr) {
		int total = 0;

		for (int i = 0; i < arr.length; i++) {
			total += arr[i];
		}

		return total;
	}

	public static float avgMarks(int[] arr, int n) {
		int total = totalMarks(arr);

		return total / n;
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

		int maxi = findMaxMarks(arr);
		int mini = findMinMarks(arr);
		int total = totalMarks(arr);
		float avg = avgMarks(arr, n);

		System.out.println("Maximum marks is : " + maxi);
		System.out.println("Minimum marks is : " + mini);
		System.out.println("Total marks is : " + total);
		System.out.println("Avg marks is : " + avg);

	}
}
