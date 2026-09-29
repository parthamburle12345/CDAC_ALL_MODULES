# what are pandas?
# Pandas is a powerful data manipulation and analysis library for Python.
# It provides data structures like Series (1D) and DataFrame (2D) to work with structured data efficiently.

# Example usage:
import pandas as pd

# series example
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print("Series:\n", series)

players = ["sachin", "virat", "rahul", "ms dhoni", "rohit"]
# series from the list
players_series = pd.Series(players,name = "Players")
print("Players Series:\n", players_series)
print("_" * 60)

# integer payload to series
integer_series = pd.Series([10, 20, 30, 40, 50], name="Integers")
print("Integer Series:\n", integer_series)
print("_" * 60)

players_1 = ["sachin", "virat", "rahul", "ms dhoni", "rohit"]
# series from the list
col_index = [100,200,300,400,500]
players_1_series = pd.Series(players_1, index=col_index, name="Players 1")
print("Players 1 Series:\n", players_1_series)

print("_" * 60)
players_role = {
    "sachin": "batsman",
    "virat": "captain",
    "rahul": "batsman",
    "dhoni": "wicketkeeper",
    "rohit": "batsman"
}
players_role_series = pd.Series(players_role, name="Players Role")
print("Players Role Series:\n", players_role_series)
print("_" * 60)

# intermediate
data_dict = {'a':100,'b':200,'c':300}
data_dict_series = pd.Series(data_dict, name="Data Dict", index=['b', 'a', 'c','d'])
print("Data Dict Series:\n", data_dict_series)

print("_" * 60)
print("_" * 60)

# vectorized operations on series
vector_series = pd.Series([1, 2, 3, 4, 5], name="Vector")
print("Original Vector Series:\n", vector_series)
print("Vector Series after adding 10:\n", vector_series + 10)
print("Vector Series after multiplying by 2:\n", vector_series * 2)
print("Vector Series after subtracting 3:\n", vector_series - 3)
print("Vector Series after dividing by 2:\n", vector_series / 2)
print("the sum of Vector Series:\n", vector_series.sum())
print("the mean of Vector Series:\n", vector_series.mean())
print("the maximum of Vector Series:\n", vector_series.max())
print("the minimum of Vector Series:\n", vector_series.min())
print("the standard deviation of Vector Series:\n", vector_series.std())
print("the variance of Vector Series:\n", vector_series.var())
print("the median of Vector Series:\n", vector_series.median())
print("the mode of Vector Series:\n", vector_series.mode())
print("the product of Vector Series:\n", vector_series.prod())


print("_" * 60)
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
fruits_day = pd.Series(fruits, index=weekdays, name="Fruits Day")
print("Fruits Day Series:\n", fruits_day)
print("_" * 60)
print("Values Array",fruits_day.values)
print("Index Array",fruits_day.index)
print("Data type of Fruits Day Series:", fruits_day.dtype)
print("Shape of Fruits Day Series:", fruits_day.shape)
print("Number of dimensions of Fruits Day Series:", fruits_day.ndim)
print("Size of Fruits Day Series:", fruits_day.size)
print("Memory usage of Fruits Day Series:", fruits_day.memory_usage())

print("_" * 60)