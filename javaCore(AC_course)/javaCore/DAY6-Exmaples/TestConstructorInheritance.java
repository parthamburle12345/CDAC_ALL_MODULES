package com.cdac;

class A
{ 
	 int i;
	 
	A()
	{
		System.out.println("default of A");
	}
	
	A(int i)
	{
		this.i =i;
		System.out.println("parameter of A " +i);
	}
}


class B extends A
{
	int j;
	
	B()
	{ 
		System.out.println("default of B");
	}
	
	B(int i,int j)
	{  
		super(i);
		this.j = j;
		System.out.println("parameter of B " + j);
	}
}





public class TestConstructorInheritance 
{

	public static void main(String[] args) 
	{
		
		
		B b = new B(10,20);
	}
	
	
}
