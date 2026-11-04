package assignment2;

import java.util.*;

public class TemperatureConversion {

	static double convertTemperature(double celsius) {
		return (celsius * 9 / 5) + 32;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		System.out.print("Enter temperature in Celsius: ");
		double celsius = sc.nextDouble();

		double fahrenheit = convertTemperature(celsius);

		System.out.println("Temperature in Fahrenheit = " + fahrenheit + "°F");

		if (fahrenheit > 100) {
			System.out.println("The temperature is above 100°F.");
		} else {
			System.out.println("The temperature is 100°F or below.");
		}
	}
}
