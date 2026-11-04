package cdacParth;

class BankAccount {
    int accountNo;
    String accountHolderName; // Fixed spelling typo
    float balance;
    
    public BankAccount(int accountNo, String accountHolderName, float balance) {
        this.accountNo = accountNo;
        this.accountHolderName = accountHolderName;
        this.balance = balance;
    }
    
    void calculateInterest() {
        System.out.println("General bank account interest calculation");
    }
}

class SavingsAccount extends BankAccount {
    float interestRate;

    public SavingsAccount(int accountNo, String accountHolderName, float balance, float interestRate) {
        super(accountNo, accountHolderName, balance);
        this.interestRate = interestRate;
    }

    @Override
    void calculateInterest() {
        // Fixed: Added '*' multiplication operator
        float interest = (balance * interestRate) / 100;

        System.out.println("\n--- Savings Account ---");
        System.out.println("Account Number: " + accountNo);
        System.out.println("Account Holder: " + accountHolderName); // Uses inherited field correctly
        System.out.println("Balance: Rs. " + balance);
        System.out.println("Interest: Rs. " + interest);    
    }
}

class CurrentAccount extends BankAccount {
    float interestRate;

    public CurrentAccount(int accountNo, String accountHolderName, float balance, float interestRate) {
        super(accountNo, accountHolderName, balance);
        this.interestRate = interestRate;
    }

    @Override
    void calculateInterest() {
        // Fixed: Added '*' multiplication operator
        float interest = (balance * interestRate) / 100;

        System.out.println("\n--- Current Account ---");
        System.out.println("Account Number: " + accountNo);
        System.out.println("Account Holder: " + accountHolderName); // Uses inherited field correctly
        System.out.println("Balance: Rs. " + balance);
        System.out.println("Interest: Rs. " + interest);
    }
}

