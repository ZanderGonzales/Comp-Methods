# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 16:18:45 2025

@author: micha
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# ------------- Problem 1 -------------
m = 20.0
k = 20.0

"""
y = [x, xdot]
dx/dt = xdot
dxdot/dt = 1/m(-b*xdot - k*x)  
"""
def springmass(t, y, b):
    x, xdot = y
    dxdt = xdot
    dxdotdt = -1/m*(b*xdot + k*x)
    return [dxdt, dxdotdt]

tspan = [0, 15.0]
y0 = [1.0, 0.0]
sol1 = solve_ivp(springmass, tspan, y0, rtol=1e-12, atol=1e-12, args=(5,))
sol2 = solve_ivp(springmass, tspan, y0, rtol=1e-12, atol=1e-12, args=(40,))
sol3 = solve_ivp(springmass, tspan, y0, rtol=1e-12, atol=1e-12, args=(200,))

plt.figure()
plt.plot(sol1.t, sol1.y[0, :])
plt.plot(sol2.t, sol2.y[0, :])
plt.plot(sol3.t, sol3.y[0, :])
plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend(["b = 5", "b = 40", "b = 200"])


# -----------------  Problem 2 --------------------

def epidemic(t, y, i, r):
    S, I, R = y
    dSdt = -i*S*I
    dIdt = i*S*I - r*I
    dRdt = r*I
    return [dSdt, dIdt, dRdt]

i = 0.002/7
r = 0.15
tspan = (0.0, 60.0)
y0 = [10_000, 1.0, 0.0]
sol = solve_ivp(epidemic, tspan, y0, args=(i, r), rtol=1e-12, atol=1e-12)

plt.figure()
plt.plot(sol.t, sol.y[0, :])
plt.plot(sol.t, sol.y[1, :])
plt.plot(sol.t, sol.y[2, :])
plt.xlabel("t")
plt.ylabel("individuals")
plt.legend(["susceptible", "infected", "recovered"])

plt.figure()
plt.plot(sol.t, sol.y[0, :])
plt.plot(sol.t, sol.y[1, :])
plt.plot(sol.t, sol.y[2, :])
plt.plot([40, 60], [10, 10], "k--")
plt.xlabel("t")
plt.ylabel("individuals")
plt.legend(["susceptible", "infected", "recovered"])
plt.xlim([40, 60])
plt.ylim([0, 11])

def epidemic2(t, y, i, r, rho):
    S, I, R = y
    dSdt = -i*S*I + rho*R
    dIdt = i*S*I - r*I
    dRdt = r*I - rho*R
    return [dSdt, dIdt, dRdt]

i = 0.002/7
r = 0.15
rho = 0.03
tspan = (0.0, 60.0)
y0 = [10_000, 1.0, 0.0]
sol = solve_ivp(epidemic2, tspan, y0, args=(i, r, rho), rtol=1e-12, atol=1e-12)

plt.figure()
plt.plot(sol.t, sol.y[0, :])
plt.plot(sol.t, sol.y[1, :])
plt.plot(sol.t, sol.y[2, :])
plt.xlabel("t")
plt.ylabel("individuals")
plt.legend(["susceptible", "infected", "recovered"])


# ------------------------ Problem 3 --------------------------------

# manual
mean = (70*1 + 15*2 + 10*3 + 3*4 + 2*5) / 100
stdev = math.sqrt((70*(1 - mean)**2 + 15*(2 - mean)**2 + 10*(3 - mean)**2 + 3*(4 - mean)**2  + 2*(5 - mean)**2) / 99)

# using numpy
x = np.concatenate((np.ones(70), np.full(15, 2), np.full(10, 3), np.full(3, 4), np.full(2, 5)))
print("mean =", np.mean(x))
print("std =", np.std(x, ddof=1))
print("median =", np.median(x))
print("1st quartile =", np.percentile(x, 25))
print("3rd quartile =", np.percentile(x, 75))
print("proportion > mean =", sum(x > mean) / len(x))  # perhaps easier to do by hand in this case


plt.show()