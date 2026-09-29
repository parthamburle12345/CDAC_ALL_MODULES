package com.cdac;

public class PrintAlphabet extends Thread
{

	public void run()
	{
	for(char i='A';i<'J';i++)
	{
		try {
			Thread.sleep(500);
			System.out.println(Thread.currentThread().getName() +" "+i);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	
	}
	}
}
