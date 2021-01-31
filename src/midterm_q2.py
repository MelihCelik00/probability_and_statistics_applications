#!/usr/bin/env python
# Name surname: Melih Safa Celik
# Student ID: 010180519
# Probability and Statistics Midterm
# Question 2

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

'''
where λ is the rate parameter of the distribution.
 In a single figure, show the PDFs of X with 100 samples where
- the rate parameter equals to the last digit of your student ID. 
- the rate parameter equals to the eighth digit of your student ID. 
'''

# Random exponential distribution with numpy
param1 = 9
param2 = 1

exp_dist_1 = np.random.exponential(scale=1/param1, size=100) # 100 rv [1,2,3,4,5,..,99,100]
exp_dist_2 = np.random.exponential(scale=1/param2, size=100) 

exp_dist_1 = np.sort(exp_dist_1) # sort distribution
exp_dist_2 = np.sort(exp_dist_2)

pdf_of_first = param1 * (math.e**(-param1*exp_dist_1))
pdf_of_second = param2 * (math.e**(-param2*exp_dist_2))

plt.plot(exp_dist_1,pdf_of_first, linewidth=4, label="pdf of first", color="red") # put only 1 parameter for showing variables on x-axis
plt.plot(exp_dist_2,pdf_of_second, linewidth=4, label="pdf of second", color="blue") # put only 1 parameter for showing variables on x-axis

plt.title("PDFs of first and second parameters") # TITLE AT
plt.legend()
plt.xlabel("Exponensial distribution values") # LABEL AT 
plt.ylabel("PDFs") # BU LABELI DA AT
plt.show() # GOSTER

######
cdf_of_first = 1-math.e**(-9*exp_dist_1)
cdf_of_second = 1-math.e**(-exp_dist_2)

plt.plot(exp_dist_1,cdf_of_first,linewidth=4, label="CDF of param1", color="red")
plt.plot(exp_dist_2,cdf_of_second,linewidth=4, label="CDF of param2", color="blue")
plt.title("CDFs of first and second parameters") # TITLE AT
plt.legend()
plt.xlabel("Exponensial distribution values") # LABEL AT 
plt.ylabel("CDFs")
plt.show()