# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 13:30:36 2025

@author: micha
"""

import numpy as np

#Create data set
dataset1 = np.zeros(70) + 1
dataset2 = np.zeros(15) + 2
dataset3 = np.zeros(10) + 3
dataset4 = np.zeros(3) + 4
dataset5 = np.zeros(2) + 5

dataset = np.hstack((dataset1, dataset2, dataset3, dataset4, dataset5))

#Part A, calculate mean
mean = np.mean(dataset)
print('Mean:', mean)

#Part B, calculate standard deviation
sd = np.std(dataset)
print('Stardard deviation:', sd)

#Part C, calculate median
med = np.median(dataset)
print('Median:', med)

#Part D, calculate third and fourth quartiles
q1 = np.percentile(dataset, 25)
q3 = np.percentile(dataset, 75)
print('First quartile', q1)
print('Third quartile', q3)