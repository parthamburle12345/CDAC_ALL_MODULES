

prices = [2,3,4,5,6,7,8]

'''
IQR => interquartile Range

step 1 find the median of the population  
median = 5 
c1 = [2,3,4]  median  = 3  =25th percentile  Q1
c2 = [6,7,8]  median  = 7  = 75th percentile  Q3
IQR = Q3 - Q1

'''

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
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

print("Finding IQR using numpy:")
# find IQR using numpy
import numpy as np
'''
list of possible method parameter of np.percentile
method='linear'  # default method for interpolation
method='lower'   # always round down to the nearest data point
method='higher'  # always round up to the nearest data point
method='midpoint' # average of the two nearest data points
method='nearest'  # nearest data point
method = 'weibull'  # Weibull interpolation method
method='cubic'  # cubic interpolation method
method='polynomial'  # polynomial interpolation method
method='all'  # use all available methods
method = "closest_observation"  # closest observation method

'''
Q1_np = np.percentile(sorted_prices, 25) 
Q3_np = np.percentile(sorted_prices, 75)
IQR_np = Q3_np - Q1_np
print("Q1 (numpy):", Q1_np)
print("Q3 (numpy):", Q3_np)
print("IQR (numpy):", IQR_np)   

# find IQR using scipy
from scipy.stats import iqr
IQR_scipy = iqr(sorted_prices)
print("IQR (scipy):", IQR_scipy)

