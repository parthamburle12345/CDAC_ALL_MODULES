import sys
from pprint import pprint

import numpy as np


def print_section(title):
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


def print_value(label, value):
    print(f"{label:<32}: {value}")


vector_1 = np.array([10, 20, 30, 40, 50])
matrix_2d = np.array([[10, 20, 30, 40, 50], [60, 70, 80, 90, 100]])

# 1. Introduction to ndarrays
print_section("1. INTRODUCTION TO NDARRAYS")
print_value("1D array", vector_1)
print_value("Array type", type(vector_1))
print_value("Data type", vector_1.dtype)
print_value("Shape", vector_1.shape)
print_value("Python object size (bytes)", sys.getsizeof(vector_1))
print_value("NumPy buffer size (bytes)", vector_1.nbytes)

print("\n2D array:")
print(matrix_2d)
print_value("Shape", matrix_2d.shape)
print_value("Python object size (bytes)", sys.getsizeof(matrix_2d))
print_value("NumPy buffer size (bytes)", matrix_2d.nbytes)

# 2. Tensor initialization using factory functions
zero_matrix = np.zeros((3, 4), dtype=int)
one_matrix = np.ones((3, 4), np.float64)
const_matrix = np.full((3, 4), 5.5)
identity_matrix = np.eye(4)

print_section("2. TENSOR INITIALIZATION (FACTORY FUNCTIONS)")
print("Zero matrix:")
print(zero_matrix)
print("\nOne matrix:")
print(one_matrix)
print("\nConstant matrix:")
print(const_matrix)
print("\nIdentity matrix:")
print(identity_matrix)

# 3. Vectorized operations
print_section("3. VECTORIZED OPERATIONS")
inch_measures = np.array([1.0, 2.5, 5.0, 10.0])
cms_measures = inch_measures * 2.54
print_value("Measurements in inches", inch_measures)
print_value("Measurements in centimetres", cms_measures)

n1 = np.array([10, 20, 30])
n2 = np.array([2, 4, 6])
print("\nElement-wise arithmetic:")
print_value("First array", n1)
print_value("Second array", n2)
print_value("Sum", n1 + n2)
print_value("Product", n1 * n2)
print_value("Ratio", n1 / n2)

# 4. Data generation and filtering
print_section("4. DATA GENERATION AND BOOLEAN FILTERING")
rng = np.random.default_rng(seed=100)
my_gen_data = rng.uniform(low=0.2, high=0.8, size=(4, 4))
print("Generated data:")
print(my_gen_data)

mask = my_gen_data > 0.5
filtered_data = my_gen_data[mask]
print("\nBoolean mask (values > 0.5):")
print(mask)
print_value("Filtered values", filtered_data)
print_value("Rounded generated data", np.round(my_gen_data, 2))
print_value("Rounded filtered data", np.round(filtered_data, 2))
print_value("Floor of filtered data", np.floor(filtered_data))
print_value("Ceiling of filtered data", np.ceil(filtered_data))

# 5. Data type precision
print_section("5. DATA TYPE PRECISION")
int_var = np.array([1, 2, 3])
float_var = np.array([1.0, 2.0, 3.0])
float_var_2 = np.array([1.0, 2.0, 3.0], dtype=np.float32)
print_value("Integer array", f"{int_var.dtype} ({int_var.itemsize} bytes/item)")
print_value("Default float array", f"{float_var.dtype} ({float_var.itemsize} bytes/item)")
print_value("32-bit float array", f"{float_var_2.dtype} ({float_var_2.itemsize} bytes/item)")

# 6. Data type character inspection
print_section("6. DATA TYPE CHARACTER INSPECTION")
dt_double = np.dtype("float64")
print_value("Type character for float64", dt_double.char)
print_value("C-class equivalent", dt_double.type)

# 7. Data type aliases
print_section("7. DATA TYPE ALIASES")
print_value("float64 (d)", np.dtype("d"))
print_value("float32 (f)", np.dtype("f"))
print_value("float16 (f2)", np.dtype("f2"))

# 8. NumPy scalar type dictionaries
print_section("8. NUMPY SCALAR TYPE DICTIONARIES")
print("Scalar type dictionary:")
pprint(np.sctypeDict, width=40, indent=2)
print("\nScalar type characters and dtypes:")
pprint({np.dtype(k).char: np.dtype(k) for k in np.sctypeDict}, width=40, indent=2)

# 9. Custom structured data types
print_section("9. CUSTOM STRUCTURED DATA TYPES")
metric_data = np.dtype(
    [
        ("device_id", str, 16),
        ("status_code", np.int32),
        ("cpu_load", np.float32),
        ("latency_ms", np.float64),
    ]
)

sensor_data = np.array(
    [
        ("sensor1", 200, 35.5, 12.4),
        ("sensor2", 200, 42.1, 15.8),
        ("sensor3", 500, 28.7, 10.2),
    ],
    dtype=metric_data,
)

print("Structured sensor data:")
print(sensor_data)
print_value("Device IDs", sensor_data["device_id"])
print_value("Latency (ms)", sensor_data["latency_ms"])
print_value("Second sensor record", sensor_data[1])
