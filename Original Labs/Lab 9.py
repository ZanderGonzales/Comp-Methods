# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 16:04:04 2025

@author: micha
"""

import scipy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def step_1():
    crit1 = scipy.stats.norm.ppf(0.60)
    print(crit1)
    
    crit2 = scipy.stats.t.ppf(0.60, 24)
    print(crit2)
    
    crit3 = scipy.stats.norm.ppf(0.975)
    print(crit3)
    
    crit4 = scipy.stats.t.ppf((1-.01/2 ), 9)
    print('crit 4:', crit4)

def step_2():
    df = pd.read_csv('osteoporosis.csv')
    osteo = df['Osteoporosis']
    proportion = (np.sum(osteo) / len(osteo))
    z = scipy.stats.norm.ppf(0.995)
    
    n2 = len(osteo) + 4
    p2 = float ( (np.sum(osteo)+2) / n2)
    CI1 = p2 - z * np.sqrt( (p2 * (1-p2)) / n2)
    CI2 = p2 + z * np.sqrt( (p2 * (1-p2)) / n2)
    print('Confidence Interval of 99%: [',CI1, ',', CI2,']')
 

def step_3():
    tensile = [34.5, 35.3, 33.8, 35.8, 37.0, 37.5, 35.6, 34.4, 33.2, 38.0]
    
    #Check if the data is roughly normal in distribution by plooting a boxplot
    plt.figure()
    plt.boxplot(tensile)
    plt.ylabel('Tensile Strength (ksi)')
    
    #Find values for calculating confidence interval of 95%
    tens_mean = np.mean(tensile)
    t_tens = scipy.stats.t.ppf(0.975, 9)
    stan_d_tens = np.std(tensile, ddof = 1)
    n_tens = 10
    
    print('Average tensile strength:', tens_mean)
    
    CI1_t = tens_mean - ( t_tens * stan_d_tens / np.sqrt(n_tens))
    CI2_t = tens_mean + ( t_tens * stan_d_tens / np.sqrt(n_tens))
    print('Confidence Interval of 95%: [',CI1_t, ',', CI2_t,']')

def step_4():
    #Split sample into values for t test and z test
    n = np.arange(2,1000,1)
    n_t = np.arange(2,31,1)
    n_norm = np.arange(31,1000,1)
    
    #Knowns given
    mean_4 = 45
    s_4 = 3.5
    
    #Find z score for sample over 30
    z_4 = scipy.stats.norm.ppf(0.975)
    
    widths = np.zeros(len(n))
    for i in n:
        if i in n_t:
            t_4 = scipy.stats.t.ppf(0.975, i-1)
            CI1 = mean_4 - ( t_4 * s_4 / np.sqrt(i) )
            CI2 = mean_4 + ( t_4 * s_4 / np.sqrt(i) )
        elif i in n_norm:
            CI1 = mean_4 - ( z_4 * s_4 / np.sqrt(i) )
            CI2 = mean_4 + ( z_4 * s_4 / np.sqrt(i) )
        widths[i-2] = CI2 - CI1
        
    plt.scatter(n,widths)
    plt.xlabel('Number of samples')
    plt.ylabel('Width of a 95% confidence interval')
    plt.yscale('log') 
            



