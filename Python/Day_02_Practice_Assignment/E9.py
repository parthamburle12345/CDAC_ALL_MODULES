"""
 Longest Palindromic Substring
Write a program that prompts the user to enter a text string and finds the longest substring within it that reads the same forward and backward. If there are multiple palindromic substrings of the same maximum length, print any one of them.

Sample Input: "babad"
Sample Output: "bab" (or "aba")
Sample Input: "cbbd"
Sample Output: "bb"

"""

text = input("Enter a string: ")

longest = ""

for i in range(len(text)):

    for j in range(i + 1, len(text) + 1):

        substring = text[i:j]

        if substring == substring[::-1]:

            if len(substring) > len(longest):
                longest = substring

print("Longest Palindromic Substring:", longest)