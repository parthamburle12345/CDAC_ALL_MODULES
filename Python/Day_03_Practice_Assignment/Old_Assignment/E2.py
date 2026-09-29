"""
Merge and Sort Lists
Write a program that takes two lists of integers, merges them,
 and sorts the resulting list in ascending order.

Sample Input: list1 = [5, 1, 9], list2 = [8, 2, 4]
Sample Output: [1, 2, 4, 5, 8, 9]


"""
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

list1.extend(list2)

list1.sort()

print("Sorted list:", list1)