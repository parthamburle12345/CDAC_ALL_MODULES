package CharacterBasedFileWriteandRead;

import java.io.*;
import java.util.*;


public class CharacterBasedFileWriteandRead {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Enter a string: ");
            String input = sc.nextLine();

            FileWriter fw = new FileWriter("data.txt");
            fw.write(input);
            fw.close();

            FileReader fr = new FileReader("data.txt");

            int ch;
            int uppercase = 0;
            int lowercase = 0;
            int digits = 0;
            int special = 0;
            int spaces = 0;

            StringBuilder data = new StringBuilder();

            while ((ch = fr.read()) !=-1) {
                char c = (char) ch;
                data.append(c);

                if (Character.isUpperCase(c)) {
                    uppercase++;
                } else if (Character.isLowerCase(c)) {
                    lowercase++;
                } else if (Character.isDigit(c)) {
                    digits++;
                } else if (c == ' ') {
                    spaces++;
                } else {
                    special++;
                }
            }

            fr.close();

            System.out.println("\nData Read from File:");
            System.out.println(data);

            System.out.println("\nUppercase Characters: " + uppercase);
            System.out.println("Lowercase Characters: " + lowercase);
            System.out.println("Digits: " + digits);
            System.out.println("Special Characters: " + special);
            System.out.println("Spaces: " + spaces);

        } catch (IOException e) {
            System.out.println("File error: " + e.getMessage());
        }

        sc.close();
    }
}

