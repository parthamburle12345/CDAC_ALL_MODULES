package com.cdac;

public class TestStudent 
{

	public static void main(String[] args) 
	{
	
		Student s1= new Student(1001,"shan");
		Student s2= new Student(1002,"RAJ");
		Student s3= new Student(1003,"SIJU");
		
		s1.display();
		s2.display();
		s3.display();
		
		Student.cname="PGCP-BDA";
		
		//Student.changecname();
		
		Student s4= new Student(1004,"kumar");
		Student s5= new Student(1005,"saravan");
		s4.display();
		s5.display();
		
	}
	
}
