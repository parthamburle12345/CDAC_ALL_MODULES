"""
List Intersection without Sets
Write a function that returns the intersection (common elements) of two list structures without converting them to sets. Do not allow duplicate common values in the output.

Sample Input: l1 = [1, 2, 2, 3], l2 = [2, 2, 4]
Sample Output: [2]
"""

def intersection(l1, l2):
    result = []

    for i in l1:
        if i in l2 and i not in result:
            result.append(i)

    return result


l1 = list(map(int, input("Enter first list: ").split()))
l2 = list(map(int, input("Enter second list: ").split()))

print(intersection(l1, l2))