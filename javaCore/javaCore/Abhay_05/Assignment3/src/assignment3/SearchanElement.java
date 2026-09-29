package assignment3;

import java.util.*;

public class SearchanElement {

	public static int searchElement(int[] arr, int key, int n) {
//      binary search
//		int low = 0;
//		int high = n - 1;
//		while (low <= high) {
//			int mid = low + (high - low) / 2;
//			if (arr[mid] == key)
//				return mid + 1;
//			else if (arr[mid] > key)
//				high = mid - 1;
//			else
//				low = mid + 1;
//		}
//		return -1;
		// linear search
		for (int i = 0; i < n; i++) {
			if (arr[i] == key)
				return i + 1;
		}
		return -1;
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

		System.out.println("Enter the key to be searched ");
		int k = sc.nextInt();

//		Arrays.sort(arr);

		int idx = searchElement(arr, k, n);
		if (idx != -1)
			System.out.println("Idx of key element is : " + idx);
		else
			System.out.println("element not present in array.");
	}
}
