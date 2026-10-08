# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:20:00 2025

@author: micha
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy

time = np.array([ 0,0.52,1.04,1.75,2.37,3.25,3.83 ]) #Time in seconds
dist = np.array([ 153,185,208,249,261,271,273 ]) #Distance in meters

def q21_12():
    vel = np.gradient(dist, time)
    acc = np.gradient(vel, time)
    print(vel, acc)
    
    plt.plot(time, dist, color = 'red', label = 'Distance')
    plt.plot(time, vel, color = 'blue', label = 'Velocity')
    plt.plot(time, acc, color = 'green', label = 'Acceleration')
    plt.xlabel('$Time (s)$')
    plt.ylabel('Dependent Variable')
    plt.legend()
    plt.grid()
    plt.show()



E = 200000000000 #Pa
I = 0.0003 #m^4
wx = 250000 #N/m
L = 3 #m
dx = np.arange(0,3.125,0.125)

def slope_func(x):
    answer = wx/(120*E*I*L) * (-5 * x**4 + 6 * L**2 * x**2 - L**4)
    return answer
    

slope = slope_func(dx)
print('Slope:', slope)
plt.plot(dx, slope, color = 'red')
plt.xlabel('Distance')
plt.ylabel('Slope')
plt.grid()
plt.show()

y = scipy.integrate.cumulative_trapezoid(slope,dx,initial = 0) #Deflection in m
print('y:', y)
plt.plot(dx, y, color = 'blue')
plt.xlabel('Distance')
plt.ylabel('Deflection')
plt.grid()
plt.show()


M = ( np.gradient(slope,dx) ) * (E*I)
def M_manual(x):
    slope_deriv = wx/(120*E*I*L) * (-20 * x**3 + 12 * L**2 * x)
    return ( slope_deriv * (E*I) )
print('M:', M)
plt.plot(dx, M, color = 'green', label = 'Numerical')
plt.plot(dx, M_manual(dx), color = 'red', label = 'Analytical')
plt.xlabel('Distance')
plt.ylabel('Moment')
plt.legend()
plt.grid()
plt.show()


V = np.gradient(M,dx)
def V_manual(x):
    answer = wx/(120*E*I*L) * (-60 * x**2 + 12 * L**2) * (E*I)
    return answer
print('V:', V)
plt.plot(dx, V, color = 'purple', label = 'Numerical')
plt.plot(dx, V_manual(dx), color = 'yellow', label = 'Analytical')
plt.xlabel('Distance')
plt.ylabel('Shear')
plt.legend()
plt.grid()
plt.show()


