# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:14:23 2025

@author: micha
"""

import numpy as np

def iterations(dx0, error):
    '''Use an equation to find how many iterations are needed to get within the error range give'''
    return round(np.log2(dx0/error))

def bungee_eq(c):
    '''The basic equation of a falling bungee jumper rearranged for the coefficient of drag'''
    m = 95 #Mass (kg)
    g = 9.81 #Gravity (m/s^2)
    t = 9 #Time (s)
    v = 46 #Velocity (m/s)
    
    return np.sqrt((g*m)/c) * np.tanh(np.sqrt((g*c)/m)*t) - v

def bisection_method(x0h, x0l, error):
    '''
    Uses bisection to find the root of a given equation, given an initial range and error range
    x0h = initial upper end guess
    x0l = initial lower end guess
    error = error desired for the root
    '''
    pres_root = np.mean([x0h, x0l])
    x_h = x0h #Upper limit is instantiated
    x_l = x0l #Lower limit is instantiated
    n = 0 #Number of iterations instantiated at 0
    
    for i in range(iterations(x0h-x0l, error)): #Takes the number of iterations from the other function
        n += 1
        if bungee_eq(x_l)*bungee_eq(pres_root) < 0: #If the function changes signs in the lower range
            x_h = pres_root #Take the midpoint and make it the new upper point
            pres_root = np.mean([x_l, x_h]) #Take a new midpoint between the new upper and old lower point
        elif bungee_eq(x_h)*bungee_eq(pres_root) < 0: #If the function changes signs in the lower range
            x_l = pres_root #Take the midpoint and make it the new lower point
            pres_root = np.mean([x_l, x_h])  #Take a new midpoint between the new lower and old upper point
            
    print(pres_root, n) #After the given number of iterations, give the approximation of the root


bisection_method(x0h = 0.5, x0l = 0.2, error = 1*10**-7) #Run the bisection method with given upper
                                                         #and lower limit, as well error value
                                                         
            
        
    