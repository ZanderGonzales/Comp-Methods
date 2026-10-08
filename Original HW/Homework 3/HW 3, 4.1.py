# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:28:43 2025

@author: micha
"""

x = 9
true_val = x**0.5

def approximate_root(x,stop = 1e-4, max_it = 50):
  #Instantiate variables
    fx_old = 1 #Last solution
    iter = 1 #Iteration number
    APRE = 100 #Approximate percent relative error (%)
    
    while True: #Continues until boundary conditions are met
        fx = (fx_old + (x/fx_old))/2 #Calculate an approximate answer using the last approximation
        
        APRE = abs((fx-fx_old)/fx)*100 #Calculate error based on current and previous answer
        
        fx_old = fx
        iter += 1
        
        if iter >= max_it or APRE < stop: #Boundary conditions
            break
    return fx #Return the most recent answer

current_guess = approximate_root(x, stop = 1e-4, max_it = 50)
print(current_guess)