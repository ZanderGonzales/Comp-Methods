# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:00:39 2025

@author: micha
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import root_scalar

# ----- problem 1 --------

def f(n):
    value = n/10
    for i in range(n):
        value -= 0.1
    return abs(value)


nvec = [10, 100, 1000, 10000, 100000, 1000000]
nn = len(nvec)
fz = np.zeros(nn)
for i in range(nn):
    fz[i] = f(nvec[i])

plt.figure()
plt.loglog(nvec, fz, "-o")
plt.xlabel("n, number of terms")
plt.ylabel("f(n), ideally should be zero")


# ----- problem 2 --------

nterms = np.arange(0, 21, 1)
n = len(nterms)
piest = np.zeros(n)
for i in range(n):
    for k in range(nterms[i]):
        piest[i] += 4 * (-1)**k / (2*k + 1)

plt.figure()
plt.plot(nterms, abs(piest - np.pi)/np.pi*100, "-o")
plt.xlabel("k, number of terms")
plt.ylabel("percent error")


# -------- Problem 3 ------------

def bisection(f, a, b, tol=1e-6):
    """
    Find a root of function f (i.e., f(x) = 0) within bracket [a, b] using bisection.

    Parameters
    ----------
    f : function
        the function that we are finding a root for: f(x) = 0
    a : float
        left endpoint
    b : float
        right endpoint. note f(a) * f (b) must be < 0, otherwise function will return.
    tol : float
        tolerance for stopping criteria

    Returns
    -------
    x : float
        the root where f(x) = 0
    """

    # check if this is a valid interval.  if not return
    if f(a)*f(b) > 0:
        raise ValueError("invalid interval")

    # start while loop, continue while the bracket half-width is > tolerance
    m = a  # initialize to something
    while (b - a)/2 > tol:

        # compute midpoint
        m = (a + b)/2

        # evaluate function at midpoint
        fm = f(m)

        # check if midpoint is a root (within tolerance), if so return it
        if abs(fm) < tol:
            return m

        # update new bracket based on sign of f(midpoint)
        if fm*f(a) < 0:
            b = m
        else:
            a = m

    # done with while loop, return midpoint as the root
    return m


def projectile(V, sx, sy):

    g = 9.81

    # ------ scipy ------
    residual = lambda theta : sx*math.tan(theta) - sy - g/2*sx**2/(V*math.cos(theta))**2
    sol = root_scalar(residual, bracket=[0.0, 1.0])

    # ----- bisection -----
    myroot = bisection(residual, 0.0, 1.0, tol=1e-6)

    return sol.root, myroot

scipy_root, my_root = projectile(100, 400, 50)
print("scipy root (deg) = ", scipy_root*180/math.pi)
print("my root (deg) = ", my_root*180/math.pi)



plt.show()