# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 13:11:06 2025

@author: micha
"""
import scipy.stats as scistats
import numpy as np

def prob_10():
    #Statistics about women with tests suggesting coronary artery disease
    nx = 110 #Sample size
    mu_x = 169.9 #mmHg, mean peak systolic blood pressure
    s_x = 24.8 #mmHg, sample standard deviation
    
    #Statistics about women with tests suggesting no coronary artery disease
    ny = 225 #Sample size
    mu_y = 163.3 #mmHg, mean peak systolic blood pressure
    s_y = 25.8 #mmHg, sample standard deviation
    
    #Calculate the z scores for a 95% confidence interval
    z = scistats.norm.ppf(0.05 / 2)
    
    #Calculate the confidence interval
    CI_1 = (mu_x - mu_y) - z* np.sqrt( (s_x**2 / nx) + (s_y**2 / ny))
    CI_2 = (mu_x - mu_y) + z* np.sqrt( (s_x**2 / nx) + (s_y**2 / ny))
    CI = [CI_1, CI_2]
    print(CI)

def prob_12():
    #Statistics about males drinking energy drinks
    nm = 413
    mu_m = 2.49
    s_m = 4.87
    
    #Statistics about females drinking energy drinks
    nf = 382
    mu_f = 1.22
    s_f = 3.24
    
    #Calculate the z score that the mean for males is greater than females
    diff = 0
    z = (mu_m - mu_f - diff) / np.sqrt((s_m**2 / nm) + (s_f**2 / nf))
    
    #Calculate the p value that the mean value for males is higher than females (1-tail test)
    p_val = scistats.norm.cdf(1-z)
    print('Probability that the mean value for males is not higher than females:', p_val)

def prob_2():
    #Statistics about Walsburg Road
    nh_w = 13 #Heavy vehicles
    n_w = 67 + 2 #Total vehicles
    
    p_w = (nh_w + 1) / (n_w)
    
    #Statistics about North 52nd Street
    nh_52 = 32 #Heavy vehicles
    n_52 = 91 #Total vehicles
    
    p_52 = (nh_52 + 1) / (n_52)
    
    #Z score for a 90% confidence interval
    z = scistats.norm.ppf(0.1 / 2)
    
    #Critical Value
    cv = z * np.sqrt( (p_w * (1-p_w) / n_w) + (p_52 * (1-p_52) / n_52) )
    
    #Confidence Interval
    CI = [p_w-p_52 - cv, p_w-p_52 + cv]
    print(CI)
    
def prob_14():
    #Statistics about Route 7 and North Shrewsbury
    ran_7 = 21
    n_7 = 154 
    
    p_7 = (ran_7 ) / n_7
    
    #Statistics about Route 62 and Paine Turnpike
    ran_62 = 20
    n_62 = 183
    
    p_62 = (ran_62 ) / n_62
    
    #Pooled proportion
    p = (ran_7 + ran_62) / (n_7 + n_62)
    
    #Calculate z score that the proportion is the same
    z = (p_7 - p_62) / np.sqrt( p*(1-p)*( (1/n_7) + (1/n_62) ) )
    
    #Calculate the p value that the proportions are the same
    p_val = scistats.norm.ppf(z)
    print(p_val)