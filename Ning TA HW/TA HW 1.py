# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 16:02:15 2025

@author: micha
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def patriot():
    # I don't expect people to code this part this way
    # but probably they will  do it manually like
    # brep = 2**-4 + 2**-5 + 2**-8 ....
    dec2 = ".00011001100110011001100"
    brep = 0.0
    for i in range(1, len(dec2)):
        brep += float(dec2[i])*2**(-i)
    # --------------------------------------------
    error = 0.1 - brep
    number_of_events = 10 * 60 * 60 * 100
    total_error = error * number_of_events
    distance = 1670 * total_error

    return distance


def atmosphere():
    npts = 200
    h = np.linspace(0.0, 47, npts)
    T = np.zeros(npts)
    for i in range(npts):
        if h[i] <= 11.0:
            T[i] = 288.15 - 6.5*h[i]
        elif h[i] <= 20.0:
            T[i] = 216.65
        elif h[i] <= 32.0:
            T[i] = 216.65 + (h[i] - 20)
        elif h[i] <= 47.0:
            T[i] = 228.65 + 2.8*(h[i] - 32)

    plt.figure()
    plt.plot(T, h)
    plt.xlabel("temperature (K)")
    plt.ylabel("altitude (km)")
    plt.show()


def polar2cart(r, theta):
    x = r * math.cos(theta*math.pi/180)
    y = r * math.sin(theta*math.pi/180)
    return x, y

def polar2cart_np(r, theta):
    x = r * np.cos(theta*math.pi/180)
    y = r * np.sin(theta*math.pi/180)
    return x, y

def cart2polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)*180/math.pi
    return r, theta

def cart2polar_np(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)*180/math.pi
    return r, theta

def avg(x):
    return np.sum(x) / len(x)

def mavg(x, c=1):
    return c * avg(x)

def wavg(x, w):
    return np.sum(x * w) / np.sum(w)

def tavg(filename):
    try:
        data = np.loadtxt(filename)
        nr, nc = data.shape
        return np.sum(data, axis=0)/nr

    except FileNotFoundError:
        print("file not found")
        return np.array([0.0, 0.0])

def favg(x, f):
    return avg(f(x))


if __name__ == '__main__':
    atmosphere()
    
