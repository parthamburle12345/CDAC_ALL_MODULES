"""
Multi-dimensional List Index Finder
Write a function find_element_indices(nested_list, target) that searches for a target item inside a 2D list (grid of elements) and returns its row and column index as a tuple (row, col). Return (-1, -1) if not found.

Sample Input: grid = [['a', 'b'], ['c', 'd']], target = 'c'
Sample Output: (1, 0)
"""

def find_element_indices(nested_list, target):

    for row in range(len(nested_list)):
        for col in range(len(nested_list[row])):

            if nested_list[row][col] == target:
                return (row, col)

    return (-1, -1)


grid = [['a', 'b'], ['c', 'd']]

target = input("Enter target: ")

print(find_element_indices(grid, target))