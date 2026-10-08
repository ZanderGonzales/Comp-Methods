# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:22:56 2025

@author: micha
"""
import numpy as np


'''Unit vectors for each bar, formatted in ( [x],[y] )'''
F = 1000
ax = 0
ay = 0
bx = 1
by = 0
cx = 2
cy = 1

uac = np.array([  ((cx-ax) / np.sqrt((cy-ay)**2 + (cx-ax)**2))  , ((cy-ay) / np.sqrt((cy-ay)**2 + (cx-ax)**2)) ])
ubc = np.array([ ((cx-bx) / np.sqrt((cy-by)**2 + (cx-bx)**2))  , ((cy-by) / np.sqrt((cy-by)**2 + (cx-bx)**2)) ]) 
uab = np.array([ 1, 0 ])

'''Coefficients: Fac, Fab, Fbc, Ax, Ay, By'''
coefficients = np.array([
                        [-uac[0], 0, -ubc[0], 0, 0, 0], #Node C, horizontal
                        [-uac[1], 0, -ubc[1], 0, 0, 0], #Node C, vertical
                        [0, -uab[0], ubc[0], 0, 0, 0], #Node B, horizontal
                        [0, uab[1], ubc[1], 0, 0, 1], #Node B, vertical
                        [uac[0], uab[0], 0, 1, 0, 0], #Node A, horizontal
                        [uac[1], uab[1], 0, 0, 1, 0] #Node A, vertical
                                               ])
b = np.array([ [0], [F], [0], [0], [0], [0] ])

cond = np.linalg.cond(coefficients, p = 'fro')

solution = np.linalg.solve(coefficients, b=b)
print(solution)
print('Condition Number:', cond)
