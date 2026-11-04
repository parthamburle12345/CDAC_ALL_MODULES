package examprep;

import java.util.Scanner;

public class StudentMain {
public static void main(String[] args) {
	StudentOperation st=new StudentOperation();
	Scanner sc=new Scanner(System.in);
	boolean enter=true;
	while(enter==true) {
		System.out.println("1.Add  Student:");
		System.out.println("2.Display Student Details :");
		System.out.println("3.Search Student :");
		System.out.println("4.Update Student");
		System.out.println("5.Delete student");
		System.out.println("6.Exit");
		System.out.println("Enter choice:");
		int choice=sc.nextInt();
		switch(choice) {
		case 1:{
			st.addBook();
			break;
		}
		case 2:{
			st.display();
			break;
		}
		case 3:{
			st.search();
			break;
		}
		case 4:{
			st.update();
			break;
		}
		case 5:{
			st.delete();
			break;
		}
		case 6:{
			enter=false;
			break;
		}
		}
	}
}
}
