package com.cdac;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class FileReadString 
{

	
	public static void main(String[] args) throws IOException 
	{
	
		FileReader fr = new FileReader("pgcpac.txt");
		BufferedReader br = new BufferedReader(fr);
		br.readLine();
		
		
		//read from file
//		int ch;
//		while(( ch= fr.read())!=-1)
//{
//	
//			System.out.print((char)ch);
//	
//}
            String str; 
         
          //read from file and write to the console   
            
		while((str =br.readLine())!=null)
		{
			System.out.println(str);
		}
		
		
		
		
		
		
	//	char ch =(char) fr.read();
		
		
		//write to the console
		
		
		
		
		
	}
	
}
