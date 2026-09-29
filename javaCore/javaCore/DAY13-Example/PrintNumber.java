package com.cdac;

public class PrintNumber extends Thread
{

	public void run()
	{
		
		for(int i=0;i<10;i++)
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
