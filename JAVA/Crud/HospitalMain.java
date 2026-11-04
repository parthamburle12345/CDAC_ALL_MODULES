package examprep;

import java.util.Scanner;

public class HospitalMain {
public static void main(String[] args) {
	HospitalCRUD hc=new HospitalCRUD();
	Scanner sc=new Scanner(System.in);
	boolean enter=true;
	while(enter ==true) {
		System.out.println("1.Add Patient");
		System.out.println("2.Display Details");
		System.out.println("3.Search patient");
		System.out.println("4.update patient");
		System.out.println("5.Delete Patient");
		System.out.println("6.Exit");
		System.out.println("Enter choice:");
		int choice=sc.nextInt();
		switch(choice) {
		case 1:{
			hc.AddPatient();
			break;
		}
		case 2:{
			hc.display();
			break;
		}
		case 3:{
			hc.SearchPatient();
		}
		case 4:{
			hc.updatePatient();
			break;
		}
		case 5:{
			
		}
		case 6:{
			enter=false;
			break;
		}
		}
}
}
}
