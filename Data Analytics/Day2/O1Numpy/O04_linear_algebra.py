import numpy as np

# Linear algebra operations with NumPy arrays
# Create two 1D arrays
a = np.array([9, 10])
b = np.array([11,12])

print("a:\n", a)
print("b:\n", b)

# Dot product of two 1D arrays
dot_product = np.dot(a, b) # computation ( 9*11 + 10*12 = 219)
print("Dot product of a and b: ", dot_product)

# dot product operator
print("Dot product of a and b using operator (@): ", a @ b)

# linear algebra with 2D arrays
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("A:\n", A)
print("B:\n", B)

# Matrix multiplication
C = np.dot(A, B)
print("Matrix multiplication of A and B:\n", C)

# Matrix multiplication using operator (@)
print("Matrix multiplication of A and B using operator (@):\n", A @ B)

# Transpose of a matrix
matrix = np.array([[1, 2,3], [4,5,6]])
print("Original matrix:\n", matrix)
print("Transpose of the matrix:\n", matrix.T)

# Note : for 1D arrays, the transpose operation has no effect
a = np.array([9, 10])
print("1D array a:\n", a)
print("Transpose of 1D array a:\n", a.T)
print("shape a and a.t:\n", a.shape, a.T.shape)

# to transpose a 1D array into a 2D column vector
b = np.array([9, 10])[:, np.newaxis]
print("1D array b as a 2D column vector:\n", b)
print("shape of b:\n", b.shape)

# BroadCasting
matrix_grid = np.array([[1, 2, 3], [4, 5, 6]])
print("Original matrix grid:\n", matrix_grid)
bias_scalar = 10
biased_matrix = matrix_grid + bias_scalar
print("Biased matrix:\n", biased_matrix)

# another bias on matrix_grid using a 1D array
bias_array = np.array([1, 2, 3])
biased_matrix_with_array = matrix_grid + bias_array
print("Biased matrix with 1D array:\n", biased_matrix_with_array)

matrix_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matrix data:\n", matrix_data)
biased_row_array = np.array([10, 20, 30])
biased_matrix_with_row_array = matrix_data + biased_row_array
print("Biased matrix with row array:\n", biased_matrix_with_row_array)

# another bias on matrix_data using a 2D column vector
biased_column_array = np.array([[100], [200], [300]])
biased_matrix_with_column_array = matrix_data + biased_column_array
print("Biased matrix with column array:\n", biased_matrix_with_column_array)


print("_" * 60)
# problem 
vec_x = np.array([1, 2, 3]) # shape (3,)
vec_y = np.array([4, 5]) # shape (2,)
print("vec_x:\n", vec_x)
print("vec_y:\n", vec_y)
# change vec_x to shape (3,1)
vec_x_col = vec_x[:, np.newaxis]
print("vec_x as a column vector:\n", vec_x_col)
print("shape of vec_x_col:\n", vec_x_col.shape)

print("_" * 60)
print("vec_x_col as a column vector:\n", vec_x_col)
print("vec_y:\n", vec_y)
new_grid = vec_x_col + vec_y
print("New grid after broadcasting vec_x_col and vec_y:\n", new_grid)
print("_" * 60)