package BankAccountUsingConstructor;

public class BankAccount {
	int accountNo;
	String customerName;
	double balance;

	BankAccount(int no, String name, double bal) {
		accountNo = no;
		customerName = name;
		balance = bal;
	}

	void display() {
		System.out.println("Account No : " + accountNo);
		System.out.println("Name       : " + customerName);
		System.out.println("Balance    : " + balance);
	}

	void checkBalance() {
		System.out.println("Current Balance : " + balance);
	}

	void calculateInterest() {

		double interest;

		if (balance >= 100000) {
			interest = balance * 0.07;
		} else if (balance >= 50000) {
			interest = balance * 0.06;
		} else {
			interest = balance * 0.05;
		}

		System.out.println("Interest   : " + interest);
		System.out.println();
	}
}
