package com.cdac;

public class Address 
{

	String city;
	String state;
	int pin;
	
	public Address(String city, String state, int pin) 
	{
		
		this.city = city;
		this.state = state;
		this.pin = pin;
	}
	
	
	void displayAddress()
	{
		System.out.println(city+state+pin);
	}
	
}
