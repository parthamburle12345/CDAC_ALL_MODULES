package com.cdac;

class Payment
{
	 String cname;
	 float amount;
	
	 public Payment(String cname, float amount)
	 {
			
			this.cname = cname;
			this.amount = amount;
		}
	 
	public void makePayment()
	{
		System.out.println("payment processed");
	}

	
}

class CreditCardPayment extends Payment
{
	String crdNo;
	
	public CreditCardPayment(String cname, float amount,String crdNo)
	{
		super(cname, amount);
	    this.crdNo = crdNo;	
	}



	
	
	
	
	public void makePayment()
	{
		System.out.println("payment " + amount + " processed using CreditCard" );
		System.out.println(cname);
		System.out.println(crdNo);
		
	}
	
}

class UpiPayment extends Payment
{
	   int upiId;
	   
	public UpiPayment(String cname, float amount,int upiId)
	{
		super(cname, amount);
	    this.upiId = upiId;	
	}
	
	
	public void makePayment()
	{
		System.out.println("payment " + amount + " processed using UPI" );
		System.out.println(cname);
		System.out.println(upiId);
		
	}
	
}


public class OverridingPayment 
{

	public static void main(String[] args)
	{
//		CreditCardPayment c = new CreditCardPayment("nsnathan",30000,"a001");
//		c.makePayment();
		
		UpiPayment u = new UpiPayment("raj",2000,200001);
		u.makePayment();
	}
	
}
