# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:59:44 2025

@author: micha
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy


data = np.loadtxt('Original Labs/rocking_baby.csv', delimiter=',', unpack=True,skiprows=1)

t = data[0]
x_accel = data[1]
y_accel = data[2]
z_accel = data[3]
tot_accel = data[4]

def acc_plots():
    '''Shows plots for a baby rocking in three different axes'''
    fig, ax = plt.subplots(3,1, figsize=(8,6))
    
    ax[0].plot(t, x_accel)
    ax[0].set_ylabel('Acceleration x ($m/s^2$)')
     
    ax[1].plot(t,y_accel)
    ax[1].set_ylabel('Acceleration y ($m/s^2$)')
    
    ax[2].plot(t,z_accel)
    ax[2].set_ylabel('Acceleration z ($m/s^2$)')
    ax[2].set_xlabel('Time (s)')
    
    plt.tight_layout()
    plt.show()
    

def z_plots():
    '''Numerically finds velocity and position of the child in the z axis, and then graphs 
    that along with acceleration'''

    fig, ax = plt.subplots(3,1, figsize=(8,6))
    ax[2].set_xlabel('Time (s)')
    
    ax[2].plot(t,z_accel)
    ax[2].set_ylabel('Acceleration z ($m/s^2$)')
    
    
    v = scipy.integrate.cumulative_trapezoid(z_accel,t,initial = 0)
    ax[1].plot(t,v)
    ax[1].set_ylabel('Velocity z (m/s)')
    
    
    x = scipy.integrate.cumulative_trapezoid(v,t,initial = 0)
    ax[0].plot(t,x)
    ax[0].set_ylabel('Displacement z (m)')

    plt.show()

acc_plots()
z_plots()



