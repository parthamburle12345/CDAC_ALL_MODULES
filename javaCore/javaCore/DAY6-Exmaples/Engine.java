package com.cdac;

public class Engine 
{

	int engineNo;
	int cc;
	
	
	
	public Engine(int engineNo, int cc) 
	{
		
		this.engineNo = engineNo;
		this.cc = cc;
	}



	void displayEngine()
	{
		System.out.println(engineNo+cc);
	}
	
	
	
}
