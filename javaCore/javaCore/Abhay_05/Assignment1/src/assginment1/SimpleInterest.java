package assginment1;

public class SimpleInterest {
	public static void main(String[] args) {
		float P = 10000.00f;
		float R = 2.5f;
		int T = 2;

		double simpleInterest = (P * R * T) / 100;
		double amount = P + simpleInterest;

		System.out.println("Simple Interest is " + " " + simpleInterest);
		System.out.println("amount is " + " " + amount);

	}

}
