package Interface_NotificationSystem;

interface Notification {
	void sendNotification(String message);

	void showStatus();
}

class EmailNotification implements Notification {
	String emailId;
	String subject;

	EmailNotification(String emailId, String subject) {
		this.emailId = emailId;
		this.subject = subject;
	}

	@Override
	public void sendNotification(String message) {
		System.out.println(message);
		System.out.println("Email: " + emailId);
		System.out.println("Subject: " + subject);
		System.out.println("Message sent through Email");
	}

	@Override
	public void showStatus() {
		System.out.println("Status: Email Delivered");
	}
}

class SMSNotification implements Notification {
	String mobileNumber;
	String provider;

	SMSNotification(String mobileNumber, String provider) {
		this.mobileNumber = mobileNumber;
		this.provider = provider;
	}

	@Override
	public void sendNotification(String message) {
		System.out.println(message);
		System.out.println("Mobile: " + mobileNumber);
		System.out.println("Provider: " + provider);
		System.out.println("Message sent through SMS");
	}

	@Override
	public void showStatus() {
		System.out.println("Status: SMS Delivered");
	}
}

class PushNotification implements Notification {
	String deviceId;
	String appName;

	PushNotification(String deviceId, String appName) {
		this.deviceId = deviceId;
		this.appName = appName;
	}

	@Override
	public void sendNotification(String message) {
		System.out.println(message);
		System.out.println("Device ID: " + deviceId);
		System.out.println("App: " + appName);
		System.out.println("Message sent through Push Notification");
	}

	@Override
	public void showStatus() {
		System.out.println("Status: Notification Delivered");
	}
}

public class NotificationSystem {
	public static void main(String[] args) {

		String message = "Your account has been updated.";

		Notification email = new EmailNotification("user@gmail.com", "Account Update");

		Notification sms = new SMSNotification("9876543210", "Airtel");

		Notification push = new PushNotification("DEV1023", "MyShoppingApp");

		System.out.println("Email Notification");
		email.sendNotification(message);
		email.showStatus();

		System.out.println();

		System.out.println("SMS Notification");
		sms.sendNotification(message);
		sms.showStatus();

		System.out.println();

		System.out.println("Push Notification");
		push.sendNotification(message);
		push.showStatus();
	}
}