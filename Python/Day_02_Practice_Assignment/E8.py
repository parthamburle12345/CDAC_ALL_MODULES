"""
Name Anonymizer
Write a program that prompts the user to enter a full name (first name, middle name, last name) and anonymizes it. The output should print the initials of the first and middle names followed by the full last name. If the name consists of only a single word, print it as-is.

Sample Input: "Vinod Kumar Kayartaya"
Sample Output: "V. K. Kayartaya"
Sample Input: "Bangalore"
Sample Output: "Bangalore"

"""

name = input("enter a full name: ")
words=name.split()     #["Vinod", "Kumar", "Kayartaya"]

if len(words) == 1:     # checks the total no of words in string
    print(name)     #if only 1 number of string then print as it is
else:
    result = " "

    for i in range (len(words) - 1):
        result += words[i][0].upper() + ". "    # just filling result by extracting the 1st letter and using uppercase.
    result += words[-1] 
    print(result)       #Give me the last word.