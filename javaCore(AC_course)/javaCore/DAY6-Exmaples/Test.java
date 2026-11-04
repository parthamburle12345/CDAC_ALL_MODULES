package com.cdac;

public class Test 
{

	public static void main(String[] args) 
	{
		Engine e = new Engine(1000001,125);
		Car c = new Car(1001,"Toyota",300000,e);
		
		c.displayCar();
		
		
		
	}
}
