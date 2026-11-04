package EmployeeDetailsUsingMethod;

public class Employee {
	int empId;
	String empName;
	double salary;

	void read(int id, String name, double sal) {
		empId = id;
		empName = name;
		salary = sal;
	}

	void calculateBonus() {
		double bonus;
		if (salary >= 50000) {
			bonus = salary * 0.1;
		} else {
			bonus = salary * 0.5;
		}
		System.out.println("Bonus is : " + bonus);
		System.out.println();
	}

	void display() {
		System.out.println("Employee Id is : " + empId);
		System.out.println("Employee Name is : " + empName);
		System.out.println("Employee salary is : " + salary);

	}

}
