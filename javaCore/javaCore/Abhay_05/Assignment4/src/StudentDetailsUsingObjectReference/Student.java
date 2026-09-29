package StudentDetailsUsingObjectReference;

public class Student {
	int rollNo;
	String name;
	float marks;

	void dispaly() {
		System.out.println("roll number is " + rollNo);
		System.out.println("name is " + name);
		System.out.println("marks are " + marks);
	}

	void calculateGrade() {
		if (marks >= 90) {
			System.out.println("Grade is " + "Ä");
		} else if (marks >= 75 && marks < 90) {
			System.out.println("Grade is " + "B");
		} else if (marks >= 60 && marks < 75) {
			System.out.println("Grade is " + "C");
		} else {
			System.out.println("Grade is " + "D");
		}
	}

}
