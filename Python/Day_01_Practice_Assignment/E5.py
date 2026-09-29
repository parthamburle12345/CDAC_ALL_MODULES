""""
Basic Operator Calculator
Create a program that takes two numbers and a math operator (+, -, *, /) from the user, performs the corresponding calculation, and prints the result.

Sample Input: num1=15, num2=3, operator='/'
Sample Output: Result: 5.0
"""

num1=float(input("enter number 1:"))
num2=float(input("enter number 2:"))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator")
    result = None

if result is not None:
    print("Result:", result)
