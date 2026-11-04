package examprep;

import java.util.Scanner;

public class BookMain {
public static void main(String[] args) {
	BookManagement m=new BookManagement();
	
	Scanner s = new Scanner(System.in);
	boolean enter = true;
	while(enter == true) {
	     System.out.println("1. Add Book");
	     System.out.println("2. Display All Book");
	     System.out.println("3. Search Book By Id");
	     System.out.println("4. Update Book");
	     System.out.println("5. Delete Book");
	     System.out.println("6. Exit ");
	     System.out.println("Choose a value");
	     int choice=s.nextInt();
	     switch(choice){
	     case 1:{
	    	 m.addBook();
	    	 break;
	     }
	     case 2:{
	    	 m.displayBook();
	    	 break;
	     }
	     case 3:{
	    	 m.searchBook();
	    	 break;
	     }
	     case 4:{
	    	 m.updateBook();
	    	 break;
	     }
	     case 5:{
	    	 m.deleteBook();
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
