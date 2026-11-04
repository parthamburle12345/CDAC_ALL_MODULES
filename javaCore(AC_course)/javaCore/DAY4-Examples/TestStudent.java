package com.cdac;

public class TestStudent 
{
	public static void main(String[] args) 
	   {
		
		   Student s1 = new Student();
		   
		//  s1.readStudent();
		    s1.readStudent(1001,"shan",30,"java");
		   
		   Student s2 = new Student();
		   
		   s2.readStudent(1002,"vasu",50,"python");
		   
		   Student s3 = new Student();
		   
		   s3.readStudent(1003,"kumar",60,"java");
		   		
		   
		   System.out.println("first object-student");
		   s1.displayStudent();
		   s1.findResult();
		   
		   System.out.println("second object-student");
		   s2.displayStudent();
		   s2.findResult();
		   
		   System.out.println("third object-student");
		   s3.displayStudent();
		   s3.findResult();
		   
	   }
}
