package com.cdac;

public class MyThread extends Thread
{

	public void run()
	{
		for(int i = 0;i<50;i++)
		{
		
			try {
				Thread.sleep(500);
				System.out.println(i);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		
		}
	
	}
	
}
