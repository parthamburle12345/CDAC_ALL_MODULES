"""
Leap Year Checker
Write a program that takes a year as input from the user and checks whether it is a leap year or not.

Leap Year Criteria: A year is a leap year if it is divisible by 4, except for century years (ending in 00), which must also be divisible by 400.
Sample Input: 2024
Sample Output: 2024 is a Leap Year.

"""

year=int(input("enter a year:"))
if year<1:
    print(f"{year} is not valid.")
if year % 400 == 0 or (year % 4 == 0 and year % 100!= 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap .")