package com.cdac;

public class PassbyReference 
{
	private static void change(int[] num) 
	{
		num[0]=100;
		num[1]=200;
		
	}
	
	public static void main(String[] args) 
	{
	
		int[] num = {10,20,30,40,50};
		
		
				
		change(num);
		
		
		
		for(int ele:num)
		{
			System.out.println(ele);
		}
		
		
		
	}

	
	
	
}
