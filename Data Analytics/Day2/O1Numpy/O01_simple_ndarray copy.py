import numpy as np
import sys

vector_1 = np.array([10,20,30,40,50])
matrix_2d = np.array([[10,20,30,40,50],[60,70,80,90,100]])

# Intro to ND Array
print("1D Array")
print("vector_1",vector_1,sep="\t:\t")
print("type(vector_1)",type(vector_1),sep="\t:\t")
print("vector_1.dtype",vector_1.dtype,sep="\t:\t")
print("vector_1.shape",vector_1.shape,sep="\t:\t")
print("size(vector_1)",sys.getsizeof(vector_1),sep="\t:\t")
print("bytes(vector_1)",vector_1.nbytes,sep="\t:\t")
print("_" * 60)

print("matrix_2d")
print(matrix_2d)
print("matrix_2d.shape",matrix_2d.shape,sep="\t:\t")
print("python size(matrix_2d)",sys.getsizeof(matrix_2d),sep="\t:\t")
print("numpy buffer bytes(vector_1)",matrix_2d.nbytes,sep="\t:\t")
print("_" * 60)

#2. Tensor Initialization (Factory)
zero_matrix = np.zeros((3,4),dtype=int)
one_matrix = np.ones((3,4),np.float64)
const_matrix = np.full((3,4),5.5) # type inference
identity_matrix = np.eye(4)

print("zero_matrix".center(60,'_'))
print(zero_matrix)
print("one_matrix".center(60,'_'))
print(one_matrix)
print("const_matrix".center(60,'_'))
print(const_matrix)
print("identity_matrix".center(60,'_'))
print(identity_matrix)
print("_" * 60)

# 3. Vectorized operation
print("Vectorized operation".center(60,"="))
inch_measures = np.array([1.0,2.5,5.0,10.0])
cms_measures = inch_measures * 2.54
print("Inches : ",inch_measures)
print("Cms    : ",cms_measures)
print("_" * 60)

n1 = np.array([10,20,30])
n2 = np.array([2,4,6])

print(n1,n2,sep="\n")
print("sum",n1 + n2,sep="\t:\t")
print("product",n1 * n2,sep="\t:\t")
print("Ratio",n1 / n2,sep="\t:\t")

print("="* 60)

# intermediate (Algorithm Rigor & Data Filtering)
# Boolean mask
rng = np.random.default_rng(seed=100)
my_gen_data = rng.uniform(low = 0.2, high=0.8, size=(4,4))
print(my_gen_data)

mask = my_gen_data > 0.5
extrat_data = my_gen_data[mask]
print(mask)
print("_"* 60)
print(extrat_data)

print("_"* 60)
print("vector rounded ",np.round(my_gen_data,2))
print("vector rounded ",np.round(extrat_data,2))
print("_"* 60)
print("vector floor ",np.floor(extrat_data))
print("vector ceil ",np.ceil(extrat_data))

print("_"* 60)
print("_"* 60)

# Data type Precision
int_var = np.array([1,2,3]) # type inference
float_var = np.array([1.0,2.0,3.0])
float_var_2 = np.array([1.0,2.0,3.0],dtype=np.float32)

print(f"int_var type :  {int_var.dtype} -> ({int_var.itemsize}) bytes/item")
print(f"float_var type :  {float_var.dtype} -> ({float_var.itemsize}) bytes/item")
print(f"float_var_2 type :  {float_var_2.dtype} -> ({float_var_2.itemsize}) bytes/item")
print("_"* 60)

# char inspection
dt_double = np.dtype("float64")
print(f"Type char of float64 is : {dt_double.char}")
print(f"Type C-Class Equivalent is : {dt_double.type}")
print("_"* 60)

print("Datatype Aliases")
print(f" -  float64 (d) : {np.dtype('d')}")
print(f" -  float32 (f) : {np.dtype('f')}")
print(f" -  float16 (f2) : {np.dtype('f2')}")
print("_"* 60)
from pprint import pprint
pprint(np.sctypeDict,width=40,indent=2)
print("_"* 60)
pprint({np.dtype(k).char:np.dtype(k) for k in np.sctypeDict},width=40,indent=2)
print("_"* 60)

# custom Data data types
metric_data = np.dtype([
    ('device_id',str,16),
    ("status_code",np.int32),
    ("cpu_load",np.float32),
    ("latency_ms",np.float64)
])

# Allocate memory
sensor_data = np.array([
    ('sensor1', 200, 35.5, 12.4),
    ('sensor2', 200, 42.1, 15.8),
    ('sensor3', 500, 28.7, 10.2),
], dtype=metric_data)

print("sensor_data")
print(sensor_data)
print(sensor_data["device_id"])
print(sensor_data["latency_ms"])

print(sensor_data[1])

 