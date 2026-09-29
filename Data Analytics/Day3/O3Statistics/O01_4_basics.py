from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(100) # which ensures reproducibility of random numbers
roll_a_die = np.random.randint(low=1, high=7,size=10) # simulates rolling a six-sided die
print("Roll a die: ", roll_a_die)
# The type of distribution for rolling a die is uniform discrete distribution

# Roll 2 dice 
dice_1 = np.random.randint(low=1, high=7,size=10)
dice_2 = np.random.randint(low=1, high=7,size=10)
print("Roll 2 dice: ", dice_1, dice_2)
totals = dice_1 + dice_2
print("Totals of 2 dice: ", totals)
# The type of distribution for the sum of two dice is approximately a discrete triangular distribution
# normal distribution can be used as an approximation for the sum of two dice when the number of rolls is large
# Example of using normal distribution as an approximation


values = np.random.uniform(low=-10.0, high=10.0, size=10) 
print("Uniformly distributed values: ", values)
# plt.hist(values, bins=10, edgecolor='black')
# plt.title("Histogram of Uniformly Distributed Values")
# plt.show()

x = np.arange(-10.0, 10.0, 0.1)
# y = np.random.normal(loc=0.0, scale=1.0, size=len(x))

y = norm.pdf(x,scale=1,loc=0)
plt.plot(x, y)
plt.title("Normal/Gassian Distribution Approximation")
plt.show()