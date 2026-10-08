# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 16:02:14 2025

@author: micha
"""

import numpy as np
from scipy.integrate import quad
from math import sqrt
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import t

#---------- P1 ---------

x = np.array([1, 2, 3, 4, 5])
p = np.array([0.4, 0.25, 0.2, 0.1, 0.05])

mu = np.sum(x*p)
sigma2 = np.sum((x - mu)**2*p)
print("p1 mu =", mu)
print("p1 var =", sigma2)

#---------- P2 ---------
# this one could easily be done by hand,
# but I'm going to do it in Python for generality with harder distributions

pdf = lambda x: (x - 80)/800

prob, _ = quad(pdf, 80, 90)
mu, _ = quad(lambda x: x*pdf(x), 80, 120)
var, _ = quad(lambda x: (x - mu)**2*pdf(x), 80, 120)

print("2a:", prob)
print("2b:", mu)
print("2c:", sqrt(var))

#---------- P3 ---------
n = 123
xbar = 136.9
s = 22.6
se = s/sqrt(n)

print("3a:", norm.interval(.95, xbar, se))

zsigma = 139.9 - xbar
z = zsigma / se
pleft = norm.cdf(z)
pside = 1 - pleft
pmiddle = 1 - 2*pside
print("3b:", pmiddle)

# z s/sqrt(n) = 3
z = norm.ppf(.95+0.025)
n = (z * s / 3)**2
print("3c:", n)

z = norm.ppf(0.98)
print("3d:", xbar - z*se)

#---------- P4 ---------
x = [87.0, 86.0, 86.5, 88.0, 85.3]
n = 5
df = 4
xbar = np.mean(x)
se = np.std(x, ddof=1) / sqrt(n)
ci = t.interval(0.99, 4, xbar, se)
print("4:", ci)

#---------- P5 ---------

data = np.loadtxt("knee.csv", skiprows=1)

plt.figure()
plt.hist(data, 20)
plt.xlabel("knee height (mm)")
plt.ylabel("frequency")

plt.figure(2)
plt.hist(data, 20, density=True)
plt.xlabel("knee height (mm)")
plt.ylabel("probability")

plt.figure()
plt.hist(data, 20, density=True, cumulative=True)
plt.xlabel("knee height (mm)")
plt.ylabel("cumulative probability")

#---------- P6 ---------

mu = np.mean(data)
sigma = np.std(data)
x = np.linspace(np.min(data), np.max(data))
y = norm.pdf(x, mu, sigma)

plt.figure(2)
plt.plot(x, y)
plt.legend(["data", "Gaussian fit"])

plt.show()