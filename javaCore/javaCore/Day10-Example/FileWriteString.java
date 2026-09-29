package com.cdac;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class FileWriteString 
{

	public static void main(String[] args) throws IOException  
	{
	
		//create file
		
			FileWriter fw = new FileWriter("pgcpac.txt");
			
		//read from console
		System.out.println("enter the string");
			Scanner s = new Scanner(System.in);
			String str;;
			
		
			
			
		//read from console and write to the file
			
			while(!(str = s.nextLine()).equals("exit"))
			{
			
			fw.write(str+"\n");
			
			}
		//close the file
		System.out.println("file write is over");
			fw.close();
		
		//read from the file
		
		//write to the console
		
		
		//close the file
		
		
		
	}
	
	
	
}
