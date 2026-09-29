package com.cdac;
class Employee extends Object
{
	int empno;
	String name;
	float salary;
	
 public Employee(int empno, String name, float salary)
 {
		
		this.empno = empno;
		this.name = name;
		this.salary = salary;
	}
	
	
void displayEmployee()
{
	System.out.print(empno+name+salary);
}
	
}

class Developer extends Employee 
{
	String Planguage;

	public Developer(int empno, String name, float salary, String planguage) 
	{
		super(empno,name,salary);
		this.Planguage = planguage;
	}
	
	
  void displayDeveloper()
  {
	  super.displayEmployee();
	  System.out.println(Planguage);
  }
	
		
}


class Tester  extends Employee
{
	
	String tool;

	public Tester(int empno, String name, float salary,String tool)
	{
		super(empno,name,salary);
		this.tool = tool;
	}
	
	
	void displayTester()
	  {
		System.out.println("tester details");
		  super.displayEmployee();
		  System.out.println(tool);
	  }
	
	
	
}




public class TestHierarchicalInheritance
{

	
	public static void main(String[] args) 
	{
		System.out.println("developer details");
		Developer d = new Developer(1001,"shan",30000,"python");
		d.displayDeveloper();
		
		
		
		Tester t = new Tester(1002,"raj",5000,"selenium");
		t.displayTester();
		
	}

}
