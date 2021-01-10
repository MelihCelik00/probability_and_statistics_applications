#!/usr/bin/env python
# author: Melih Safa Celik
# Student ID: 010180519

import re
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, t
import random

# First create variables for cdf as a list by using boundaries. First x, than y
x_list = np.linspace(0,2,1000) # From 0 to 2 with step size 0.05
y_list = np.linspace(9,13,1000)
# Let's define pdf and cdf of x by using the given function at homework pdf
# find pdf of x
pdf_of_x = 5/32 * x_list**4

# find cdf of x
cdf_of_x = (x_list**5)/32

# Let's define pdf and cdf of y by using the calculated function
# find pdf of y
pdf_of_y = 5/64 * ((y_list-9)**(3/2))

# find cdf of y
cdf_of_y = (np.sqrt(y_list-9)**(5))/32

# mean values for x and y
meanOf_x = np.mean(cdf_of_x)
meanOf_y = np.mean(cdf_of_y)


'''
plt.xlim([0, 200])
plt.ylim([0, 1.2])
plt.yticks(np.arange(0, 1.2, 0.2))
plt.xticks(np.arange(0, 500, 100))
'''
plt.plot(meanOf_x, "ro", label = "Mean of x", color="purple")
plt.plot(meanOf_y, "ro", label = "Mean of y", color="green")
plt.plot(x_list,cdf_of_x, label="CDF of x", color="blue") # put only 1 parameter for showing variables on x-axis
plt.plot(y_list,cdf_of_y, label="CDF of y", color="red") # put only 1 parameter for showing variables on x-axis
plt.title("CDF of x and y")
plt.show()


