"""
Write a program that accepts a list of elements and returns a new list containing only the unique elements in the original order of occurrence. Do not use Python's built-in set conversion.

Sample Input: [1, 2, 2, 3, 4, 4, 1, 5]
Sample Output: [1, 2, 3, 4, 5]

"""

num = [1, 2, 2, 3, 4, 4, 1, 5]
unique=[]
for i in num:
    if i not in unique:   #checks whether the element is already in the new list.
        unique.append(i)   #adds it only if it isn't already there.
print(unique)        
