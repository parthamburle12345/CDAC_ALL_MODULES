package com.cdac;

import java.util.Scanner;

interface Bank
{
	
 public void makePayment(int amount);
	
}

class Netbanking implements Bank
{
	
	public void makePayment(int amount)
	{
		System.out.println("payment " + amount + "processed using netbanking");
	}
	
}


class DebitCard implements Bank
{

	@Override
	public void makePayment(int amount) 
	{
		System.out.println("payment " + amount + " processed using Debitcard");
		
	}
	
		
}


class Upi implements Bank
{

	@Override
	public void makePayment(int amount) 
	{
		System.out.println("payment " + amount + " processed using upi");
		
	}
	
		
}


public class InterfaceExample
{

	public static void main(String[] args) 
	{
	
		
	      Bank b;
	      BankType bt = new BankType();
	      
		Scanner s = new Scanner(System.in);
		
		System.out.println("enter the mode of payment");
		String cname = s.next(); 
			
		 b=bt.createObject(cname);
		b.makePayment(1000);
						
				
		}
}
