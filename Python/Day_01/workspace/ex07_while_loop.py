"""
This is an example script to understand the use of `while` loop.

Accept a number from the user and check if it is a prime or not.
"""

def main():
    while True:
        num = int(input("Enter a positive number: "))

        if num < 0:
            print("Please retry with a positive number")
            continue

        break

    limit = num // 2
    d = 2

    while d <= limit:
        if num % d == 0:
            print(f"{num} is not a prime, it was divided by {d}")
            break
        d += 1
    else:
        # this is reached only if the `break` was not encountered inside the while loop
        print(f"{num} is a prime number")


print("="*80)
main()
