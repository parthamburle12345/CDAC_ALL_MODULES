package hospital;

import java.util.Scanner;

public class PatientMain {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);


        System.out.println("Enter InPatient ID:");
        int id1 = sc.nextInt();
        sc.nextLine();

        System.out.println("Enter InPatient Name:");
        String name1 = sc.nextLine();

        System.out.println("Enter Age:");
        int age1 = sc.nextInt();

        System.out.println("Enter Number of Days:");
        int days = sc.nextInt();

        System.out.println("Enter Room Charge per Day:");
        double roomCharge = sc.nextDouble();


        // OutPatient Details

        System.out.println("\nEnter OutPatient ID:");
        int id2 = sc.nextInt();
        sc.nextLine();

        System.out.println("Enter OutPatient Name:");
        String name2 = sc.nextLine();

        System.out.println("Enter Age:");
        int age2 = sc.nextInt();

        System.out.println("Enter Consultation Fee:");
        double consultationFee = sc.nextDouble();

        System.out.println("Enter Medicine Cost:");
        double medicineCost = sc.nextDouble();



        Patient p1 = new InPatient(
            id1, name1, age1, days, roomCharge
        );

        Patient p2 = new OutPatient(
            id2, name2, age2, consultationFee, medicineCost
        );



        System.out.println("\n--- InPatient Details ---");
        System.out.println("Patient ID: " + p1.patientId);
        System.out.println("Patient Name: " + p1.patientName);
        System.out.println("Age: " + p1.age);
        System.out.println("Treatment Cost: Rs. " + p1.calculateTreatmentCost());


        System.out.println("\n--- OutPatient Details ---");
        System.out.println("Patient ID: " + p2.patientId);
        System.out.println("Patient Name: " + p2.patientName);
        System.out.println("Age: " + p2.age);
        System.out.println("Treatment Cost: Rs. " + p2.calculateTreatmentCost());

        sc.close();
    }
}