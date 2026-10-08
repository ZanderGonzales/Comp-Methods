# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 16:10:00 2025

@author: micha
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import math


# ------------- Problem 1 -------------
def fun(t, y):
    return y*t**2 - 1.1*y

def euler(ode, tspan, y0, h):
    t = np.arange(tspan[0], tspan[1]+1e-6, h) # define time vector (added a little to ending point because of numerical precision)
    npts = len(t)  # number of time points
    y = np.zeros(npts)  # initialize y array
    y[0] = y0[0]  # set initial condition
    for i in range(npts-1):  # iterate through time
        y[i+1] = y[i] + h * ode(t[i], y[i])

    return t, y

tspan = (0, 2.0)
y0 = [1.0]

# euler
t1, y1 = euler(fun, tspan, y0, 0.5)
t2, y2 = euler(fun, tspan, y0, 0.1)
t3, y3 = euler(fun, tspan, y0, 0.01)

# rk45
sol1 = solve_ivp(fun, tspan, y0)
sol2 = solve_ivp(fun, tspan, y0, atol=1e-12, rtol=1e-12)

plt.figure()
plt.plot(t1, y1)
plt.plot(t2, y2)
plt.plot(t3, y3)
plt.plot(sol1.t, sol1.y[0, :])
plt.plot(sol2.t, sol2.y[0, :])
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend(["Euler (h = 0.5)", "Euler (h = 0.1)", "Euler (h = 0.01)", "RK45 (default)", "RK45 (tighter tol)"])


# -------------------- Problem 2 ----------------------------------

def vander(t, z, mu):
    x, xdot = z
    dxdt = xdot
    d2xdt2 = mu*(1 - x**2)*xdot - x
    return [dxdt, d2xdt2]

tspan = (0.0, 10)
z0 = [1, 2]

mu = 2.0
sol = solve_ivp(vander, tspan, z0, args=(mu,), atol=1e-12, rtol=1e-12)

plt.figure()
plt.plot(sol.t, sol.y[0, :])
plt.xlabel("t")
plt.ylabel("z(t)")


# --------------- Problem 3 ------------------

def bounce(t, z):
    f = 0.0007
    b = 0.01
    k = 200.0
    m = 0.0027
    g = 9.81

    x, xdot, y, ydot = z

    dxdt = xdot
    dxdotdt = -f/m*xdot*math.sqrt(xdot**2 + ydot**2)
    dydt = ydot
    dydotdt = -f/m*ydot*math.sqrt(xdot**2 + ydot**2) - g

    if y <= 0:
        dydotdt += -b/m*ydot -k/m*y

    return [dxdt, dxdotdt, dydt, dydotdt]

tspan = (0, 3.0)
x0 = 0.0
xdot0 = 4.0
y0 = 0.2
ydot0 = 0.0
z0 = [x0, xdot0, y0, ydot0]
sol = solve_ivp(bounce, tspan, z0, atol=1e-12, rtol=1e-12)

plt.figure()
plt.plot(sol.y[0, :], sol.y[2, :])
plt.xlim([0, 1])
plt.xlabel("x")
plt.ylabel("y")

plt.show()
