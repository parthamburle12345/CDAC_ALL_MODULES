package com.cdac;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.*;

public class StudentFileRead {

	public static void main(String[] args) throws IOException, ClassNotFoundException {
		FileInputStream fis = new FileInputStream("student.txt");
		ObjectInputStream ois = new ObjectInputStream(fis);
		Scanner sc = new Scanner(System.in);
//		Student s1 = (Student) ois.readObject();
//		Student s2 = (Student) ois.readObject();
//		Student s3 = (Student) ois.readObject();
//		
//		
//		s1.display();
//		s2.display();
//		s3.display();
		Student s;
		ArrayList<Student> al=new ArrayList<Student>();
		try {
			while((s =(Student) ois.readObject())!=null)
			{
				al.add(s);
			}
			
		} catch (EOFException e) {

			// TODO: handle exception
		}
	
		for(Student s1:al) {
			//System.out.println(s1);
			s1.display();
		}
		int id = sc.nextInt();
		for(Student s1:al) {
			if(s1.id==id)
			{
				s1.marks=100;
			}
		}
			for(Student s1:al) {
				//System.out.println(s1);
				s1.display();
			}
		}
	}


