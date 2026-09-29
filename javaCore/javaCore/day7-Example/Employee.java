package com.cdac;

abstract public class Employee 
{
   int empno;
   String name;
   float sal;
public Employee(int empno, String name, float sal) {
	
	this.empno = empno;
	this.name = name;
	this.sal = sal;
}
 
abstract public void calculateBonous();

  
void displayEmployee()
{
	System.out.println(empno+name+sal);
}
   
   
	
	
}
