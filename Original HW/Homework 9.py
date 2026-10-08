# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:06:54 2025

@author: micha
"""
import numpy as np
import scipy
#19.2

a = 3.02 #analytically
b = 1.96 #single trapezoidal
c = 2.711 #composite trapezoidal
d = 2.96 #simpsons 1/3
e = 3.013 #composite simpsons 1/3

def rel_error(true,test):
    error = (true - test) / true *100
    print(error)
    
def q19_2_error():
    rel_error(a,b)
    rel_error(a,c)
    rel_error(a,d)
    rel_error(a,e)
    
    
#19.8
vel = ([ 5,6,5.5,7,8.5,8,6,7,7,5 ])
time = ([1,2,3,4.5,6,7,8,9,10])
def q19_8(t,v):
    n = len(time)
    approx = 0
    
    for k in range(0,n-1):
        approx = approx + (t[k+1]-t[k])*(v[k+1]+v[k])/2
        
    print('Integral with trapezoidal rule', approx)
    print('Average velocity', np.average(vel))
    
#q19_8(time,vel)

#19.25

height = [ 0,50,100,150,225,300,375,450,600 ]
force_dens = [ 0,30,40,40,50,50,60,80,100 ]
def q19_25(f,z):
    
    total_force = np.trapezoid(f,z)
    
    forces = []
    for k in range(len(z)):
        force = f[k] * z[k]
        forces.append(force)
        
    total_moment = np.trapezoid(forces,z)
    distance = total_moment / total_force
        
    print('Total Force:', total_force, 'kN',
          '\nTotal Moment:', total_moment, 'kN-m',
          '\nDistance force is applied:', distance, 'm')
    

q19_25(force_dens,height)
    