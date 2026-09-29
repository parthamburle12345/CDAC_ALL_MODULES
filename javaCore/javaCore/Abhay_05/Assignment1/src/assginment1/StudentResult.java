package assginment1;

import java.util.*;

public class StudentResult {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the marks");
		int marks = sc.nextInt();

		if (marks >= 40) {
			System.out.println("Student has passed");
		} else {
			System.out.println("Student has failed");
		}
	}

}
