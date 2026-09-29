package com.cdac;

class A
{
   int i;
   
   void dispA()
   {
	   System.out.println("dispA  " +i);
   }
	
	
	
}

class B  extends A
{
	
	int j;
	   
	   void dispB()
	   {
		   System.out.println("dispB " +j);
	   }
	
	
}

class C extends A 
{
	
	int k;
	   
	   void dispC()
	   {
		   System.out.println("dispc " +k);
	   }
	
	
}




public class TestInheritance 
{

	public static void main(String[] args) 
	{
	
		
		B b = new B();
		b.i=20;
		b.j = 30;
		b.dispA();
		b.dispB();
		
		
		C c = new C();
		c.i=50;
		c.k=60;
		c.dispA();
		c.dispC();
		
      
		
		
		
	}
	
}
