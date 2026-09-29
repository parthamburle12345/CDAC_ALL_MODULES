"""
List Comprehension Challenge
Write a list comprehension statement that filters a list of numbers from 1 to 100, keeping only those numbers that are divisible by both 3 and 5.

Sample Output: [15, 30, 45, 60, 75, 90]
"""

numbers = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]

print(numbers)