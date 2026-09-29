import numpy as np

A = np.array([[1, 2], [4, 5]])
print("A:\n", A)
B = np.array([[5,6], [7,8]])
print("B:\n", B)
# 1. Matrix multiplication C_ik = sum_j (A_ij * B_jk)
mat_mul_einsum = np.einsum('ij,jk->ik', A, B)
print("Matrix multiplication using einsum:\n", mat_mul_einsum)
print("@ operator for matrix multiplication:\n", A @ B)
