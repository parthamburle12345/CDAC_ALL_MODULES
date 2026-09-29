package com.cdac;

import java.util.ArrayList;

public class ArrayListExample
{

	
	public static void main(String[] args) 
	{
	
		ArrayList<Integer> al = new ArrayList<>();
		
		al.add(10);
		al.add(20);
		al.add(30);
		al.add(40);
		al.add(50);
		
		for( Integer  ele :al)
			
		{
			System.out.println(ele);
			
		}
		
		System.out.println("after remove");
		
		al.remove(2);
		for( Integer  ele :al)
			
		{
			System.out.println(ele);
			
		}
		
		al.set(3, 100);
		System.out.println("after modify");
		
	
	for( Integer  ele :al)
		
	{
		System.out.println(ele);
		
	}
	System.out.println("after insert");
	al.add(1, 25);
	for( Integer  ele :al)
		
	{
		System.out.println(ele);
		
	}
	
}}
