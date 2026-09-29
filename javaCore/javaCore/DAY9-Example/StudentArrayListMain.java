package cdac.com;

import java.util.ArrayList;

public class StudentArrayListMain 
{
public static void main(String[] args)
{

	StudentManagement sm = new StudentManagement();
	
	
	
	
	ArrayList<Student> al = sm.createStudents();
	
							sm.displayStudents(al);
	
							sm.updateStudents(al);
	
							sm.displayStudents(al);

							sm.DeleteStudents(al);
							sm.displayStudents(al);
}
}