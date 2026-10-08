# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:06:51 2025

@author: micha
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as scint
import scipy 

def func_22_1(t,y):
    return y * (t**2 - 1.1)

def analyt_22_1():
    '''Graphs the analytically solved ODE'''
    t = np.arange(0,2,0.01)
    y = np.e**( (t**3/3) -1.1* t )
    plt.plot(t, y, label="Analytical Euler's Method")
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.legend()
    plt.grid()
    plt.show()

def prob_22_1():
    #a.) Analytically solving gets y = e**( (t**3/3) -1.1t )
    #b.)
    t_span = [0,2]
    y0 = np.array([1])
    h1 = 0.5 #Changing h to a smaller number better approximates the analytical solution
    h2 = 0.25
    
    t = np.arange(0,2,0.01)
    y = np.e**( (t**3/3) -1.1* t )
    plt.plot(t, y, label="Analytical Euler's Method")
    
    sol = scint.solve_ivp(func_22_1, t_span, y0, t_eval = np.arange(0,2+ h1, h1))
    plt.plot(sol.t, sol.y[0], label="Numerical, h = 0.5")
    
    sol2 = scint.solve_ivp(func_22_1, t_span, y0, t_eval = np.arange(0,2+ h2, h2))
    plt.plot(sol2.t, sol2.y[0], label="Numerical, h = 0.25")
    
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.legend()
    plt.grid()
    plt.show()
    
prob_22_1()

def func22_2(x,y):
    return (1+2*x) * np.sqrt(y)

def analyt_22_2():
    '''Graphs the analytically solved ODE'''
    x = np.arange(0,1,0.01)
    y = np.exp(x**2) * ( (np.sqrt(np.pi) / 2) * scipy.special.erf(x) + 1 )
    plt.plot(x, y, label="Analytical Euler's Method")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.legend()
    plt.grid()
    plt.show()
    
def prob22_2():
    
    x = np.arange(0,1,0.01)
    y = np.exp(x**2) * ( (np.sqrt(np.pi) / 2) * scipy.special.erf(x) + 1 )
    plt.plot(x, y, color = 'purple', label="Analytical Euler's Method")
    
    t_span = [0,1]
    y0 = np.array([1])
    h1 = 0.25 #Changing h to a smaller number better approximates the analytical solution
    sol = scint.solve_ivp(func22_2, t_span, y0, t_eval = np.arange(0,1+ h1, h1))
    plt.plot(sol.t, sol.y[0], label="Numerical, h = 0.5")
    
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.legend()
    plt.grid()
    plt.show()
    
prob22_2()

    