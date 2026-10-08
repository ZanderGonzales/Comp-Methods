# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:18:04 2025

@author: micha
"""

import numpy as np
import math
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid, quad


# --------- problem 1 --------------

def shock(beta, theta, Mach):
    num = Mach**2 * math.sin(beta)**2 - 1
    den = Mach**2 * (1.4 + math.cos(2*beta)) + 2
    return 2/math.tan(beta)*num/den - math.tan(theta)

theta = 15*math.pi/180
Mach = 2.0
bmin = math.asin(1/Mach)
bmax = 64*math.pi/180
sol = root_scalar(shock, args=(theta, Mach), bracket=[bmin, bmax])
print("----- problem 1 -------")
print("shock angle (deg) =", sol.root*180/math.pi)


# --------- problem 2 -------

def newton(f, fp, x, tol):

    deltax = 2*tol  # just some arbitrary value to make sure we enter the loop
    iter = 0  # keep track of iterations
    while abs(deltax) > tol:
        deltax = f(x)/fp(x)
        x -= deltax
        iter += 1
    return x, iter


f = lambda x: x**3 - 3*x**2 + x - 1
fp = lambda x: 3*x**2 - 6*x + 1
tol = 1e-6
xguess = 2
sol, iter = newton(f, fp, xguess, tol)

print("--- problem 2 ---")
print("root =", sol)
print("number of iterations", iter)


# -------- problem 3 ------------
# lift distribution function
liftdist = lambda x: 4*np.sqrt(1 - 4*x**2)

# trapezoidal integral
npts = [10, 20, 40, 80, 160, 320]
n = len(npts)
I1 = np.zeros(n)
for i in range(n):
    x = np.linspace(-0.5, 0.5, npts[i])
    I1[i] = np.trapz(liftdist(x), x)

# Gaussian quadrature
I2, err = quad(liftdist, -0.5, 0.5)

plt.figure()
plt.plot(npts, I1, "-o")
plt.plot([10, 320], [I2, I2], "--")
plt.xlabel("number of points")
plt.ylabel("integral")
plt.legend(["trapezoidal", "Gauss quad"])

# -------- problem 4 ------------


time, accel = np.loadtxt("accel.dat", unpack=True)
vel = cumulative_trapezoid(accel, time, initial=0)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, vel)
plt.ylabel("velocity (m/s)")

plt.subplot(2, 1, 2)
plt.plot(time, accel)
plt.xlabel("time (s)")
plt.ylabel("acceleration (m/s^2)")
plt.show()