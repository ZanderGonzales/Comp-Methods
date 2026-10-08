# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 16:22:50 2025

@author: micha
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy

#Define constants
m= 0.0027 #Mass, kg
bair = 0.001 #Drag coefficient, Ns/m
bball = 0.01 #Damping coefficient, Ns/m
kball = 50.0 #Spring constant, N/m
g = 9.81 #Gravity, m/s^2

#Define perameters
init_cond = np.array([ 0, 0.7, 0.7, 0]) #[x, vx, y, vy]
init_cond2 = np.array([ 0, 0.5, 0.7, 0]) #[x, vx, y, vy]
t_span = [0,4] #seconds
xtotal = 1 #m

def ode(t, init_cond):
    x = init_cond[0] #Displacement in x-direction
    vx = init_cond[1] #Velocity in x-direction
    y = init_cond[2] #Displacement in y-direction
    vy = init_cond[3] #Velocity in y-direction
    
    #Velocity in x-direction
    xdot = vx
   
    #Acceleration in x- direction. Works whether it's in the air or on the table
    vxdot = -bair / m * vx 
   
    #Velocity in y-direction
    ydot = vy
    
    #Acceleration in y-direction, changes whether in air or on table
    if y > 0:
        vydot = -g -( bair / m * vy )
    elif y <= 0:
        vydot = -g -(bair / m *vy) -(bball / m *vy) -(kball / m * y)
    
    #Return first and second derivatives for each direction of movement
    solution = [xdot, vxdot, ydot, vydot]
    return solution

#Solve ODEs
sol1 = scipy.integrate.solve_ivp(ode, t_span, init_cond, t_eval = np.arange(0,4,0.01))
x1_1 = sol1.y[0] #x-values
x2_1 = sol1.y[2] #y-values

sol2 = scipy.integrate.solve_ivp(ode, t_span, init_cond2, t_eval = np.arange(0,4,0.01))
x1_2 = sol2.y[0] #x-values
x2_2 = sol2.y[2] #y-values

#Plot the results, using a for loop for an animation effect
def animation(x1,x2):
    for i in range(len(x1)):
        plt.title('Animated bouncing')
        plt.plot(x1[0:i], x2[0:i])
        plt.plot(x1[i], x2[i], 'ro', markersize=10)
        plt.xlim([0, 1])
        plt.ylim([-0.05, 0.7])
        plt.xlabel('Distance in x-direction (m)')
        plt.ylabel('Distance in y-direction (m)')
        plt.pause(0.01) 
        
#Plot the results as a single plot
def graph(x1,x2, label):
    plt.plot(x1, x2, label = label)
    plt.legend()
    plt.xlim([0, 1])
    plt.ylim([-0.05, 0.7])
    plt.xlabel('Distance in x-direction (m)')
    plt.ylabel('Distance in y-direction (m)')

graph(x1_2,x2_2,'Number 1')
graph(x1_1,x2_1,'Number ')
animation(x1_1,x2_1)