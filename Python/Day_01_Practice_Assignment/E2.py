"""
Fibonacci Sequence Generator
Write a Python script to print the first N
N terms of the Fibonacci sequence, where N
N is provided by the user.
"""

num = int(input("enter a number:"))
a=0
b=1
for i in range(num):
    print(a, end = "")
    c=a+b
    a=b
    b=c