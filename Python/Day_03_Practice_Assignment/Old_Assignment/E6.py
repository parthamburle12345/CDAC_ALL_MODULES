"""
 Matrix Transpose
Write a program that computes the transpose of a 3x3 matrix represented as a list of lists.

Sample Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Sample Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = []

for i in range(3):
    row = []

    for j in range(3):
        row.append(matrix[j][i])

    transpose.append(row)

print(transpose)