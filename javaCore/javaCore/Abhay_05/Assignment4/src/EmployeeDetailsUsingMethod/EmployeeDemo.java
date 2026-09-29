package EmployeeDetailsUsingMethod;

public class EmployeeDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Employee e1 = new Employee();
		Employee e2 = new Employee();
		Employee e3 = new Employee();
		Employee e4 = new Employee();

		e1.read(101, "rahul", 30000.0);
		e2.read(102, "harsh", 50000.0);
		e3.read(103, "abhay", 60000.0);
		e4.read(104, "mishra", 40000.0);

		e1.display();
		e1.calculateBonus();

		e2.display();
		e2.calculateBonus();

		e3.display();
		e3.calculateBonus();

		e4.display();
		e4.calculateBonus();

	}

}
