package cdac.com;

import java.util.HashMap;
import java.util.Map;

public class HashMapmain 
{

public static void main(String[] args) 
{

	HashMap<Integer,String> hm = new HashMap<>();
	
	//add or create
	
	hm.put(1, "pune AC");
	hm.put(2, "mumbai AC");
	hm.put(3, "Bangalore  AC");
	hm.put(4, "Bangalore bda");
	hm.put(5, "pune  AI");
	
	
	for(Map.Entry<Integer, String> m: hm.entrySet())
	{
		System.out.println(m.getKey()  + " "+ m.getValue());
		
	}
	
	
	hm.put(5, "Bangalore AI");
	
	System.out.println("--------------------------------------");
	for(Map.Entry<Integer, String> m: hm.entrySet())
	{
		System.out.println(m.getKey()  + " "+ m.getValue());
		
	}
	
	
	System.out.println("--------------------------------------");
	
	hm.remove(4);
	for(Map.Entry<Integer, String> m: hm.entrySet())
	{
		System.out.println(m.getKey()  + " "+ m.getValue());
		
	}
	
}	
	
}
