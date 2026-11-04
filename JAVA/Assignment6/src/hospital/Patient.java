package hospital;

public class Patient {

    int patientId;
    String patientName;
    int age;

    public Patient(int patientId, String patientName, int age) {
        this.patientId = patientId;
        this.patientName = patientName;
        this.age = age;
    }

    double calculateTreatmentCost() {
        return 500.0;
    }
}


class InPatient extends Patient {

    int numberOfDays;
    double roomCharge;

    public InPatient(int patientId, String patientName, int age,
                     int numberOfDays, double roomCharge) {

        super(patientId, patientName, age);

        this.numberOfDays = numberOfDays;
        this.roomCharge = roomCharge;
    }

    @Override
    double calculateTreatmentCost() {

        double totalCost = numberOfDays * roomCharge;

        return totalCost;
    }
}


class OutPatient extends Patient {

    double consultationFee;
    double medicineCost;

    public OutPatient(int patientId, String patientName, int age,
                      double consultationFee, double medicineCost) {

        super(patientId, patientName, age);

        this.consultationFee = consultationFee;
        this.medicineCost = medicineCost;
    }

    @Override
    double calculateTreatmentCost() {

        double totalCost = consultationFee + medicineCost;

        return totalCost;
    }
}