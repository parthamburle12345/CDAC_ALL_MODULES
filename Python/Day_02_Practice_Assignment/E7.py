"""
Manual Substring Counter
Write a program that prompts the user to enter a main text string and a substring. Count how many times the substring appears in the main string without using Python's built-in .count() method.

Sample Input: (User inputs main string "banana" and substring "an")
Sample Output: 2

"""

str=input("enter a string:")
substring=input("enter a substring:")

count = 0

for i in range (len(str) - len(substring) + 1 ):
    if str[i:i + len(substring)] == substring:
        count+=1
print("occurance", count)        