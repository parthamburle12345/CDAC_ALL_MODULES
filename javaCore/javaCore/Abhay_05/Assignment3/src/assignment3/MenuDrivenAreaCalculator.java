package assignment3;

import java.util.Scanner;

public class MenuDrivenAreaCalculator {

	public static double areaOfCircle(float r) {
		return 3.14 * r * r;
	}

	public static double areaOfRectangle(float len, float bre) {
		return len * bre;
	}

	public static double areaOfTriangle(float base, float height) {
		return 0.5 * base * height;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println(
				"enter choice \n 1->Area of circle \n 2->Area of rectangle \n 3->Area of Triangle \n 4->Exit  ");
		int choice = sc.nextInt();
		switch (choice) {
		case 1: {
			float r = sc.nextFloat();
			double area = areaOfCircle(r);
			System.out.println("Area of circle :" + area);
			break;
		}
		case 2: {
			float len = sc.nextFloat();
			float bre = sc.nextFloat();
			double area = areaOfRectangle(len, bre);
			System.out.println("Area of rectangle :" + area);
			break;
		}
		case 3: {
			float base = sc.nextFloat();
			float height = sc.nextFloat();
			double area = areaOfTriangle(base, height);
			System.out.println("Area of Triangle :" + area);
			break;
		}
		case 4: {
			System.out.println("exit from operation.");
			break;
		}
		}

	}

}
