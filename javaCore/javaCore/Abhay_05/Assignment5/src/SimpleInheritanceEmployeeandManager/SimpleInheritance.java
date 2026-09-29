package SimpleInheritanceEmployeeandManager;


class Employee {
	int empId;
	String empName;
	double salary;
	
	static String companyName="DataBricks";

	Employee(int empId, String empName, double salary) {
		this.empId = empId;
		this.empName = empName;
		this.salary = salary;
	}

}

class Manager extends Employee {
	String department;
	int teamSize;

	Manager(int empId, String empName, double salary,String department, int teamSize) {
		super(empId, empName, salary);
		this.department = department;
		this.teamSize = teamSize;
	}
	
	void display() {
		System.out.println(empId+" "+empName+" "+salary+" "+department+" "+teamSize+" "+companyName);
		System.out.println();
		
	}
	
	
}

public class SimpleInheritance {
public static void main(String[] args) {
	
	Manager mc1=new Manager(101,"Rahul",50000,"IT", 10);
	Manager mc2=new Manager(102,"XYZ",5000,"HR", 8);
	Manager mc3=new Manager(103,"ABC",100000,"Developer", 12);
	
	mc1.display();
	mc2.display();
	mc3.display();
}
}

