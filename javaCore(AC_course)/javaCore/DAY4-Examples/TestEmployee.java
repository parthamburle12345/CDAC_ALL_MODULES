package com.cdac;

public class TestEmployee
{

	public static void main(String[] args) 
	{
	
		Employee e1 = new Employee(1001,"shan",3000);
		
		e1.Employeedisplay();
		e1.findcomission();
		
		Employee e2 = new Employee(1002,"raj",4000);
		
		e2.Employeedisplay();
		e2.findcomission();
		Employee e3 = new Employee(1003,"suresh",6000);
		
		e3.Employeedisplay();
		e3.findcomission();
		
	}
	
}
