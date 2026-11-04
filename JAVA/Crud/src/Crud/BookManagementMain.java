package Crud;

import java.util.Scanner;

public class BookManagementMain {

	public static void main(String[] args) {
		BookManagement m = new BookManagement();
		
		Scanner sc = new Scanner(System.in);
		boolean enter = true;
		
		while(enter == true) {
			System.out.println("1. add book");
			System.out.println("2. display book");
			System.out.println("3. search book");
			System.out.println("4. update book");
			System.out.println("5. delete book");
			System.out.println("6. Exit");
			
			int choice = sc.nextInt();
				switch(choice) {
				case 1 : {
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
					enter = false;
					break;
				}
				
				}
			}
		sc.close();
		}
		
	}

