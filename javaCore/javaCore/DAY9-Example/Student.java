package cdac.com;

public class Student
{

	int sid;
	String name;
	
	public Student(int sid, String name)
	{
		
		this.sid = sid;
		this.name = name;
	}
	
	void displayStudent()
	{
		System.out.println(sid+name);
		
	}
	
}
