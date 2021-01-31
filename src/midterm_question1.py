#!/usr/bin/env python
# Name surname: Melih Safa Celik
# Student ID: 010180519
# Probability and Statistics Midterm 04.01.2020
# Question 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

array = np.array([0,1,0,1,8,0,5,1,9,0,1,0,1,8,0,5,1,9,0,1,0,1,8,0,5,1,9])

plt.hist(array, bins=20, align='mid', density=True) # density -> normalize

plt.title("Normalized histogram of created array")
plt.show()
###### HISTOGRAM BELOW ######
n,bins,patches = plt.hist(array,bins=20,align='mid',density=True) # same with 12th row
###### HISTOGRAM ABOVE ######
plt.plot(bins,norm.cdf(bins, np.mean(array), np.std(array)),linewidth=2,label="CDF",color="purple") 
plt.title("CDF of created array")
plt.show()

print("Mean of variable x: {}\n".format(np.mean(array)))