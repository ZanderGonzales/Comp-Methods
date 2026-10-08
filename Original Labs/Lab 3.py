# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 16:05:09 2026

@author: micha
"""

import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt

def func(x):
    y= x - np.e**-x
    return y
    
def dfunc(x):
    y = 1 + np.e**-x 
    return y

def newton_raph(x0, f, df):
    '''Uses the Newton Raphson method to find the root, 
    given an initial value, a function, and the derivative of that function'''
    xi = x0
    iter = 0
    
    while True:
        xi_last = xi
        xi = xi_last - ( f(xi_last) / df(xi_last) )
        
        iter += 1
        
        #print(iter, xi) #uncomment to print each iteration number as it progresses
        
        if abs(f(xi)) <= 10**-6 or iter >= 1000:
            break
    
    return xi, iter
        
print( 'Final' ,newton_raph(0, func, dfunc ))

def newton_raph_sec(x0, f, df, dx):
    '''Uses the Newton Raphson method to find the root, using a secant approximation for
    the derivative, given an initial value, and a function'''
    xi = x0
    iter = 0
    
    while True:
        xi_last = xi
        xi = xi_last - ( f(xi_last) * dx / (f(xi_last + dx) - f(xi_last)) )
        
        iter += 1
        
        #print(iter, xi) #uncomment to print each iteration number as it progresses
        
        if abs(f(xi)) <= 10**-6 or iter >= 1000:
            break
    
    return xi, iter

print( 'Final' ,newton_raph_sec(0, func, dfunc, 10**-6))

def brentq_func(f, bottom, top):
    '''Uses the scipy brentq function to find the root of the passed in function, using 
    a bracketing method with a passed in bottom and top bracket values'''
    root = brentq(f, bottom, top, full_output = True)
    return(root)
    
print(brentq_func(func, 0, 1))

def find_poly_roots():
    zero = [3] #y= 3
    first = [2,3] #y= 2x +3
    second = [4,2,3] #y= 4x^2 + 2x + 3
    third = [5,4,2,3] #y= 5x^3 4x^2 + 2x + 3
    fourth = [6,5,4,2,-3] #y= 6x^4 5x^3 4x^2 + 2x - 3
    
    print(np.roots(zero))
    print(np.roots(first))
    print(np.roots(second))
    print(np.roots(third))
    print(np.roots(fourth))
    
def graphs(f):
    fourth = [6,5,4,2,-3] #y= 6x^4 5x^3 4x^2 + 2x - 3
    x = np.arange(-2,2.1,0.1)
    y = 6*x**4 + 5*x**3 + 4*x**2 + 2*x - 3
    
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('$6x^4 + 5x^3 + 4x^2 + 2x - 3$')
    plt.grid()
    plt.show()
    
    x_1 = np.arange(0,1,0.01)
    plt.plot(x_1,f(x_1))
    plt.xlabel('x')
    plt.ylabel('$x-e^{-x}$')
    #plt.yscale('log')
    plt.grid()
    plt.show()
    
graphs(func)
