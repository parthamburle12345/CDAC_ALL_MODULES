package AbstractClass_BankingWithdrawalSystem;

abstract class BankAccount {
	String accountNumber;
	String customerName;
	double balance;

	BankAccount(String accountNumber, String customerName, double balance) {
		this.accountNumber = accountNumber;
		this.customerName = customerName;
		this.balance = balance;
	}

	void deposit(double amount) {
		balance = balance + amount;
		System.out.println("Deposited Amount: ₹" + amount);
	}

	void displayAccountDetails() {
		System.out.println("Account Number: " + accountNumber);
		System.out.println("Customer Name: " + customerName);
		System.out.println("Balance: ₹" + balance);
	}

	abstract void calculateWithdrawalLimit();
}

class SavingsAccount extends BankAccount {
	double withdrawalPercentage;

	SavingsAccount(String accountNumber, String customerName, double balance, double withdrawalPercentage) {

		super(accountNumber, customerName, balance);
		this.withdrawalPercentage = withdrawalPercentage;
	}

	@Override
	void calculateWithdrawalLimit() {
		double limit = balance * withdrawalPercentage / 100;

		System.out.println("Withdrawal Limit: ₹" + limit);
	}
}

class CurrentAccount extends BankAccount {
	double overdraftFacility;

	CurrentAccount(String accountNumber, String customerName, double balance, double overdraftFacility) {

		super(accountNumber, customerName, balance);
		this.overdraftFacility = overdraftFacility;
	}

	@Override
	void calculateWithdrawalLimit() {
		double limit = balance + overdraftFacility;

		System.out.println("Withdrawal Limit: ₹" + limit);
	}
}

public class BankingWithdrawalSystem {
	public static void main(String[] args) {

		SavingsAccount savings = new SavingsAccount("SA1001", "Arun", 50000, 40);

		CurrentAccount current = new CurrentAccount("CA2001", "Kumar", 80000, 30000);

		System.out.println(" SAVINGS ACCOUNT ");

		savings.deposit(10000);
		savings.calculateWithdrawalLimit();
		savings.displayAccountDetails();

		System.out.println("\n CURRENT ACCOUNT ");

		current.deposit(20000);
		current.calculateWithdrawalLimit();
		current.displayAccountDetails();
	}
}