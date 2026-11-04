package com.cdac;

public class TestThreading
{

	public static void main(String[] args) 
	{
	
		MyThread t1 = new MyThread();
		t1.start();
		System.out.println("end of main");
		
	}
}
