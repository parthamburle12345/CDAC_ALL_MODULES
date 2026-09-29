"""
Sentence Analysis (Character & Word Count)
Write a Python program that prompts the user to enter a sentence.
The program must count and display:

The total number of characters (including spaces and punctuation).
The total number of words.
Sample Input: "Learning Python is fun!"
Sample Output:
Total Characters: 23
Total Words: 4

"""
str = input("enter a string:")
char=len(str)
words=len(str.split())
print("total char:", char)

print("total words:", words)