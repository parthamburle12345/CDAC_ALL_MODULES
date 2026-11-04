package CustomExceptionAgeValidation;

import java.util.*;

class InvalidAgeException extends Exception {
	InvalidAgeException(String message) {
		super(message);
	}
}

public class CustomExceptionAgeValidation {

	static void validateAge(int age) throws InvalidAgeException {
		if (age < 18) {
			throw new InvalidAgeException("Age should be above 18");
		}

		System.out.println("Age is vaild. Registration allowed");
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.println("Enter Age");
		int age = sc.nextInt();

		try {
			validateAge(age);
		} catch (InvalidAgeException e) {
			System.out.println(e.getMessage());
		}
	}

}
