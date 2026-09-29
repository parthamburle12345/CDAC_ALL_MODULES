package cdac.com;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class StudentHashMapMain 
{
public static void main(String[] args) 
{

	Student s1 = new Student(1001,"nsnathan");
	Student s2 = new Student(1002,"nathan");
	Student s3 = new Student(1003,"raj");
	
	
	//add or create
	
	HashMap<Integer,Student> hm = new HashMap<>();
	
	hm.put(s1.sid, s1);
	hm.put(s2.sid, s2);
	hm.put(s3.sid, s3);
	
	//display
	
	for(Map.Entry<Integer, Student> m: hm.entrySet())
	{
		System.out.print(m.getKey()+ " ");
		
	   m.getValue().displayStudent();
		
		
	}
	
	//update
	
	System.out.println("enter the sid, name  to update ");
	Scanner s = new Scanner(System.in);
	int no  = s.nextInt();
	String na = s.next();
	
	Student obj=hm.get(no);
	obj.name = na;
	
	System.out.println("after update");
	
	
	for(Map.Entry<Integer, Student> m: hm.entrySet())
	{
		System.out.print(m.getKey()+ " ");
		
	   m.getValue().displayStudent();
		
		
	}
	 
	//delete
	System.out.println("enter sid to delete");
	 no  = s.nextInt();
	 hm.remove(no);
	 System.out.println("after delete");
	 
	 for(Map.Entry<Integer, Student> m: hm.entrySet())
		{
			System.out.print(m.getKey()+ " ");
			
		   m.getValue().displayStudent();
			
			
		}
	
}
}
