package com.cdac;

import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

public class ReadEmployeeObject 
{

	public static void main(String[] args) throws IOException, ClassNotFoundException 
	{
		
	
		FileInputStream fis = new FileInputStream("pgcpbda.txt");
		ObjectInputStream ois = new ObjectInputStream(fis);
		
		Employee e;
		
		
//		Employee e1=(Employee) ois.readObject();
//		
//		e1.displayEmployee();
//		
//		Employee e2=(Employee) ois.readObject();
//		
//		e2.displayEmployee();
//		
//		
//		Employee e3=(Employee) ois.readObject();
//		
//		e3.displayEmployee();
		ArrayList<Employee> al = new ArrayList<>();
		
		
		try
		{
		while(( e = (Employee) ois.readObject())!=null)
		{
			//e.displayEmployee();
			
			al.add(e);
			
		}
		}catch(EOFException e1)
		{
			
		}
		
		
		
		for(Employee obj:al)
		{
			obj.displayEmployee();
		}
		
		
	}
	
}
