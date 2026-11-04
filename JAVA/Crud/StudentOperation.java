package examprep;

import java.util.ArrayList;
import java.util.Scanner;

public class StudentOperation {

ArrayList<Student>al=new ArrayList<>();
Scanner sc=new Scanner(System.in);

public void addBook() {
	// TODO Auto-generated method stub
	System.out.println("Enter Student id");
	int id=sc.nextInt();
	sc.nextLine();
	System.out.println("Enter student name:");
	String name=sc.nextLine();
	System.out.println("Enter Marks :");
	float marks=sc.nextFloat();

	Student s=new Student(id,name,marks);
	al.add(s);
}



public void display() {
	// TODO Auto-generated method stub
	if(al.isEmpty()) {
		System.out.println("ArrayList Is Empty");
	}else {
		for(Student s:al) {
			s.display();
		}
	}
	
}
public void search() {
	// TODO Auto-generated method stub
	boolean found=false;
	if(al.isEmpty()) {
		System.out.println("ArrayList is empty ");
	}else {
		System.out.println("enter the Id of Student:");
		int id=sc.nextInt();
		for(Student s1:al) {
			if(id==s1.getId()) {
				found=true;
				s1.display();
			}
		}
	}
	if(!found) {
		System.out.println("No such id is found:");
	}
}



public void update() {
	// TODO Auto-generated method stub
	boolean found=false;
	if(al.isEmpty()) {
		System.out.println("ArrayList Is Empty!");
	}else {
		System.out.println("Student id you want to update:");
		int id=sc.nextInt();
		for(Student s2:al) {
			sc.nextLine();
			if(id==s2.getId()) {
				System.out.println("enter Student name:");
				String name=sc.nextLine();
				s2.setName(name);
				System.out.println("enter marks:");
				float marks=sc.nextFloat();
				s2.setMarks(marks);
				found=true;
				s2.display();
			}
		}
		
	}
	if(!found) {
		System.out.println("No such student found");
	}
	
}
public void delete() {
	// TODO Auto-generated method stub
	boolean found=false;
	if(al.isEmpty()) {
		System.out.println("ArrayList is Empty");
	}else {
		System.out.println("Enter id ");
		int id=sc.nextInt();
		for(int i=0;i<al.size();i++) {
			Student s3=al.get(i);
			if(id==s3.getId()) {
				al.remove(i);
				found=true;
				System.out.println("Student deleted from ArrayList");
			}
		}
		}
	if(!found) {
		System.out.println("No such id is found!");
	}
}


}




class Student{
	private int id;
	private String name;
	private float marks;
	public Student(int id, String name, float marks) {
		
		this.id = id;
		this.name = name;
		this.marks = marks;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public float getMarks() {
		return marks;
	}
	public void setMarks(float marks) {
		this.marks = marks;
	}
	void display() {
		System.out.println("Student Id:"+id);
		System.out.println("Student name:"+name);
		System.out.println("Student marks:"+marks);
	}
}