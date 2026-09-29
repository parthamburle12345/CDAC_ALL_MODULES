"""
Multiplication Table Generator
Write a program that takes an integer from the user
 and prints its multiplication table from 1 to 10.
"""

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)