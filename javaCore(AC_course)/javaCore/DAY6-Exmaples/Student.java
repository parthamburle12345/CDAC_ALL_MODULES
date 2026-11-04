package com.cdac;

public class Student extends Object
{

	int sid;
	String name;
	
	public Student(int sid, String name) 
	{
		
		this.sid = sid;
		this.name = name;
	}
	
	void display()
	{
		System.out.println(sid+name);
	}
	
	
}
