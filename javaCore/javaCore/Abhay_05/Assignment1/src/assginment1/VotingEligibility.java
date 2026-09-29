package assginment1;

import java.util.*;

public class VotingEligibility {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the age");
		int age = sc.nextInt();

		if (age >= 18) {
			System.out.println("Person is eligibile");
		} else {
			System.out.println("Person is not eligibile");
		}

	}

}