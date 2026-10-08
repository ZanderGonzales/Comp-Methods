# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:00:37 2025

@author: micha
"""
import numpy as np
import matplotlib.pyplot as plt

def roundoff_error():
    n = 15
    approx = np.zeros(n+1)
    
    for i in range(n+1):
        approx[i] = round(np.pi, i)
        #error = ( (np.pi-estimate) / np.pi)* 100
    
    error_array = abs(np.pi - approx) / np.pi * 100
    
    #Plot
    plt.figure()
    plt.scatter(np.arange(0,16,1), error_array)
    plt.yscale('log')
    plt.xlabel('Digit rounded to')
    plt.ylabel('Relative percent error')

#roundoff_error()

def leibniz(N):
    pi_estimate = 0
    for k in range(N+1):
        pi_estimate += ((-1)**k) / (2*k +1)
    return 4 * pi_estimate
    
            
def truncation_error():
    N = 20
    approx_arr = np.zeros(N+1)
    
    for n in np.arange(0,N+1,1):
        approx_arr[n] = leibniz(n)
        
    error = abs(np.pi - approx_arr) / np.pi *100
    
    #Plot
    plt.figure()
    plt.scatter(np.arange(0,21,1), error, color = 'purple')
    plt.xlabel('Terms in approximation')
    plt.ylabel('Relative percent error')
    
#truncation_error()
