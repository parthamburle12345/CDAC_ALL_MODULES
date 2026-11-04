package interface0;

public class PaymentMain {

    public static void main(String[] args) {

        UPIPayment upi = new UPIPayment(101, "parth@upi");

        upi.processPayment(1500);
        upi.displayPaymentDetails();

        System.out.println("----------------------");

        CardPayment card = new CardPayment(102, "1234567890123456");

        card.processPayment(2500);
        card.displayPaymentDetails();

    }
}