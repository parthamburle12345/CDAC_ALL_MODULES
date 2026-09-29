package com.cdac;

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class StudentFileWrite {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		
//		
//		Student s1=new Student(101, "Piyush",30 );
//		Student s2=new Student(102, "Ram",50 );
//		Student s3=new Student(103, "Anant",80 );
		
		
		FileReader fr = new FileReader("Student.csv");
		BufferedReader br = new BufferedReader(fr);
		
		FileOutputStream fos=new FileOutputStream("student.txt"); 
		ObjectOutputStream oos=new ObjectOutputStream(fos); 
		
		String str; 
		
	//	int[] num = {10,20,30,40};
		
		//String[] s = {"welcome","to","java"};
		
		while((str = br.readLine())!=null)
		{
			String[] w = str.split(",");
			Student s = new Student(Integer.parseInt(w[0]),w[1],Integer.parseInt(w[2]));
			oos.writeObject(s);
		}
		
		
		
		
		
		
		fos.close();
		oos.close();
		br.close();
		fr.close();
		
		
		

		System.out.println("object write is over");
		
	}

}
