package examprep;

import java.util.ArrayList;
import java.util.Scanner;

public class VehicleRentalCRUD {

    ArrayList<VehicleRental> al = new ArrayList<>();
    Scanner sc = new Scanner(System.in);

    public void AddRental() {

        System.out.println("Enter Rental Id:");
        int id = sc.nextInt();
        sc.nextLine();

        // // Check unique Rental ID
        // for (VehicleRental v : al) {
        //     if (id == v.getRentalId()) {
        //         System.out.println("Rental ID already exists");
        //         return;
        //     }
        // }

        System.out.println("Enter Vehicle Number:");
        String number = sc.nextLine();

        System.out.println("Enter Customer Name:");
        String name = sc.nextLine();

        System.out.println("Enter Vehicle Type (Car/Bike/SUV):");
        String type = sc.nextLine();

        System.out.println("Enter Rental Type (Daily/Weekly/Monthly/Long Term):");
        String rentalType = sc.nextLine();

        System.out.println("Enter Rental Cost:");
        double cost = sc.nextDouble();
        sc.nextLine();

        System.out.println("Enter Rental Status (Reserved/Active/Completed/Cancelled):");
        String status = sc.nextLine();

        VehicleRental v = new VehicleRental(
                id, number, name, type, rentalType, cost, status);

        al.add(v);

        System.out.println("Rental Added Successfully");
    }

    public void display() {

        if (al.isEmpty()) {
            System.out.println("ArrayList is Empty");
        } else {
            for (VehicleRental v : al) {
                v.display();
            }
        }
    }

    public void SearchRental() {

        boolean found = false;

        if (al.isEmpty()) {
            System.out.println("ArrayList is Empty");
        } else {
            System.out.println("Enter Vehicle Number:");
            String number = sc.nextLine();

            for (VehicleRental v : al) {
                if (number.equalsIgnoreCase(v.getVehicleNumber())) {
                    found = true;
                    v.display();
                    break;
                }
            }
        }

        if (found == false) {
            System.out.println("No such Vehicle Number is found");
        }
    }

    public void updateRental() {

        boolean found = false;

        if (al.isEmpty()) {
            System.out.println("ArrayList is Empty");
        } else {
            System.out.println("Enter Rental Id:");
            int id = sc.nextInt();
            sc.nextLine();

            for (VehicleRental v : al) {
                if (id == v.getRentalId()) {

                    System.out.println("Enter Rental Type:");
                    String rentalType = sc.nextLine();
                    v.setRentalType(rentalType);

                    System.out.println("Enter Rental Cost:");
                    double cost = sc.nextDouble();
                    sc.nextLine();
                    v.setRentalCost(cost);

                    System.out.println("Enter Rental Status:");
                    String status = sc.nextLine();
                    v.setRentalStatus(status);

                    found = true;

                    System.out.println("Rental Updated Successfully");
                    v.display();
                    break;
                }
            }
        }

        if (found == false) {
            System.out.println("No such Rental Id is found");
        }
    }

    public void deleteRental() {

        boolean found = false;

        if (al.isEmpty()) {
            System.out.println("ArrayList is Empty");
        } else {
            System.out.println("Enter Rental Id:");
            int id = sc.nextInt();

            for (VehicleRental v : al) {
                if (id == v.getRentalId()) {
                    al.remove(v);
                    found = true;
                    System.out.println("Rental Deleted Successfully");
                    break;
                }
            }
        }

        if (found == false) {
            System.out.println("Rental record not found");
        }
    }
}


// VehicleRental class
class VehicleRental {

    int rentalId;
    String vehicleNumber;
    String customerName;
    String vehicleType;
    String rentalType;
    double rentalCost;
    String rentalStatus;

    public VehicleRental(int rentalId, String vehicleNumber,
            String customerName, String vehicleType,
            String rentalType, double rentalCost, String rentalStatus) {

        this.rentalId = rentalId;
        this.vehicleNumber = vehicleNumber;
        this.customerName = customerName;
        this.vehicleType = vehicleType;
        this.rentalType = rentalType;
        this.rentalCost = rentalCost;
        this.rentalStatus = rentalStatus;
    }

    public int getRentalId() {
        return rentalId;
    }

    public String getVehicleNumber() {
        return vehicleNumber;
    }

    public String getRentalType() {
        return rentalType;
    }

    public void setRentalType(String rentalType) {
        this.rentalType = rentalType;
    }

    public double getRentalCost() {
        return rentalCost;
    }

    public void setRentalCost(double rentalCost) {
        this.rentalCost = rentalCost;
    }

    public String getRentalStatus() {
        return rentalStatus;
    }

    public void setRentalStatus(String rentalStatus) {
        this.rentalStatus = rentalStatus;
    }

    public void display() {
        System.out.println("Rental ID: " + rentalId);
        System.out.println("Vehicle Number: " + vehicleNumber);
        System.out.println("Customer Name: " + customerName);
        System.out.println("Vehicle Type: " + vehicleType);
        System.out.println("Rental Type: " + rentalType);
        System.out.println("Rental Cost: " + rentalCost);
        System.out.println("Rental Status: " + rentalStatus);
        System.out.println("------------------------------");
    }
}
