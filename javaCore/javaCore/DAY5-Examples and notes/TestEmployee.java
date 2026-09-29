package com.cdac;

import java.util.Scanner;

public class TestEmployee
{

	public static void main(String[] args) 
	{
	
		
		Employee[] e = new Employee[3];
			
		Scanner s = new Scanner(System.in);
				
		for(int i =0;i<3;i++)
		{
			e[i] = new Employee(s.nextInt(),s.next(),s.nextFloat());
			
		}
		
		for(int i =0;i<3;i++)
		{
			
			e[i].display();
		}
	}
	
}
