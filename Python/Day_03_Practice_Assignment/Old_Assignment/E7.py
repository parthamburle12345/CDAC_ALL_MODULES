"""
Right Shift List by K
Write a script that accepts a list and an integer 
K
, and shifts the list elements to the right by 
K
 positions. Elements shifted off the end should wrap around to the beginning.

Sample Input: lst = [1, 2, 3, 4, 5], K = 2
Sample Output: [4, 5, 1, 2, 3]

"""

lst = list(map(int, input("Enter list elements: ").split()))
k = int(input("Enter K: "))

k = k % len(lst)

result = lst[-k:] + lst[:-k]

print(result)