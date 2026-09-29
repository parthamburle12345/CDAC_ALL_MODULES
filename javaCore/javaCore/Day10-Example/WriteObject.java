package com.cdac;

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class WriteObject 
{

	
	
	
	public static void main(String[] args) throws IOException 
	{
	     
		FileReader fr = new FileReader("Employee.csv");
		BufferedReader br = new BufferedReader(fr);
		
		 
		
		
		
		FileOutputStream fos = new FileOutputStream("pgcpbda.txt");
		ObjectOutputStream oos = new ObjectOutputStream(fos);
		
		String str = br.readLine();
	      
	      //String[] sub = {"c++","java","python"};
		                
	      String[] e =  str.split(",");
		
		Employee obj = new Employee(Integer.parseInt(e[0]),e[1],Float.parseFloat(e[2]));
		
		
		oos.writeObject(obj);
		
		
		
		System.out.println("object write is over");
		
		fos.close();
		oos.close();
		
		
		
		
	} 
	
	
	
}
