"""
Write a function that finds the second largest number 
in a list of integers. Return None if the list has fewer than 2 unique elements.

Sample Input: [12, 35, 1, 10, 34, 1]
Sample Output: 34

"""

def second_largest(numbers):

    unique = []

    for i in numbers:
        if i not in unique:
            unique.append(i)

    if len(unique) < 2:
        return None

    unique.sort()

    return unique[-2]


numbers = list(map(int, input("Enter numbers: ").split()))

print(second_largest(numbers))