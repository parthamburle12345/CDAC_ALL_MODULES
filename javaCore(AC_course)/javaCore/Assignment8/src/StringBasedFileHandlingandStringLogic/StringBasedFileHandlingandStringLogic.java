package StringBasedFileHandlingandStringLogic;

import java.io.*;
import java.util.*;

public class StringBasedFileHandlingandStringLogic {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		try {
			System.out.print("Enter a sentence: ");
			String input = sc.nextLine();

			FileWriter fw = new FileWriter("sentence.txt");
			fw.write(input);
			fw.close();

			BufferedReader br = new BufferedReader(new FileReader("sentence.txt"));

			String sentence = br.readLine();
			br.close();

			String[] words = sentence.trim().split(" ");
			int wordCount = words.length;

			int vowels = 0;
			int consonants = 0;

			for (int i = 0; i < sentence.length(); i++) {
				char c = Character.toLowerCase(sentence.charAt(i));

				if (c >= 'a' && c <= 'z') {
					if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
						vowels++;
					} else {
						consonants++;
					}
				}
			}

			String longestWord = words[0];

			for (String word : words) {
				if (word.length() > longestWord.length()) {
					longestWord = word;
				}
			}

			String reversed = new StringBuilder(sentence).reverse().toString();

			String uppercase = sentence.toUpperCase();

			System.out.println("\nNumber of Words: " + wordCount);
			System.out.println("Number of Vowels: " + vowels);
			System.out.println("Number of Consonants: " + consonants);
			System.out.println("Longest Word: " + longestWord);

			System.out.println("\nUppercase:");
			System.out.println(uppercase);

			System.out.println("\nReversed:");
			System.out.println(reversed);

		} catch (IOException e) {
			System.out.println("File error: " + e.getMessage());
		}

		sc.close();
	}
}
