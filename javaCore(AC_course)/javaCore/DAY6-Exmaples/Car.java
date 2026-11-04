package com.cdac;

public class Car
{

	int carNo;
	String brand;
	float price;
	Engine e;
	
	public Car(int carNo, String brand, float price,Engine e) {
	
		this.carNo = carNo;
		this.brand = brand;
		this.price = price;
		this.e = e;
	}
	
	void displayCar()
	{
		System.out.println(carNo+brand+price+e.cc+e.engineNo);
		//e.displayEngine();
	}
	
	
}
