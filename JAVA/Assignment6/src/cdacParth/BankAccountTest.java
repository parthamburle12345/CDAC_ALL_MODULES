package cdacParth;

import java.util.Scanner;

public class BankAccountTest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter account number:");
        int accountNo = sc.nextInt();
        sc.nextLine(); 

        System.out.println("Enter account holder name:");
        String accountHolderName = sc.nextLine();

        System.out.println("Enter balance:");
        float balance = sc.nextFloat();

        System.out.println("Enter savings account interest rate:");
        float savingsRate = sc.nextFloat();

        System.out.println("Enter current account interest rate:");
        float currentRate = sc.nextFloat();

        SavingsAccount sa = new SavingsAccount(
            accountNo, accountHolderName, balance, savingsRate
        );

        CurrentAccount ca = new CurrentAccount(
            accountNo, accountHolderName, balance, currentRate
        );

        sa.calculateInterest();
        ca.calculateInterest();

        sc.close();
    }
}

