# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 12:55:41 2025

@author: micha
"""
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

#Probelm 24.1, given values
x0 = 0 #m
xf = 10 #m
T0 = 240 #K
Tf = 150 #K

#Part A, Analytically Solving
'''Graphs the analytic solution to the given BVP'''
def analytic(x):
    T = 3.01 * np.e**(0.3873*x) + 236.99 * np.e**(-0.3873*x)
    return T

x = np.arange(x0,xf + 0.01, 0.01)

#Plot the results
plt.plot(x, analytic(x), label = 'Analytic', color = 'red')
plt.xlabel('Distance (m)')
plt.ylabel('Temperature (K)')
plt.title('Steady State Energy Balance Rod')
plt.grid()

#-------------------------------------------------------------------------------------#

#Part B, Shooting Method
'''Uses the shooting method to solve the given BVP'''

#Define Initial Conditions
guess1 = -90
guess2 = -95 
x_span = [x0 , xf]
init_cond1 = (T0, guess1) #Initial temperature and first derivative
init_cond2 = (T0, guess2)
init_cond = (T0,-90.61494308491416 )

def bar_temp(x,y):
    #Split y into the first two variables
    z1 = y[0] #Temperature
    z2 = y[1] #First derivative of temperature
    
    #Split up into two first order equations, with equations for the second two variables
    z1prime = z2
    z2prime = 0.15 * z1
    
    return z1prime, z2prime #Returns first and second derivative of temperature

#Solve the problem using both guesses
sol1 = integrate.solve_ivp(bar_temp, x_span, y0 = init_cond1)
sol2 = integrate.solve_ivp(bar_temp, x_span, y0 = init_cond2)

#Get a final condition using both guesses
Tf1 = sol1.y[0, -1]
Tf2 = sol2.y[0, -1]

#Average the guesses together to get the correct initial slope
dT = guess1 + ( (guess2 - guess1) / (Tf2 - Tf1) ) * (Tf - Tf1)

#Set up once more, with the correct ititial conditions
init_cond = (T0, dT)
sol = integrate.solve_ivp(bar_temp, x_span, y0 = init_cond)

#Plot the results
plt.plot(sol.t, sol.y[0], label = 'Shooting Method', linestyle = '--', color = 'purple')

#--------------------------------------------------------------------------------------#

#Part C, Finite Difference
'''Use the finite difference method to solve the given BVP'''

#Define the matrices for the given BVP
A = np.array([ [2.15,-1,0,0,0,0,0,0,0],
               [-1,2.15,-1,0,0,0,0,0,0],
               [0,-1,2.15,-1,0,0,0,0,0],
               [0,0,-1,2.15,-1,0,0,0,0],
               [0,0,0,-1,2.15,-1,0,0,0],
               [0,0,0,0,-1,2.15,-1,0,0],
               [0,0,0,0,0,-1,2.15,-1,0],
               [0,0,0,0,0,0,-1,2.15,-1],
               [0,0,0,0,0,0,0,-1,2.15] ])

b = np.array([ [240],[0],[0],[0],[0],[0],[0],[0],[150] ])

#Solve
sols = np.linalg.solve(A,b)

#Set up the x values associated with the solutions
x_finite = np.arange(1,10,1)

#Plot the results
plt.plot(x_finite,sols, label = 'Finite Difference', color = 'green')
plt.legend()
plt.show()