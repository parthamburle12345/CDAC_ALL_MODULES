package StackBrowserHistory;

import java.util.*;

public class StackBrowserHistory {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Stack<String> st = new Stack<>();

		while (true) {
			System.out.println();
			System.out.println("Enter choice \n1. Visit New Page\r\n" + "2. Go Back\r\n" + "3. View Current Page\r\n"
					+ "4. Display History\r\n" + "5. Exit ");
			System.out.println();
			System.out.println("enter choice: ");
			int a = sc.nextInt();

			switch (a) {
			case 1:
				System.out.println("enter url: ");
				String url = sc.next();
				st.push(url);
				System.out.println("New url visited successfully.");
				break;
			case 2:
				if (st.isEmpty()) {
					System.out.println("No page found!");
				} else {
					String page = st.pop();
					System.out.println("Going Back From " + page);
				}
				break;
			case 3:
				if (st.isEmpty()) {
					System.out.println("No page found!");
				} else {
					String page = st.peek();
					System.out.println("Current Page " + page);
				}
				break;
			case 4:
				if (st.isEmpty()) {
					System.out.println("No page found!");
				} else {
					System.out.println("------- History ---------");
					for (String s : st) {
						System.out.println(s);
					}
				}
				break;
			case 5:
				System.out.println("Closed");
				return;

			default:
				System.out.println("Invalid choice! Please try again.");

			}

		}
	}

}
