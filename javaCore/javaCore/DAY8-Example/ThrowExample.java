package com.cdac;

public class ThrowExample
{

	public static void checkBalance(int amount) throws MinumumBalance  
	{
		
			if(amount<500)
			{
				throw new MinumumBalance("Minimum balance should be 500"); 
			}else
			{
				System.out.println("withdraw completed");
			}
		
	}
	
	
	
	public static void main(String[] args) 
	{
		
		
			try {
				checkBalance(200);
			} catch (MinumumBalance e) {
				System.out.println(e.getMessage());
			}
		
		 System.out.println("end of main");
		
	}

	
	
}
