package com.cdac;

public class Test
{

	public static void main(String[] args) 
	{
	
//		int a = 5;
//		int b = 10;
//		boolean result = (a++ > 5) || (++b > 10);
//		System.out.println(a);
//		System.out.println(b);
//		System.out.println(result); 
		
//		A. 6 11 true
//		B. 6 10 true
//		C. 5 11 false
//		D. 5 10 false

		
		
		
		int x = 10;
		if (x > 5 && x++ > 10)
		 System.out.println("Yes");
		else
		 System.out.println("No");
		System.out.println(x);
		
		
//		A. Yes 11
//		B. No 11
//		C. No 10
//		D. Yes 10

		
		
		
	}
}
