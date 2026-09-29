"""
Odd or Even Checker
Write a program that prompts the user for an integer and prints whether it is even or odd.

"""

num = int(input("enter a num to check odd or even"))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")    