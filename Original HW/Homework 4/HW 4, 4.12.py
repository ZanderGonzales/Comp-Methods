# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 13:48:27 2025

@author: micha
"""
#ALL OF THE DERIVATIVES OF THE POLYNOMIAL
def f(x):
    fx = 25*x**3 - 6*x**2 + 7*x -88
    return fx

def f_prime(x):
    fx = 75*x**2 - 12*x + 7
    return fx

def f_2prime(x):
    fx = 150*x - 12
    return fx

def f_3prime(x):
    fx = 150
    return fx

#ALL OF THE TAYLOR APPROXIMATIONS OF THE POYNOMIAL
x0 = 1
x_final = 3
h = x_final - x0

def taylor_0():
    fx = f(x0)
    return fx

def taylor_1():
    fx = taylor_0() + f_prime(x0) * h
    return fx

def taylor_2():
    fx = taylor_1() + f_2prime(x0) / 2  * h**2
    return fx

def taylor_3():
    fx = taylor_2() + (f_3prime(x0) / 6 * h**3)
    return fx

#TRUE PERCENT RELATIVE ERROR
def rel_error(approximate):
    true = f(x_final)
    return(((true-approximate)/true)*100)

print('True Percent Relative Error for Zero Order:', rel_error(taylor_0()),'%')
print('True Percent Relative Error for First Order:', rel_error(taylor_1()),'%')
print('True Percent Relative Error for Second Order:', rel_error(taylor_2()),'%')
print('True Percent Relative Error for Third Order:', rel_error(taylor_3()),'%')