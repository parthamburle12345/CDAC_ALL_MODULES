package com.cdac;

public class MultiThreadMain
{

	public static void main(String[] args) 
	{
		
		PrintNumber pn = new PrintNumber();
		pn.start();
		
		PrintAlphabet pa = new PrintAlphabet();
		pa.start();
	}
	
}
