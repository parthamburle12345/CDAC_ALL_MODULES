package com.cdac;

public class ExceptionExample 
{

	public static void main(String[] args) 
	{
	
//		int[] num = {10,20,30};
//		try
//		{
//		System.out.println(num[4]);
//		}catch(ArrayIndexOutOfBoundsException e)
//		{
//			//System.out.println(e.getMessage());
//			System.out.println("size should be 3 or less than 3");
//			
//		}
		
		int a = 0;
		int b = 20;
		
		
		try
		{
		int c = b/a;
		System.out.println(c);
		}catch(ArithmeticException e)
		{
			System.out.println(e.getMessage());
		}
		finally
		{
			
			System.out.println("resource closed");
		}
		System.out.println("last line in main");
		
		
		
	}
}
