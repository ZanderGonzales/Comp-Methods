# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:46:59 2025

@author: micha
"""

import scipy.integrate as scint
import matplotlib.pyplot as plt

def infect_model_a(t, y):
    #Define Constants
    a = 0.002 / 7  #People / day infected
    r = 0.15  #People / day recovered
    
    #Create equations
    S, I, R = y
    dS = -a * S * I
    dI = (a * S * I) - (r * I)
    dR = r * I
    
    return dS, dI, dR

def infect_model_b(t,y):
    #Define Constants
    a = 0.002 / 7  #People / day infected
    r = 0.15  #People / day recovered
    p = 0.03 #People / day suseptible again
    
    #Create equations
    S, I, R = y
    dS = (-a * S * I) + (p * R) #Adds the return rate as opposed to model A
    dI = ((a * S * I) - (r * I)) 
    dR = (r * I) - (p * R) #Subtracts the return rate as opposed to model A
    
    return dS, dI, dR
    
def solve_model_a():
    #Define Perameters
    init_cond = [10000, 1, 0] #Suseptible, Infected, Recovered (S,I,R)
    t_span = [0,50]
    
    #Solve using solve_ivp
    sol = scint.solve_ivp(infect_model_a, t_span, init_cond)
    
    #Plot results
    plt.plot(sol.t,sol.y[0],label = 'Suseptible' )
    plt.plot(sol.t,sol.y[1],label = 'Infected' )
    plt.plot(sol.t,sol.y[2],label = 'Recovered' )
    
    #Plot line at 10 people, looking for where the Infected line goes below
    plt.axhline(y=10, color="gray", linestyle="--", label="10 person threshold")
    
    plt.xlabel('Time (days)')
    plt.ylabel('People')
    plt.title('Epidemic Model A')
    plt.legend()
    plt.grid()
    plt.show()
    
def solve_model_b():
    #Define Perameters
    init_cond = [10000, 1, 0] #Suseptible, Infected, Recovered (S,I,R)
    t_span = [0,100]
    
    #Solve using solve_ivp
    sol = scint.solve_ivp(infect_model_b, t_span, init_cond)
    
    #Plot results
    plt.plot(sol.t,sol.y[0],label = 'Suseptible' )
    plt.plot(sol.t,sol.y[1],label = 'Infected' )
    plt.plot(sol.t,sol.y[2],label = 'Recovered' )
    
    #Plot line at 10 people, looking for where the Infected line goes below
    plt.axhline(y=10, color="gray", linestyle="--", label="10 person threshold")
    
    plt.xlabel('Time (days)')
    plt.ylabel('People')
    plt.title('Epidemic Model B')
    plt.legend()
    plt.grid()
    plt.show()
    
solve_model_a()
solve_model_b()

