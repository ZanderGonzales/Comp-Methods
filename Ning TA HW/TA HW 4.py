# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 16:35:18 2025

@author: micha
"""

import numpy as np
from scipy.optimize import root_scalar, approx_fprime
import math
import matplotlib.pyplot as plt

# ---- goat grazing ------

def area_difference(r, npts=200):

    x = np.linspace(0, math.sqrt(r**2 - r**4/4), npts)
    y = np.sqrt(r**2 - x**2) + np.sqrt(1 - x**2) - 1

    area = 2*np.trapz(y, x)
    return area - math.pi * 1**2 / 2


sol = root_scalar(area_difference, args=(200), bracket=[0.4, 1.4])
print("goat radius = ", sol.root)

# ------ finite differencing

testfunc = lambda x: math.exp(x) * math.sin(x)
x = 1.5

exact = math.exp(x) * math.cos(x) + math.sin(x) * math.exp(x)
f0 = testfunc(x)

def finite_diff_error(step):
    fd = (testfunc(x + step) - f0) / step
    print("pct error for step size", step, "=", abs(fd - exact)/exact*100)

finite_diff_error(1e-1)
finite_diff_error(1e-6)
finite_diff_error(1e-11)
finite_diff_error(1e-16)


# -------- my trapezoidal integration -----

def mytrapz(y, x):
    n = len(x)
    integral = 0.0
    for i in range(n - 1):
        integral += (x[i+1] - x[i]) * 0.5*(y[i] + y[i+1])
    return integral

vec_testfunc = np.vectorize(testfunc)
x = np.linspace(0, 1.0, 50)
print("trapz 50 pts = ", mytrapz(vec_testfunc(x), x))
x = np.linspace(0, 1.0, 100)
print("trapz 100 pts = ", mytrapz(vec_testfunc(x), x))
x = np.linspace(0, 1.0, 200)
print("trapz 200 pts = ", mytrapz(vec_testfunc(x), x))

# ----------- vehicle -----
time = np.array([0.0, 0.24489796, 0.44897959, 0.65306122, 0.85714286, 1.06122449, 1.26530612, 1.46938776, 1.67346939, 1.87755102, 2.08163265, 2.28571429, 2.48979592, 2.69387755, 2.89795918, 3.10204082, 3.30612245, 3.51020408, 3.71428571, 3.91836735, 4.12244898, 4.32653061, 4.53061224, 4.73469388, 4.93877551, 5.14285714, 5.34693878, 5.55102041, 5.75510204, 5.95918367, 6.16326531, 6.36734694, 6.57142857, 6.7755102 , 6.97959184, 7.18367347, 7.3877551 , 7.59183673, 7.79591837, 8.])
position = np.array([0.16326531, 0.97959184, 1.79591837, 2.6122449,  3.42857143, 4.24489796, 5.06122449, 5.87755102, 6.69387755, 7.51020408, 8.32653061, 9.14285714, 9.95918367, 10.7755102, 11.59183673, 12.40816327, 13.2244898, 14.04081633, 14.85714286, 15.67346939, 16.46730529, 17.14618909, 17.70012495, 18.12911287, 18.43315285, 18.6122449, 18.666389, 18.59558517, 18.3998334, 18.07913369, 17.63348605, 17.06289046, 16.36734694, 15.54685548, 14.60141608, 13.53102874, 12.33569346, 11.01541025, 9.57017909, 8.])

velocity = np.gradient(position, time)

# or manually:
# note that this reduces vector size by 1
# velocity = (position[1:] - position[:-1]) / (time[1:] - time[:-1])
# time_vel = time[:-1]

plt.figure()
plt.plot(time, position)
plt.plot(time, velocity)
plt.legend(["position (m)", "velocity (m/s)"])
plt.xlabel("time (s)")
plt.show()

