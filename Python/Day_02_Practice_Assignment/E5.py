"""
Write a program that accepts a string 
input from the user and outputs it in Title Case 
(capitalizing the first letter of each word and lowercasing the remaining letters).
 Do not use Python's built-in .title() method.

Sample Input: "WELCOME TO BANGALORE CITY"
Sample Output: "Welcome To Bangalore City"
"""



str = input("Enter a string: ")

words = str.split()

result = []

for i in words:
    word = i.lower()
    word = word[0].upper() + word[1:]
    result.append(word)

print(" ".join(result))