# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 22:28:49 2025

@author: micha
"""

import numpy as np
import matplotlib.pyplot as plt

#Section 2.1 Problem 1
def prob2_1_1():
    x = np.arange(1,6,1) #Create x data set
    y = [2,1,4,3,7] #Create y data set
    z = np.vstack((x,y)) #Combine into one set
    
    r_matrix = np.corrcoef(z) #Get correlation coefficient matrix
    r = r_matrix[0,1] #Extract the coefficient
    print(r)
    
    
#Section 2.1 Problem 2
'''
a.) The y values were all multiplied by a constant, this doesn't change the r value
b.) The x values all undergo the same linear transformation (x=10x+3)
c.) The values are not in order but y is a multiple of x'''
    

#Section 2.1 Problem 6
def prob2_2_6():
    v = [1.54, 1.60, 0.95, 1.30, 2.92] #Velocity
    a = [7.64, 8.04, 8.04, 6.37, 3.25] #Acceleration
    
    r_matrix = np.corrcoef(v,a) 
    r = r_matrix[0,1] #Pull the correlation coefficient from the matrix
    
    plt.scatter(v, a) #Create a scatterplot of the date 
    plt.show()
    
    #Part C, the r value is reasonable, because there is a strong negative correlation
    
    #Part D, the r value would not change because it would only be multiplying by constants

#Section 2.2, Problem 3
def prob2_2_3():
    x = np.arange(0,80) #Create value of heights in inches
    y = -0.2967 + 0.2738*x #Relationship between forearm length (y) and height
    
    plt.plot(x,y) #Plot the results
    plt.xlabel('Height')
    plt.ylabel('Forearm Length')
    plt.grid()
    plt.show()
    
    #Part A, For a height of 70 the forearm length would be 18.8693
    #Part B, He would have to be 70.48 inches tall
    #Part C, You could not conclude this, though it would be statistically likely given the data
    
    
def prob2_2_6():
    syst = [134,115,113,123,119,118,130,116, #Systolic blood pressures
            133,112,107,110,108,105,157,154]
    dias = [87,83,77,77,69,88,76,70, #Diastolic blood pressures
            91,75,71,74,69,66,103,94]
    
    plt.scatter(syst,dias) #Scatter plot the results
    plt.xlabel('Systolic')
    plt.ylabel('Diastolic')
    plt.grid()
    plt.show()
    
    least_squares = np.polyfit(syst,dias,1) #Compute the least squares line
    
    #Part C
    y1 = least_squares[0]*115 + least_squares[1]
    y2 = least_squares[0]*125 + least_squares[1]
    print(y2-y1)
    
    #Part D
    print(y2)
    
prob2_2_6()