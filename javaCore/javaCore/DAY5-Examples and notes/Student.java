package com.cdac;

public class Student
{

	int sid;
	String name;
	static String cname="PGCP-AC";
	public Student(int sid, String name) 
	{
		this.sid = sid;
		this.name = name;
		
	}
	
	static void changecname()
	{
		
		cname="PGCP-BDA";
	}
	void display()
	{
		System.out.println(sid+ " "+name+ " "+ cname);
	}
	
	
}
