
package examprep;

import java.util.Scanner;

public class VehicleRentalMain {

    public static void main(String[] args) {

        VehicleRentalCRUD vc = new VehicleRentalCRUD();

        Scanner sc = new Scanner(System.in);

        boolean enter = true;

        while (enter == true) {

            System.out.println("\n1. Add Rental");
            System.out.println("2. Display All Rentals");
            System.out.println("3. Search Rental");
            System.out.println("4. Update Rental");
            System.out.println("5. Delete Rental");
            System.out.println("6. Exit");

            System.out.println("Enter Choice:");
            int choice = sc.nextInt();

            switch (choice) {

            case 1: {
                vc.AddRental();
                break;
            }

            case 2: {
                vc.display();
                break;
            }

            case 3: {
                sc.nextLine();
                vc.SearchRental();
                break;
            }

            case 4: {
                vc.updateRental();
                break;
            }

            case 5: {
                vc.deleteRental();
                break;
            }

            case 6: {
                enter = false;
                break;
            }

            default: {
                System.out.println("Invalid Choice");
                break;
            }

            }
        }

        sc.close();
    }
}
