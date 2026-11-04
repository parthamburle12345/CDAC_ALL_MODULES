package com.cdac;

import java.util.Scanner;

//import java.util.Scanner;

public class BookMain {

	public static void main(String[] args) {
		
		BookManagement b = new BookManagement();
		Scanner sc = new Scanner(System.in);
		
		boolean b1 = true;
		
		while(b1 == true) {
			
			System.out.println("1.Add Book:");
			System.out.println("2.Display all Books:");
			System.out.println("3.Search books:");
			System.out.println("4.Update book:");
			System.out.println("5.Delete book:");
			System.out.println("6.Exit");
			System.out.println("Enter your Choice:");
			
			int choice = sc.nextInt();
			
			switch(choice) {
			case 1:{
				b.addBook();
				break;
				
			}
			case 2:{
				
			}
			case 3:{
				
			}
			case 4:{
				
			}
			case 5:{
				
			}
			case 6:{
				
			}
			
		}
		
	}

}
