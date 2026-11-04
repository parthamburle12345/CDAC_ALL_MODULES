package examprep;

import java.util.ArrayList;
import java.util.Scanner;

public class HospitalCRUD {
ArrayList<Hospital>al=new ArrayList<>();
Scanner sc=new Scanner(System.in);
public void AddPatient() {
	// TODO Auto-generated method stub
	System.out.println("Enter Patient Id");
	int id=sc.nextInt();
	sc.nextLine();
	System.out.println("Enter Patient Name");
	String name=sc.nextLine();
	System.out.println("Enter Patient Age");
	int age=sc.nextInt();
	Hospital h=new Hospital(id,name,age);
	al.add(h);
}
public void display() {
	// TODO Auto-generated method stub
	if(al.isEmpty()) {
		System.out.println("ArrayList is Empty");
	}else {
		for(Hospital h:al) {
			h.display();
		}
	}
}
public void SearchPatient() {
	// TODO Auto-generated method stub
	boolean found=false;
	if(al.isEmpty()) {
		System.out.println("ArrayList is Empty:");
	}else {
		System.out.println("Enter the Id ");
		int id=sc.nextInt();
		for(Hospital h:al) {
			if(id==h.getpId()) {
				found=true;
				h.display();
			}
		}
	}
	if(found==false) {
		System.out.println("No such Id is found:");
	}
}
public void updatePatient() {
	// TODO Auto-generated method stub
	boolean found=false;
	if(al.isEmpty()) {
		System.out.println("ArrayList is Empty");
	}else {
		System.out.println("Enter the id:");
		int id=sc.nextInt();
		for(Hospital h:al) {
			if(id==h.getpId()) {
				sc.nextLine();
				System.out.println("Enter Name");
				String name=sc.nextLine();
				h.setpName(name);
				System.out.println("Enter Age");
				int age=sc.nextInt();
				h.setpAge(age);
				found=true;
				h.display();
			}
		}
	}
	if(found==false) {
		System.out.println("No such id is found");
	}
}


}






class Hospital {
   int pId;
   String pName;
   int pAge;
	public Hospital(int pId, String pName, int pAge) {
	
		this.pId = pId;
		this.pName = pName;
		this.pAge = pAge;
	}
	public int getpId() {
		return pId;
	}
	public void setpId(int pId) {
		this.pId = pId;
	}
	public String getpName() {
		return pName;
	}
	public void setpName(String pName) {
		this.pName = pName;
	}
	public int getpAge() {
		return pAge;
	}
	public void setpAge(int pAge) {
		this.pAge = pAge;
	}
	
   void display() {
   	System.out.println("Patient ID:"+pId);
   	System.out.println("Patient Name:"+pName);
   	System.out.println("Patient Age:"+pAge);
   	
   }
}

