# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 15:06:31 2025

@author: micha
"""

import numpy as np
import math
import matplotlib.pyplot as plt
# from numpy.ma.core import array

# -------- Problem 1 -----------
A = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([8, 3, 5])
C = np.array([[1, 2], [3, 4], [5, 6]])

print("p1a:", A + C.T)
print("p1b:", 2*A)
print("p1c:", A@b)
print("p1d:", b.T @ A.T)
print("p1e:", A @ A.T)


# ----------- Problem 2 ------------
def truss(xc, yc):
    l1 = math.sqrt(xc**2 + yc**2)
    s1 = yc/l1; c1 = xc/l1
    l2 = math.sqrt((xc-1)**2 + yc**2)
    s2 = yc/l2; c2 = (xc - 1)/l2

    A = np.array([
        [c1, 1, 0, 1, 0, 0],
        [s1, 0, 0, 0, 1, 0],
        [0, -1, c2, 0, 0, 0],
        [0, 0, s2, 0, 0, 1],
        [-c1, 0, -c2, 0, 0, 0],
        [-s1, 0, -s2, 0, 0, 0],
    ])

    b = np.array([0, 0, 0, 0, 0, 1000])

    x = np.linalg.solve(A, b)
    return x

forces = truss(2, 1)
print("p2:")
print("FAC = ", forces[0])
print("FAB = ", forces[1])
print("FBC = ", forces[2])
print("RAx = ", forces[3])
print("RAy = ", forces[4])
print("RBy = ", forces[5])

n = 100
xvec = np.linspace(0, 3, n)
Fvec = np.zeros(n)
for i in range(n):
    Fvec[i] = truss(xvec[i], 1)[0]

plt.figure()
plt.plot(xvec, Fvec)
plt.xlabel("$x_c$")
plt.ylabel("$F_{AC}$ (lbs)")

# ------------ Problem 3 ------------------
m1 = 5; m2 = 3; m3 = 2
k1 = k3 = 100; k2 = 150
g = 9.81

A = np.array([
    [k1+k2, -k2, 0],
    [-k2, k2+k3, -k3],
    [0, -k3, k3],
])
b = g * np.array([m1, m2, m3])

print("p3:", np.linalg.solve(A, b))


# ------------ Problem 4 --------------
x = np.array([-2.0000, -1.7895, -1.5789, -1.3684, -1.1579, -0.9474, -0.7368, -0.5263, -0.3158, -0.1053, 0.1053, 0.3158, 0.5263, 0.7368, 0.9474, 1.1579, 1.3684, 1.5789, 1.7895, 2.0000])
y = np.array([7.7859, 5.9142, 5.3145, 5.4135, 1.9367, 2.1692, 0.9295, 1.8957, -0.4215, 0.8553, 1.7963, 3.0314, 4.4279, 4.1884, 4.0957, 6.5956, 8.2930, 13.9876, 13.5700, 17.7481])

A = np.column_stack((x**2, x, np.ones_like(x)))
coeff, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
print("p4 coeff", coeff)
xvec = np.linspace(x[0], x[-1], 100)
yvec = coeff[0]*xvec**2 + coeff[1]*xvec + coeff[2]

plt.figure()
plt.plot(x, y, ".")
plt.plot(xvec, yvec, "-")
plt.xlabel("x")
plt.ylabel("y")


plt.show()