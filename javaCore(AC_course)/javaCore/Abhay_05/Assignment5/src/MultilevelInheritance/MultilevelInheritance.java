package MultilevelInheritance;

class Person {
	String name;
	int age;

	Person(String name, int age) {
		this.name = name;
		this.age = age;
	}
}

class Employee extends Person {
	int empId;
	double salary;

	Employee(String name, int age, int empId, double salary) {
		super(name, age);
		this.empId = empId;
		this.salary = salary;
	}
}

class Manager extends Employee {
	String department;
	int teamSize;

	static String organizationName = "Tech Solutions Pvt. Ltd.";

	Manager(String name, int age, int empId, double salary, String department, int teamSize) {

		super(name, age, empId, salary);
		this.department = department;
		this.teamSize = teamSize;
	}

	double calculateAnnualSalary() {
		return salary * 12;
	}

	void displayDetails() {
		System.out.println("Organization : " + organizationName);
		System.out.println("Name         : " + name);
		System.out.println("Age          : " + age);
		System.out.println("Employee ID  : " + empId);
		System.out.println("Monthly Salary: ₹" + salary);
		System.out.println("Department   : " + department);
		System.out.println("Team Size    : " + teamSize);
		System.out.println("Annual Salary: ₹" + calculateAnnualSalary());
		System.out.println();
	}
}

public class MultilevelInheritance {
	public static void main(String[] args) {

		Manager manager1 = new Manager("Rahul", 35, 101, 75000, "Software Development", 10);

		Manager manager2 = new Manager("Priya", 32, 102, 85000, "Human Resources", 8);

		Manager manager3 = new Manager("Arun", 40, 103, 95000, "Finance", 12);
		
		manager1.displayDetails();
		manager2.displayDetails();
		manager3.displayDetails();
	}
}
