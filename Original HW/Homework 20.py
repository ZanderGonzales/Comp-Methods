# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 22:21:47 2025

@author: micha
"""
import numpy as np
import scipy.stats as scistats

def prob6_1_1():
    #List knowns given
    pop_mean = 5.4
    samp_mean = 4.5
    samp_n = 80
    samp_std = 2.7
    
    #Compute z score
    z = (samp_mean - pop_mean) / ( samp_std / np.sqrt(samp_n) )
    p_value = scistats.norm.cdf(z)
    
    #Draw conclusions from p-value
    print('Probabililty of getting such an extreme value assuming the null hypothesis:', p_value)
    print('Either the mean number of sick days has declined since the introduction '
          'of telecommuting, or the sample is in the most extreme 0.14% of its distribution.')

def prob6_1_6():
    #List knowns given
    pop_mean = 15
    samp_mean = 15.2
    samp_std = 1.8
    samp_n = 87
    
    #Compute two tailed z score
    z = (samp_mean - pop_mean) / ( samp_std / np.sqrt(samp_n) )
    p_value = scistats.norm.sf(z) * 2
    
    print('P-value:', p_value)
    print('The mean is still likely to be 15, with a 30% chance of it')
    




