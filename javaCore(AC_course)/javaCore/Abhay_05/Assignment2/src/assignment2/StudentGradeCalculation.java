package assignment2;

import java.util.*;

public class StudentGradeCalculation {
	static String calculateGrade(int marks) {
		String grade = "";
		if ((marks >= 90) && (marks <= 100)) {
			grade = "A";
		} else if (marks >= 75 && marks <= 89) {
			grade = "B";
		} else if (marks >= 60 && marks <= 74) {
			grade = "C";
		} else if (marks >= 50 && marks <= 59) {
			grade = "D";
		} else {
			grade = "F";
		}
		return grade;
	}

	public static void main(String[] args) {

		int marks;
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter marks");
		marks = sc.nextInt();
		System.out.println("Student grade is " + calculateGrade(marks));
	}

}
