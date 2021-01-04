#!/usr/bin/env python
# author: Melih Safa Celik
# Student ID: 010180519

# Insert libraries for calculation
from numpy import random,linspace
import matplotlib.pyplot as plt
from scipy.stats import norm  # use stats.norm

# Last digit of your student ID is your mean, and the 8th digit of your 
# student ID is your standard deviation. If your deviation = 0, take deviation = 1.
mean = 9 # mu
standard_deviation = 1

# 1.1 Create Normally (Gaussian) Distributed 50 r.v. X 
# with a mean mu and standart deviation sigma

x = random.normal(loc=mean, scale=standard_deviation,size=50)

# Create normally distributed 5000 samples (Y) 
# with mean and standard deviation

y = random.normal(loc=mean, scale=standard_deviation,size=5000)

# Plot what I have know
plt.plot()
plt.plot(x,'ro',color="red")
plt.title(" 50 samples of X")
plt.show()


plt.plot(y,'ro',color="green")
plt.title("5000 samples of Y")
plt.show()

#Mix them

plt.plot(y,'ro',color="green")
plt.plot(x,'ro',color="red")
plt.title(" 50 samples of X and 5000 samples of Y")
plt.show()

# Plot the histogram of random variables X and Y. 
# Do not forget to normalize the histogram

plt.hist(x,bins=100,align='mid',density=True) # normed/density True for normalizing
plt.hist(y,bins=100,align='mid',density=True)
plt.ylabel("density") # write vertical 'density'
plt.title("Normalized Histogram") 
plt.show()

# Pdf over Y

#import matplotlib.mlab as mlab # import matlab for pdf calculation

fig,ax = plt.subplots() # start

n,bins,patches = plt.hist(y,bins=100,density=1,alpha=0.75) # hist
t = norm.pdf(bins, mean, standard_deviation) # pdf

ax.plot(bins,t,linewidth=2, label="PDF", color="red") # plot pdf

ax.set_ylabel("PDF of Y",color="red",fontsize=14) 

ax2=ax.twinx()
ax2.plot(bins,norm.cdf(bins, mean, standard_deviation),linewidth=2,label="CDF",color="purple") # cdf of Y

ax2.set_ylabel("CDF of Y",color="purple",fontsize=14)

plt.title("Pdf and CDF over Y") 
plt.legend()
plt.grid()
plt.show()


fig,ax = plt.subplots() # start 

n,bins,patches = plt.hist(x,bins=15,density=1,alpha=0.75) # hist 

t = norm.pdf(bins, mean, standard_deviation) # pdf

plt.plot(bins,t,linewidth=3, label="PDF",color="red") # plot pdf

plt.plot(bins,norm.cdf(bins, mean, standard_deviation),linewidth=2,label="CDF",color="purple") # plot cdf of X

plt.title("Pdf and CDF over X")  # general title
plt.legend() # plot legend
plt.grid()
plt.show()

###### Last Question

mean_x = x.mean()
stdeviation_x = x.std()

mean_y = y.mean()
stdeviation_y = y.std()


print("Mean of variable x: {}\nMean of variable y: {}\nStandard deviation of x: {}\nStandard deviation of y: {}".format(mean_x,mean_y,stdeviation_x,stdeviation_y))