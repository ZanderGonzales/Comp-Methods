# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 12:51:12 2025

@author: micha
"""

import numpy as np
import pylab as plt


def rocket_velocity(t):
        '''Calculates velocity using a piecewise function'''
        if 0<=t<=8:
            v = 10 * t**2 - 5*t
        elif 8<=t<=16:
            v = 624 -3*t
        elif 16<=t<=26:
            v = 36*t + 12 * (t - 16)**2
        elif t > 26:
            v = 2136 * np.e**(-0.1*(t-26))
        else:
            v = 0
        return v
t_range = np.arange(-5,51)

def calculate_velocity(t):
    '''Creates a list with all of the velocities for a given number of times'''
    y = []
    for n in t :
        y_value = rocket_velocity(n)
        y.append(y_value)
    return y
    
plt.plot(t_range,calculate_velocity(t_range))
plt.xlabel('Time')
plt.ylabel('Velocity')


