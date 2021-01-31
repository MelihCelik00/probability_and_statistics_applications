#!/usr/bin/env python
# Name surname: Melih Safa Celik
# Student ID: 010180519
# Probability and Statistics Midterm 31.01.2021
# Question 2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm,gamma

a1 = 9
a2 = 1
gamma1 = np.random.gamma(1,scale=a1, size=50)
gamma2 = np.random.gamma(1,scale=a2, size=50)

gamma1 = np.sort(gamma1) # sort distribution
gamma2 = np.sort(gamma2)


plt.plot(gamma1,gamma.pdf(gamma1,a1))
plt.plot(gamma2,gamma.pdf(gamma2,a2))

plt.show()


plt.plot(gamma1,gamma.cdf(gamma1,a1),linewidth=4, label="CDF of param1", color="red")
plt.plot(gamma2,gamma.cdf(gamma2,a2),linewidth=4, label="CDF of param2", color="blue")
plt.title("CDFs")
plt.xlabel("Gamma Distribution R.V.")
plt.ylabel("CDFs")

plt.show()
