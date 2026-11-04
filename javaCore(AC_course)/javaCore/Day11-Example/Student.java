package com.cdac;
import java.io.Serializable;
import java.util.Scanner;
public class Student  implements Serializable
{
int id;
String name;
int marks;

public Student(int id, String name, int marks) {
	this.id = id;
	this.name = name;
	this.marks = marks;
	
	}	
	void display() {
		System.out.print(id);
		System.out.print(name);
		System.out.print(marks);
		System.out.println();
	}
}
