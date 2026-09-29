package com.cdac;

public class Emp 
{

	int empno;
	String name;
	Address add;
	public Emp(int empno, String name, Address add) {
		
		this.empno = empno;
		this.name = name;
		this.add = add;
	}
	
	void displayEmplyee()
	{
		System.out.print(empno+name);
		add.displayAddress();
	}
	
	
}
