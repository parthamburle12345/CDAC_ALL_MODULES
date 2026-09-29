"""
Prime Number Checker
Write a program that checks whether a positive integer entered by the user is a prime number.

Logic: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
Sample Input: 17
Sample Output: 17 is a prime number.
"""

def main():
    num = int(input("enter a number:"))

    if num < 0:
        print("enter a positive number again.")
        return
    limit=num//2
    d=2
    while d<=limit:
        if num%d==0:
            print(f"{num} is not a prime ")
            break
        d +=1
    if d > limit:
        print(f"{num} is a prime.")

main()

        