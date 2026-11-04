package practiceOver;

public class ElectricityBill {
 int consumerNo;
 String consumerName;
 int unitsConsumed;
  
 public ElectricityBill(int consumerNo, String consumerName, int unitsConsumed) {
	this.consumerNo = consumerNo;
	this.consumerName = consumerName;
	this.unitsConsumed = unitsConsumed;
}
 public void calculateBill(){
	System.out.println(unitsConsumed*8); 
	 
 }
 public void calculateBill(double rate) {
	 System.out.println(unitsConsumed*rate);
 }
 public void calculateBill(double rate,int units) {
	 System.out.println(units*rate);
 }
 
 public static void main(String[] args) {
	ElectricityBill e = new ElectricityBill(101,"Shreya",100);
	e.calculateBill();
	e.calculateBill(200);
	e.calculateBill(240,20);
}
 
}
