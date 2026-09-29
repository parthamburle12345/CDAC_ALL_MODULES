"""
Example of a `for` loop.

Accept two numbers from the user, and print all prime numbers between them.
"""

def main():
    start = int(input("Enter the first number: "))
    end = int(input("Enter the second number: "))

    if start > end:
        print("first number must be smaller than the second number.")
        return

    for n in range(start, end+1):
        limit = n // 2
        for d in range(2, limit+1):
            if n % d == 0:
                break
        else:
            print(n, end=", ")

print("=" * 80)
main()
print()
