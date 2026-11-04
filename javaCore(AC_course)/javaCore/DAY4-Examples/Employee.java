package com.cdac;

import java.util.Scanner;

public class Employee 
{

	int empno;
	String ename;
	float sal;
	
	Employee(int no,String na,float sa)
	{
		
		
		empno = no;
		ename = na;
		sal = sa;
		
	}
	
	
	
	void Employeedisplay()
	{
		System.out.print(empno+ename+sal);
	}
	
	
	void findcomission()
	{
		float comm;
		
		if(sal>2000)
		comm = sal*0.02f;
		else
			comm = sal*0.01f;
		
		System.out.println(comm);
	}
	
	
	
	
}
