package com.cdac;

public class BankType 
{

	public Bank createObject(String cname)
	{
		
		if(cname.equals("Upi"))
		{
			Upi u = new Upi();
			
			return u;

		}else if(cname.equals("DebitCard"))
		{
			DebitCard d = new DebitCard();
			return d;
            
		}else if(cname.equals("Netbanking"))
		{
			Netbanking n = new Netbanking();
            return n;
		}else
		{
			System.out.println("invalid class name");
			return null;
		}
		
	}
	
	
}
