package com.cdac;

public class Employee
{

	int empno;
	String name;
	float sal;
	
	Employee(int no,String na,float sa)
	{
		empno = no;
		name = na;
		sal = sa;
			
	}
	
	void display()
	{
		System.out.println(empno+name+sal);
	}
	
	
}
