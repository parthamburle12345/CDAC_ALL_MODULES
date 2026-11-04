package com.cdac;
class Printing
{
	public void printNumbers()
	{
		
			for(int i=0;i<10;i++)
			{
				try {
					Thread.sleep(500);
					System.out.println(Thread.currentThread().getName()+ " "+i);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
					System.out.println("Which course?");
				}
				
			
			}
			
		}
		
		
		
	
	
	
	public void printAlphabet()
	{
		
		for(char i='A';i<'J';i++)
		{
			try {
				Thread.sleep(500);
				System.out.println(Thread.currentThread().getName()+ " "+ i);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		
		}
		
		
		
	}
	
	
	
}


class ThreadPrinting extends Thread
{
	
	Printing p;
	int ch;
	
	public ThreadPrinting(Printing p,int ch) 
	{
		
		this.p = p;
		this.ch = ch;
	}




	public void run()
	{
		if(ch ==1)
		{
		p.printAlphabet();
		}
		else if(ch ==2)
		{
			p.printNumbers();
		}else
		{
			System.out.println("no choice");
		}
	}
	
	
	
}




public class TestMultiThreadMain
{

	public static void main(String[] args) 
	{
	
		
		
		
		Printing p= new Printing();
		
		ThreadPrinting tp1 = new ThreadPrinting(p,1);
		tp1.start();
		
		ThreadPrinting tp2 = new ThreadPrinting(p,2);
		tp2.start();
		
		
		
	}
	
	
}
