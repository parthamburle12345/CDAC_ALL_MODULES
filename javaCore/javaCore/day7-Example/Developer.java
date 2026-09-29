package com.cdac;

public class Developer extends Employee
{
	
	String project;
	public Developer(int empno, String name, float sal,String project)
    {
		super(empno, name, sal);
		this.project = project;
	}
	
	public void calculateBonous()
	{   //super.calculateBonous();
		float bonous = sal*0.2f;
		System.out.println(bonous);
	}
	
	void displayDeveloper()
	{   super.displayEmployee();
		System.out.println(project);
	}
	
	
}
