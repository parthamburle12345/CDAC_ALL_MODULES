"""
benchmark_list_vs_numpy.py - Comparing execution speed of Python list vs. NumPy array.
"""

print('-'*70)

import time
import numpy as np

SIZE = 1_000_000

# 1. Python List: Element-wise doubling via list comprehension
py_list = list(range(SIZE))
start = time.time()
list_result = [x * 2 for x in py_list]
list_time = time.time() - start

# 2. NumPy Array: Element-wise doubling via vectorization
np_arr = np.arange(SIZE)
start = time.time()
np_result = np_arr * 2
numpy_time = time.time() - start

print(f"Python List time : {list_time:.4f} seconds")
print(f"NumPy Array time : {numpy_time:.4f} seconds")
print(f"-> NumPy is {list_time / numpy_time:.1f}x faster!")
