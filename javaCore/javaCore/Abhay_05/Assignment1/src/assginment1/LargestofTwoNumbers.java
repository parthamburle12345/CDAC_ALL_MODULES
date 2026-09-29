package assginment1;

import java.util.*;

public class LargestofTwoNumbers {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the First No.");
		int a = sc.nextInt();
		System.out.println("Enter the Second No.");
		int b = sc.nextInt();

		if (a == b) {
			System.out.println("Number are equal");
		} else if (a > b) {
			System.out.println("First no. is larger");
		} else {
			System.out.println("Second no. is larger");
		}
	}

}
