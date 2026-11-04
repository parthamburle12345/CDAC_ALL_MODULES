package cdacParth;

import java.util.Scanner;

public class ElectricityBill {

    int consumerNo;
    String consumerName;
    float unitsConsumed;

    // Constructor
    public ElectricityBill(int consumerNo, String consumerName,
                           float unitsConsumed) {
        this.consumerNo = consumerNo;
        this.consumerName = consumerName;
        this.unitsConsumed = unitsConsumed;
    }

    double calculateBill() {
        return unitsConsumed * 8.0;
    }

    double calculateBill(double rate) {
        return unitsConsumed * rate;
    }

    double calculateBill(double rate, int units) {
        return rate * units;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Enter consumer number:");
        int consumerNo = sc.nextInt();
        sc.nextLine();

        System.out.println("Enter consumer name:");
        String consumerName = sc.nextLine();

        System.out.println("Enter units consumed:");
        float unitsConsumed = sc.nextFloat();

        ElectricityBill eb = new ElectricityBill(
            consumerNo, consumerName, unitsConsumed
        );

        System.out.println("Consumer Number: " + eb.consumerNo);
        System.out.println("Consumer Name: " + eb.consumerName);
        System.out.println("Units Consumed: " + eb.unitsConsumed);

        System.out.println("Bill at default rate: Rs. "+ eb.calculateBill());

        System.out.println("Bill at Rs. 10 per unit: Rs. "+ eb.calculateBill(10.0));

        System.out.println("Bill at Rs. 12 per unit for 100 units: Rs. "+ eb.calculateBill(12.0, 100));

        sc.close();
    }
}
