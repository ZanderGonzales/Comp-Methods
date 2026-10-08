# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 13:30:10 2025

@author: micha
"""
import numpy as np

x = 2
h = 0.25

def f(a):
    fx = 25*a**3 - 6*a**2 + 7*a -88
    return fx

def f_prime(b):
    fx = 75*b**2 - 12*b + 7
    return fx

def for_diff_approx():
    fx = ( f(x+h) - f(x) )/ h
    return fx

def back_diff_approx():
    fx = ( f(x) - f(x-h) )/ h
    return fx

def cent_diff_approx():
    fx = ( f(x+h) - f(x-h) )/ (2*h)
    return fx

#TRUE PERCENT RELATIVE ERROR
def rel_error(approximate):
    true = f_prime(x)
    return np.abs(((true-approximate)/true)*100)

print('True Percent Relative Error for Forward Approximation:', rel_error(for_diff_approx()),'%')
print('True Percent Relative Error for Backward Approximation:', rel_error(back_diff_approx()),'%')
print('True Percent Relative Error for Center Approximation:', rel_error(cent_diff_approx()),'%')