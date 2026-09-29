'''
list of methods for np.percentile function
print("Finding IQR using numpy:")
1. linear
2. lower
3. higher
4. midpoint
5. nearest
6. weibull
7. cubic
8. polynomial
9. all
10. closest_observation

list of Hyndman & Fan methods for quantile estimation
Hyndman & Fan method 1 : Inverse of empirical distribution function (EDF)
Hyndman & Fan method 2 : Similar to method 1 but with averaging at discontinuities
Hyndman & Fan method 3 : Nearest order statistic
Hyndman & Fan method 4 : Linear interpolation of the empirical CDF
Hyndman & Fan method 5 : Piecewise linear function with averaging
Hyndman & Fan method 6 : Similar to method 5 but with different averaging
Hyndman & Fan method 7 : Default method in R (used by quantile function)
Hyndman & Fan method 8 : Similar to method 7 but with different averaging
Hyndman & Fan method 9 : Another variant of linear interpolation
'''
import numpy as np
prices = [2,3,4,5,6,7,8]
def find_median(data):
    data_len = len(data)
    mid = data_len // 2
    if mid % 2 == 0:
        return (data[mid] + data[mid-1])/2.0
    return data[mid]

sorted_prices = sorted(prices)

count_elem = len(sorted_prices)
mid_point = count_elem // 2

lower_half = sorted_prices[:mid_point]
upper_half = sorted_prices[mid_point+1:]

Q1 = find_median(lower_half)
Q3 = find_median(upper_half)

IQR = Q3 - Q1

print("original prices:", sorted_prices)
print(f"Original Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
# find IQR using numpy
print("=" * 60)
methods = ['linear', 'lower', 'higher', 'midpoint', 'nearest', 'weibull', 'cubic', 'polynomial', 'all', 'closest_observation']
print("25th and 75th percentiles using different methods:")
for idx, meth in enumerate(methods,1):
    try:                                    
                Q1_method = np.percentile(sorted_prices, 25, method=meth)
                Q3_method = np.percentile(sorted_prices, 75, method=meth)
                IQR_method = Q3_method - Q1_method
                print(f"Method {idx}: {meth}")
                print(f"Q1: {Q1_method}, Q3: {Q3_method}, IQR: {IQR_method}")
    except Exception as e:
                print("Invalid method:", meth)
    finally:
                print("_"* 60)
