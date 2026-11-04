package ExceptionHandling_BankWithdrawal;

import java.util.*;

class Account {
	int accNo;
	String name;
	double balance;

	public Account(int accNo, String name, double balance) {
		this.accNo = accNo;
		this.name = name;
		this.balance = balance;
	}

	void withdraw(double amount) {
		if (amount <= 0) {
			throw new IllegalArgumentException("withdrawal amount should be positive");
		}
		if (amount > balance) {
			throw new ArithmeticException("insufficient balance");
		}

		balance -= amount;

		System.out.println("withdrawal Successfull");

		System.out.println("remaining balance : " + balance);
	}

	void display() {
		System.out.println("Name is " + name);
		System.out.println("account number is " + accNo);
		System.out.println("balance is " + balance);
		System.out.println();
	}

}

public class ExceptionHandling_BankWithdrawal {

	public static void main(String[] args) {
		Account acc = new Account(1001, "Harsh", 10000);

		acc.display();

		System.out.println("Enter Withdrawal Amount");
		Scanner sc = new Scanner(System.in);
		double amo = sc.nextDouble();

		try {
			acc.withdraw(amo);
		} catch (IllegalArgumentException e) {
			System.out.println(e.getMessage());
		} catch (ArithmeticException e) {
			System.out.println(e.getMessage());
		} finally {
			System.out.println("Transction sucessfull");
		}

	}

}
