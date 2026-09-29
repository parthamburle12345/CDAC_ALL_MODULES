import numpy as np

# Vectorized mathematical operations with NumPy arrays
x = np.array([[1.0,2.0],[3.0,4.0]],dtype=np.float64)
y = np.array([[5.0,6.0],[7.0,8.0]],dtype=np.float64)

# Print the original arrays
print("x:\n", x)
print("y:\n", y)

# Element-wise addition
print("x + y: operator (+)\n", x + y)
print("Ufunc (np.add):\n", np.add(x, y))

# Element-wise subtraction
print("x - y: operator (-)\n", x - y)
print("Ufunc (np.subtract):\n", np.subtract(x, y))

# Element-wise multiplication
print("x * y: operator (*)\n", x * y)
print("Ufunc (np.multiply):\n", np.multiply(x, y))

# Element-wise division
print("x / y: operator (/)\n", x / y)
print("Ufunc (np.divide):\n", np.divide(x, y))

# Element-wise power
print("x ** y: operator (**)\n", x ** y)
print("Ufunc (np.power):\n", np.power(x, y))

# Element-wise square root
print("np.sqrt(x):\n", np.sqrt(x))

# Element-wise exponential
print("np.exp(x):\n", np.exp(x))

# Element-wise natural logarithm
print("np.log(x):\n", np.log(x))

print("_" * 60)
print("_" * 60)
# feature_matrix 3 samples(rows) and 3 features(columns)
dataset = np.array([[10, 20, 30],
                    [40, 50, 60],
                    [70, 80, 90]])
print("dataset:\n", dataset)

# global reduction (sum,mean)
print("Global sum:\n", np.sum(dataset))
print("Global mean:\n", np.mean(dataset))

# column-wise reduction
print("Column-wise sum:\n", np.sum(dataset, axis=0))
print("Column-wise mean:\n", np.mean(dataset, axis=0))

# row-wise reduction
print("Row-wise sum:\n", np.sum(dataset, axis=1))
print("Row-wise mean:\n", np.mean(dataset, axis=1)) 
print("_" * 60)

# Reusing Buffer via the 'out' parameter
mamoth_feature = np.ones((1000,1000), dtype=np.float64)
scale_factor = 2.5
output_buffer = np.empty_like(mamoth_feature)
# print("Before scaling:\n", mamoth_feature)
# print("output_buffer before scaling:\n", output_buffer)
# Perform the scaling operation using the 'out' parameter
np.multiply(mamoth_feature, scale_factor, out=output_buffer)
# print("After scaling:\n", output_buffer)
# print("mamoth_feature remains unchanged:\n", mamoth_feature)

print("shape output_buffer:\n", output_buffer.shape)
print("sample output_buffer:\n", output_buffer[:5,:5])
print("Memory buffer identity check:\n",np.may_share_memory(mamoth_feature, output_buffer))
print("_" * 60)

# implement Z-score normalization
raw_feature = np.array([[150.0, 2.5,12.0],
                        [170.0, 3.8,15.0],
                        [140.0, 1.9,10.0],
                        [180.0, 4.2,18.0],
                        ])

col_mean = np.mean(raw_feature, axis=0)
col_std = np.std(raw_feature, axis=0)
z_score_normalized = (raw_feature - col_mean) / col_std
print("Z-score normalized feature:\n", z_score_normalized)
print("Column-wise mean of raw feature:\n", np.round(col_mean, 2))
print("Column-wise std of raw feature:\n", np.round(col_std, 2))

# validation
print("Validation - Column-wise mean of Z-score normalized feature:\n", np.round(np.mean(z_score_normalized, axis=0), 2))
print("Validation - Column-wise std of Z-score normalized feature:\n", np.round(np.std(z_score_normalized, axis=0), 2))
