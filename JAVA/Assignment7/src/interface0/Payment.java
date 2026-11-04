package interface0;

// Interface
public interface Payment {

    void processPayment(double amount);

    void displayPaymentDetails();
}


// UPI Payment Class
class UPIPayment implements Payment {

    int transactionId;
    String upiId;

    public UPIPayment(int transactionId, String upiId) {
        this.transactionId = transactionId;
        this.upiId = upiId;
    }

    @Override
    public void processPayment(double amount) {
    	// logic we have to write 
        System.out.println("UPI Payment Amount: " + amount);
        System.out.println("Transaction ID: " + transactionId);
    }

    @Override
    public void displayPaymentDetails() {
        System.out.println("Transaction ID: " + transactionId);
        System.out.println("UPI ID: " + upiId);
    }
}


// Card Payment Class
class CardPayment implements Payment {

    int transactionId;
    String cardNumber;

    public CardPayment(int transactionId, String cardNumber) {
        this.transactionId = transactionId;
        this.cardNumber = cardNumber;
    }

    @Override
    public void processPayment(double amount) {
        System.out.println("Card Payment Amount: " + amount);
        System.out.println("Transaction ID: " + transactionId);
    }

    @Override
    public void displayPaymentDetails() {
        System.out.println("Transaction ID: " + transactionId);
        System.out.println("Card Number: " + cardNumber);
    }
}