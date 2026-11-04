package com.cdac;

import java.util.Scanner;

public class Student 
{
   int sid;
   String name;
   int mark;
   String subject;
   
//    void readStudent()
//   {
//	   
//	   Scanner s = new Scanner(System.in);
//	   sid = s.nextInt();
//	   name = s.next();
//	   mark = s.nextInt();
//	   subject = s.next();
//		   
//   }
   
   
 void readStudent(int id,String na,int m,String s)
{
	   
	   
	   sid = id;
	   name = na;
	   mark = m;
	   subject = s;
		   
}
   
   
   void displayStudent()
   {
	   System.out.println(sid);
	   System.out.println(name);
	   System.out.println(mark);
	   System.out.println(subject);
   }
   
   
   void findResult()
   {
	   if(mark>16)
		   System.out.println("pass");
	   else
		   System.out.println("fail");
	     
   }
   
   
}
