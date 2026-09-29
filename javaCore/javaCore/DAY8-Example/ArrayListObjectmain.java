package com.cdac;

import java.util.ArrayList;
import java.util.Scanner;

public class ArrayListObjectmain
{

	public static void main(String[] args) 
	{
	
		ArrayList<Employee> al = new ArrayList<>();
		
		Employee e1 = new Employee(1001,"shan",40000);
		Employee e2 = new Employee(1002,"nsnathan",50000);
		Employee e3 = new Employee(1003,"raj",70000);
		
		//creation
		
		al.add(e1);
		al.add(e2);
		al.add(e3);
		
		
		//display
		
		EmployeeManagement.displayEmployeeObject(al);
		
		//update
		
		Scanner s = new Scanner(System.in);
		int eno  = s.nextInt();//1002
		float amount = s.nextFloat();
		
		
		for( Employee  obj :al)
			
		{
			if(obj.empno == eno)
			{
				obj.sal = obj.sal+amount;
			}
			
		}
		
		System.out.println("after update");
		
		EmployeeManagement.displayEmployeeObject(al);
		
		int pos =0;
		
		
		System.out.println("enter empno to delete");
		eno  = s.nextInt();//1002
		
		for( Employee  obj :al)
			
		{
			if(obj.empno == eno)
			{
				pos = al.indexOf(obj);
			}
			
		}
		
		al.remove(pos);
		System.out.println("after delete");
		
		EmployeeManagement.displayEmployeeObject(al);
		
	}
	
}
