package StudentDetailsUsingObjectReference;

public class StudentDemo {
	public static void main(String[] args) {
		Student s1 = new Student();
		Student s2 = new Student();
		Student s3 = new Student();
		
		s1.rollNo = 101;
		s1.name = "Rahul";
		s1.marks = 85;

		s2.rollNo = 102;
		s2.name = "Rahul Kumar";
		s2.marks = 95;

		s3.rollNo = 103;
		s3.name = "Harsh";
		s3.marks = 90;

		s1.dispaly();
		s1.calculateGrade();
		
		s2.dispaly();
		s2.calculateGrade();
		
		s3.dispaly();
		s3.calculateGrade();
		
	}

}
