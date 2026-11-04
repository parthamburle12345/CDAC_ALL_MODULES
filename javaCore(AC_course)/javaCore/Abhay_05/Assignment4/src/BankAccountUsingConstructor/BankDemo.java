package BankAccountUsingConstructor;

public class BankDemo {
	public static void main(String[] args) {

		BankAccount b1 = new BankAccount(1001, "Ravi", 75000);
		BankAccount b2 = new BankAccount(1002, "Rahul", 120000);
		BankAccount b3 = new BankAccount(1003, "Amit", 40000);

		b1.display();
		b1.checkBalance();
		b1.calculateInterest();

		b2.display();
		b2.checkBalance();
		b2.calculateInterest();

		b3.display();
		b3.checkBalance();
		b3.calculateInterest();
	}
}
