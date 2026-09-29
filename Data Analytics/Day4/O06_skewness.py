'''
what is skewness?
Skewness is a measure of the asymmetry of the probability distribution of a real-valued
random variable about its mean. 

You have startup with 5 employees
Salaries = [40,45,50,55,310]

step 1 calculate the mean of the salaries
mu = (40 + 45 + 50 + 55 + 310) / 5 = 100

step 2 calculate the median of the salaries
median = 50
decissions
if mu > median  => positively skewed distribution : average pulled upwards : the tail is long on the right side : its called (right-skewed)
if mu < median  => negatively skewed distribution : average pulled downwards : the tail is long on the left side : its called (left-skewed)
if mu == median => symmetric distribution   : average is centered   : the tails are of equal length on both sides : its called (zero-skewed)

step 3 Calculate Central moment (m3)
 (Ⅹ_i - mu)^3
 40 -> 40 -100 = -60  -> (-60)^3 = -216000
 45 -> 45 -100 = -55  -> (-55)^3 = -166375
 50 -> 50 -100 = -50  -> (-50)^3 = -125000
 55 -> 55 -100 = -45  -> (-45)^3 = -91125
 310 -> 310 -100 = 210  -> (210)^3 = 9261000
 sum = -216000 + -166375 + -125000 + -91125 + 9261000 = 8734500

 step 4 standardize skewness coefficient (γ1)
gamma1 = m3 / ( (1/n) * Σ((x_i - mu)^2) )^(3/2)


m3 = (1/n) * Σ((x_i - mu)^3)
'''

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
salaries = np.array([40, 45, 50, 55, 310])

mean_val = np.mean(salaries)
median_val = np.median(salaries)
skewness_val = stats.skew(salaries)
print("Mean:", mean_val)
print("Median:", median_val)
print("Skewness:", skewness_val)

# plt.hist(salaries, bins=10, edgecolor='black')
# plt.axvline(mean_val, color='r', linestyle='dashed', linewidth=1, label='Mean')
# plt.axvline(median_val, color='g', linestyle='dashed', linewidth=1, label='Median')
# plt.legend()
# plt.show()

plt.boxplot(salaries,vert=False)
plt.show()

# problem:
retirement_age = [35,62,65,67,71]