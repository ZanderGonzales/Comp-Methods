# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:22:24 2025

@author: micha
"""

import scipy.integrate as scint
import matplotlib.pyplot as plt

#Define constants
k = 20 #N/m
m = 20 #kg
x0 = 1 #m
v0 = 0 #m/s

c1 = 5 #Underdamped
c2 = 40 #Critically damped
c3 = 200 #Overdamped
c_values = [c1,c2,c3]

#Define conditions given
t_span = [0,15]
init_conds = [x0, v0] #Initial displacement and velocity

def damped_spring(t,y):
    #Split y into the first two variables
    x1 = y[0] #Displacement
    x2 = y[1] #Velocity
    
    #Split up into two first order equations, with equations for the second two variables
    x1prime = x2 
    x2prime = (-c/m)*x2 - (k/m)*x1
    return x1prime, x2prime

#Solve for each different damping value
for c in c_values:
    sol = scint.solve_ivp(damped_spring, t_span, init_conds)
    plt.plot(sol.t,sol.y[0],label = f'c = {c}' ) #Plot each line, labeled by the c value
    
    
#Plot Results
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('Damped Spring-Mass System')
plt.legend()
plt.grid()
plt.show()
    


