package cdac.com;

import java.util.ArrayList;
import java.util.Scanner;

public class StudentManagement
{

	public ArrayList<Student> createStudents()
	{
		ArrayList<Student> al = new ArrayList<>();
		 
		//read one line from excel
		 
		Student s1 = new Student(1001,"nsnathan");
		
		
		Student s2 = new Student(1002,"nathan");
		Student s3 = new Student(1003,"raj");
		
		al.add(s1);
		al.add(s2);
		al.add(s3);
		
		return al;
		
	}

	public void displayStudents(ArrayList<Student> al) 
	{
		for(Student obj :al)
		{
			obj.displayStudent();
		}
		
	}

	public void updateStudents(ArrayList<Student> al)
	{
		System.out.println("enter the sid,name  to update ");
		Scanner s = new Scanner(System.in);
		int no  = s.nextInt();
		
		String na = s.next();
		
		for(Student obj :al)
		{
			if(obj.sid == no)
			{
				obj.name = na;
			}
		}
		
		
	}

	public void DeleteStudents(ArrayList<Student> al) 
	{
		int pos = 0;
		Scanner s = new Scanner(System.in);
		int no  = s.nextInt();
		
		for(Student obj :al)
		{
			if(obj.sid == no)
			{
				pos = al.indexOf(obj);
			}
		}
		
		al.remove(pos);
		System.out.println("student removed");
	}
	
	
}
