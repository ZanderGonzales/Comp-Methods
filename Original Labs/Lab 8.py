# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 15:08:15 2025

@author: micha
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

#Import data for knee height
df = pd.read_csv('kneeheightmidpatella.csv')
data = np.reshape(df, -1)

#Plot all data for knee height on a histogram
plt.hist(df)
plt.xlabel('Knee hight (mm)')
plt.ylabel('Number of people')

#Plot a cumulative distribution
plt.figure()
plt.hist(df, bins = 100, density=True, cumulative=True)
plt.xlabel('Knee height (mm)')
plt.ylabel('Proportion of people at or under knee height')

#Plot a probability distribution
plt.figure()
plt.hist(df, bins = 30, density=True, label = 'Probability Distribution')
plt.xlabel('Knee height (mm)')
plt.ylabel('Proportion of people')

#Plot a normal distribution

#Create an x data range, and find key values
x = np.arange(np.min(data), np.max(data), 1)
mean = np.mean(df)  
standdev = np.std(df,axis=0)
variance = np.var(data, axis = 0)

#Use scipy to create a normal distribution
plt.figure()
y = scipy.stats.norm.pdf(x, mean, standdev)
plt.plot(x,y, label='Probability Density Function')
plt.legend(fontsize = 9)

#Take m samples from the population
m = 100
means = []
#Calculate the mean for each sample, collect them in a list
for i in np.arange(0,m+1,1):
    n = 10
    sample = np.random.choice(data, n)
    samp_mean = np.mean(sample)
    means.append(samp_mean)
    
#Plot the distibution of the means collected
plt.hist(means, bins= 10, density= True, label = 'Mean Distribution')
plt.ylabel('Proportion of samples')
plt.legend()

pop_mean = np.mean(means)
pop_variance = np.var(means)

print('Mean of population vs sample means:', mean, pop_mean)
print('Variance of population vs sample means:', variance / n, pop_variance)