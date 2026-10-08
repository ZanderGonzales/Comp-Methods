# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 00:11:00 2025

@author: micha
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy

def q9_2():
    x_1 = np.arange(0,6,0.1)
    
    x_2_eq = (4*x_1 + 24) / 8
    x_2_eq_2 = (-x_1 + 34) / 6
    
    plt.plot(x_1,x_2_eq, color = 'red', label = 'Equation 1')
    plt.plot(x_1, x_2_eq_2, color = 'blue', label = 'Equation 2')
    plt.xlabel('$X_1$')
    plt.ylabel('$X_2$')
    plt.legend()
    plt.grid()
    plt.show()
    
#q9_2()

def q9_5():
    x_1 = np.arange(7,13,0.1)
    
    x_2_eq = (0.5*x_1 + 9.5)
    x_2_eq_2 = (1.02*x_1 + 18.8) / 2
    
    #PART A
    plt.plot(x_1,x_2_eq, color = 'red', label = 'Equation 1')
    plt.plot(x_1, x_2_eq_2, color = 'blue', label = 'Equation 2')
    plt.xlabel('$X_1$')
    plt.ylabel('$X_2$')
    plt.legend()
    plt.grid()
    plt.show()
    
    #PART B
    A = np.array([ [0.5,-1], [1.02,-2] ])
    print('Determinant:', np.linalg.det(A))
    
    #PART C
    #It looks like it is ill-conditioned
    
    #PART D
    #Did by hand, x1 = 10, x2 = 14.5
    
    #PART E
    #It changes the numbers, but not by much so you can see that it is ill-conditioned
    
#q9_5()

def q11_1():
    A = np.array([ [10,2,-1],
                   [-3,-6,2],
                   [1,1,5] ])
    
    B = np.array([ [27], [-61.5], [-21.5] ])
    
    inverse = np.linalg.inv(A)
    print(inverse)
    print(np.dot(A,inverse))
    
    #The inverse times the original is close to the Identity matrix
    

q11_1()

def q11_10():
    n = 10
    H = scipy.linalg.hilbert(n)
    
    spec_norm = np.linalg.norm(H,2)
    cond_num = np.linalg.cond(H,2)
    print('Spectral Condition Number:', cond_num)
    
    b = np.sum(H, 1) #Create a vector that has each element as the sum of the coefficients in that row
    
    x = np.linalg.solve(H,b)
    expected_x = np.ones(n)
    
    error = np.linalg.norm(x - expected_x) / np.linalg.norm(x)
    print('Error:', error)
    expected_error = cond_num * np.finfo(float).eps
    print('Expected error:', expected_error)
    
#q11_10()