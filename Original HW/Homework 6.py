# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:21:32 2025

@author: micha
"""

import numpy as np
import matplotlib.pyplot as plt

def function(x):
    '''Returns f(x) of a given input'''
    return x**3 -6*x**2 + 11*x - 6.1

def function_prime(x):
    '''Returns the derivative of f(x) of a given input'''
    return 3*x**2 - 12*x + 11

def plot():
    '''PLots a function to look at the highest positive root'''
    #Given Function
    x = np.arange(1.5,3.5,0.1) #Creates array for x axis
    y = function(x) #Calculates f(x) for each x value
    plt.plot(x,y)
    
    #x=0 Line
    y_1 = np.zeros(20)
    plt.plot(x, y_1, color = 'red')
    
    #Generate plot
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()
    
#plot()

def newton_raph(x0):
    '''Uses the Newton Raphson method to find the highest positive root, given an initial value'''
    xi = x0
    for iter in np.arange(0,4,1):
        xi = xi - (function(xi)/function_prime(xi))
        
    return xi
        
#print(newton_raph(3.5))

def builtin_roots():
    '''Uses numpys roots function to find all roots'''
    coeff = [1,-6,11,-6.1]
    print(np.roots(coeff))
    
builtin_roots()