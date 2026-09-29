# 1D Slicing
import numpy as np
from pprint import pprint

sensor_reading = np.arange(10)
print("Original sensor readings:",sensor_reading,sep="\t:\t")
# scalar slicing
print("Scalar slicing (element at index 3):", sensor_reading[3], sep="\t:\t")
# reset a value
sensor_reading[3] = 99
print("After resetting element at index 3:", sensor_reading, sep="\t:\t")

# 1D Slicing
print("Slicing from index 2 to 5:", sensor_reading[2:6], sep="\t:\t")
print("Slicing with step 2:", sensor_reading[::2], sep="\t:\t")
print("Reversing the array:", sensor_reading[::-1], sep="\t:\t")
print("_" * 60)

# 2D Slicing
feature_matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
print("Original feature matrix:")
pprint(feature_matrix)
print("_" * 60)
print("Slicing first two rows and last two columns:")
pprint(feature_matrix[:2, 2:])
print("_" * 60)
print("Slicing with step 2 for rows and columns:")
pprint(feature_matrix[::2, ::2])
print("_" * 60)
print("Reversing the feature matrix:")
pprint(feature_matrix[::-1, ::-1])
print("_" * 60)


data_grid = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])
print("Original data grid:")
pprint(data_grid)

row_indices = np.arange(4)
print("Row indices:", row_indices) # [0, 1, 2, 3]
col_indices = np.array([0,2,0,1])
print("Column indices:", col_indices)
print("Selecting elements using row and column indices:")
pprint(data_grid[row_indices, col_indices]) # [1, 6, 7, 11]

# Mutation
print("Mutating elements using row and column indices:")
data_grid[row_indices, col_indices] = 999
pprint(data_grid)

print("_" * 60)