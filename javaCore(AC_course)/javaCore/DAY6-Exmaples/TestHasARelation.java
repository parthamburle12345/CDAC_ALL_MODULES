package com.cdac;

public class TestHasARelation 
{

	public static void main(String[] args) 
	{
	
		Address add = new Address("Bangalre","karnataka",560043);
		Emp e = new Emp(1001,"shan",add);
		e.displayEmplyee();
		
	} 
	
}
