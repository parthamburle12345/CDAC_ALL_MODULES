import pandas as pd

# df with name, age, gender
df_cricket = pd.DataFrame({
    "name": ["sachin", "virat", "rahul", "ms dhoni", "rohit",
             "mithali","anjali","priya","neha" ],
    "age": [50, 36, 32, 41, 34, 40, 28, 25, 30],
    "gender": ["male", "male", "male", "male", "male", 
               "female", "female", "female", "female"]
})
print("Cricket DataFrame:\n", df_cricket)
print("_" * 60)

# basic info about the DataFrame
print("DataFrame Info:\n")
print(df_cricket.info()) # info : provides a concise summary of the DataFrame, including the index dtype, column dtypes, non-null values, and memory usage.

# extract age column into a series
age_series = df_cricket["age"]
print("Age Column:\n", age_series)
print("Type of Age Column:\n", type(age_series))
print("Summary of Age Column:\n", age_series.describe()) # describe : generates descriptive statistics of the series, including count, mean, std, min, 25%, 50%, 75%, and max.
print("_" * 60)
print("Summary of DataFrame:\n", df_cricket.describe().T)
print("_" * 60)
