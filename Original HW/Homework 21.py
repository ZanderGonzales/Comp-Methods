# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 12:46:48 2025

@author: micha
"""
import numpy as np
import scipy.stats as scistats

#Weights of each bag of candy
candy_weights = [15.87, 16.02, 15.78, 15.83, 15.69, 15.81, 16.04, 15.81, 15.92, 16.10]

#Number of candy bags weighed
n = len(candy_weights)

#Mean and standard deviation of the sample
candy_mean = sum(candy_weights) / n
s = np.std(candy_weights, ddof = 1)

print('Tested mean of candy weights:', candy_mean)

#Given mean of the population
h0_mean = 16

#Calculate t statistic of the sample mean in the population
t = (candy_mean - h0_mean) / (s / np.sqrt(n))

#Calculate the p value of the t-statistic
p = scistats.t.cdf(t, df = n-1)


#State the results of the different variations of the values
print('\nTest statistic for the mean weight being less than 16:', t)

print('\nP-value of the mean being less than 16:', p)

print('P-value of the mean being more than 16:', 1-p)

print('P-value of the mean being different than 16:', 2*p)

