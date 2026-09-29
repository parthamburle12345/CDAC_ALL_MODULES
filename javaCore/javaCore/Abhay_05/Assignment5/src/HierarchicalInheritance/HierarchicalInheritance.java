package HierarchicalInheritance;

class BankAccount {
	String accountNo;
	String customerName;
	double balance;

	static String bankName = "State Bank of India";

	BankAccount(String accountNo, String customerName, double balance) {
		this.accountNo = accountNo;
		this.customerName = customerName;
		this.balance = balance;
	}

	void displayDetails() {
		System.out.println("Bank Name     : " + bankName);
		System.out.println("Account No    : " + accountNo);
		System.out.println("Customer Name : " + customerName);
		System.out.println("Balance       : ₹" + balance);
	}
}

class SavingsAccount extends BankAccount {
	double interestRate;

	SavingsAccount(String accountNo, String customerName, double balance, double interestRate) {
		super(accountNo, customerName, balance);
		this.interestRate = interestRate;
	}

	double calculateInterest() {
		return (balance * interestRate) / 100;
	}

	void displaySavingsDetails() {
		displayDetails();
		System.out.println("Interest Rate : " + interestRate + "%");
		System.out.println("Interest      : ₹" + calculateInterest());
		System.out.println();
	}
}

class CurrentAccount extends BankAccount {
	double minimumBalance;

	CurrentAccount(String accountNo, String customerName, double balance, double minimumBalance) {
		super(accountNo, customerName, balance);
		this.minimumBalance = minimumBalance;
	}

	boolean checkMinimumBalance() {
		return balance >= minimumBalance;
	}

	void displayCurrentDetails() {
		displayDetails();
		System.out.println("Minimum Balance: ₹" + minimumBalance);

		if (checkMinimumBalance()) {
			System.out.println("Status        : Minimum balance maintained");
		} else {
			System.out.println("Status        : Minimum balance NOT maintained");
		}

		System.out.println();
	}
}

public class HierarchicalInheritance {
	public static void main(String[] args) {

		SavingsAccount savings1 = new SavingsAccount("SA101", "Rahul", 50000, 5.0);

		SavingsAccount savings2 = new SavingsAccount("SA102", "Priya", 75000, 4.5);

		CurrentAccount current1 = new CurrentAccount("CA101", "Arun", 100000, 50000);

		CurrentAccount current2 = new CurrentAccount("CA102", "Meena", 30000, 50000);

		System.out.println("SAVINGS ACCOUNT 1");
		savings1.displaySavingsDetails();

		System.out.println("SAVINGS ACCOUNT 2");
		savings2.displaySavingsDetails();

		System.out.println("CURRENT ACCOUNT 1");
		current1.displayCurrentDetails();

		System.out.println("CURRENT ACCOUNT 2");
		current2.displayCurrentDetails();
	}

}
