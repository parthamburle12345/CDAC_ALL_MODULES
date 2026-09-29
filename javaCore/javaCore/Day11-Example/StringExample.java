package com.cdac;

public class StringExample 
{
public static void main(String[] args) 
{

	
	String str = "1001 nsnathan 30";
	//	int[] num = {10,20,30,40};
		
		//String[] s = {"welcome","to","java"};
		
	
		String[] w = str.split(" ");
		Student s = new Student(Integer.parseInt(w[0]),w[1],Integer.parseInt(w[2]));
//		for(String ele: w)
//		{
//			System.out.println(ele);
//		}
		
		s.display();
}
}
