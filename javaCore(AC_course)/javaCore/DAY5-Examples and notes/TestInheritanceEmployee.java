package com.cdac;
class Emp
{
	
	int empno;
	String name;
	float sal;
	
	public Emp(int empno, String name, float sal) 
	{
		
		this.empno = empno;
		this.name = name;
		this.sal = sal;
	}
	
	void displayEmployee()
	{
		System.out.print(empno+name+sal);
	}
	
		
	
}


class Developer extends Emp
{
	

	String project;
	
	Developer(int empno,String name,float sal,String project)
	{
		super(empno,name,sal);
		this.project = project;
	}
	
	void displayDeveloper()
	{
		System.out.println(project);
	}
	
	
	
}





public class TestInheritanceEmployee 
{

	public static void main(String[] args) 
	{
	   
	   
		Developer d = new Developer(1001,"shan",3000,"nsm");
		d.displayEmployee();
		d.displayDeveloper();
		
	}
}
