#!/usr/bin/env python
# author: Melih Safa Celik
# Student ID: 010180519

# Insert libraries for calculation
from numpy import random, mean, std, sort, meshgrid, dstack, linspace
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits .mplot3d import Axes3D
from scipy.stats import norm, multivariate_normal

mean = [0,1] # It's given on pdf
covariance_matrix = [[1,0.9],[0.9,2]]

x_rv,y_rv = random.multivariate_normal(mean,covariance_matrix,1000).T # rvs for covariance matrix values

# Sort
x_rv = sort(x_rv)
y_rv = sort(y_rv)

# Plot PDF of Samples
pdf_of_x = norm.pdf(x_rv,x_rv.mean(),x_rv.std())
pdf_of_y = norm.pdf(y_rv,y_rv.mean(),y_rv.std())

plt.plot(x_rv,pdf_of_x,label="PDF of X")
plt.plot(y_rv,pdf_of_y,label="PDF of y")

plt.title("PDF of the samples")
plt.xlabel("Random variables")
plt.ylabel("Density")
plt.legend()
plt.show()

# Plot CDF of Samples
cdf_of_x = norm.cdf(x_rv,x_rv.mean(),x_rv.std())
cdf_of_y = norm.cdf(y_rv,y_rv.mean(),y_rv.std())

plt.plot(x_rv,cdf_of_x,label="CDF of X")
plt.plot(y_rv,cdf_of_y,label="CDF of Y")

plt.title("CDF of the samples")
plt.xlabel("Random variables")
plt.ylabel("Density")
plt.legend()
plt.show()

# Plot 3d surface of PDF of X and Y vars.

X_3d,Y_3d = meshgrid(x_rv,y_rv)
p = dstack((X_3d,Y_3d))

rvar = multivariate_normal(mean, covariance_matrix)
Z_3d = rvar.pdf(p)

fig = plt.figure(figsize=(20,15), dpi=80, edgecolor='k')
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(X_3d,Y_3d,Z_3d, cmap=cm.jet)

ax.set_xlabel("X Axis")
ax.set_xlim([x_rv.min(),x_rv.max()])
ax.set_ylabel("Y Axis")
ax.set_ylim([y_rv.min(),y_rv.max()])
ax.set_zlabel("Z Axis")

fig.colorbar(surface, extend="both")

plt.show()

# Plot 3d surface of CDF of X and Y vars.

X_3d,Y_3d = meshgrid(x_rv,y_rv)
p = dstack((X_3d,Y_3d))

rvar = multivariate_normal(mean, covariance_matrix)
Z_3d = rvar.cdf(p)

fig = plt.figure(figsize=(20,15), dpi=80, edgecolor='k')
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(X_3d,Y_3d,Z_3d, cmap=cm.jet)

ax.set_xlabel("X Axis")
ax.set_xlim([x_rv.min(),x_rv.max()])
ax.set_ylabel("Y Axis")
ax.set_ylim([y_rv.min(),y_rv.max()])
ax.set_zlabel("Z Axis")

fig.colorbar(surface, extend="both")

plt.show()

# Calculate sample mean and standard deviation of X and Y
mean_of_x = x_rv.mean()
mean_of_y = y_rv.mean()
std_of_x = x_rv.std()
std_of_y = std(y_rv)

print("Mean of variable x: {}\nMean of variable y: {}\nStandard deviation of x: {}\nStandard deviation of y: {}".format(format(mean_of_x,".3f"),
                                                                                                                        format(mean_of_y,".3f"),
                                                                                                                        format(std_of_x,".3f"),
                                                                                                                        format(std_of_y,".3f")))
# Scatter Plot
plt.title("Scatter Plot")
x_rv,y_rv = random.multivariate_normal(mean,covariance_matrix,100).T

samples = linspace(0,y_rv.size+1,y_rv.size)

plt.scatter(samples, x_rv, s=75)
plt.scatter(samples, y_rv, s=75)

plt.xlabel("x values")
plt.ylabel("Y values")

plt.show()

plt.title("Scatter Plot")

plt.xlabel("x values")
plt.ylabel("Y values")

plt.scatter(x_rv,y_rv,s=75)
plt.show()
