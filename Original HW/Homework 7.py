# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:44:46 2025

@author: micha
"""
import numpy as np
def problem_8_2():   
    A = np.array([ [4,7],[1,2],[5,6] ])
    B = np.array([ [4,3,7],[1,2,7],[2,0,4] ])
    C = np.array([ [3],[6],[1] ])
    D = np.array([ [9,4,3,-6],[2,-1,7,5] ])
    E = np.array([ [1,5,8],[7,2,3],[4,0,6] ])
    F = np.array([ [3,0,1],[1,7,3] ])
    G = np.array([ [7,6,4] ])
    
    #a.) A- 3x2 B- 3x3 C- 3x1 D- 2x4 E- 3x3 F- 2x3 G- 1x3
    #b.) Square: B,E ; Column: C ; Row: G
    #c.) A[1,2] = NA ; B[2,3] = NA ; D[3,2] = NA ; E[2,2] = 6
         # F[1,2] = 3 ; G[1,2] = NA
    #d.) 
    
    print('E+B:\n', E+B)
    #print('A+F:\n', A+F) This is not possible since they are not the same shapes
    print('B-E:\n', B-E)
    print('E+B:\n', E+B)
    print('7*B:\n', 7*B)
    print('C^T:\n', C.T)
    print('E*B:\n', E@B)
    print('B*A:\n', B@A)
    print('D^T:\n', D.T)
    #print('A*C:\n', A@C) This is not possible because they aren't compatible 
    print('I*B:\n', np.eye(3)@B)
    print('E^T*E:\n', E.T * E)
    print('C^T*C:\n', C.T * C)

def problem_8_3():
    coefficient = np.array([[0,7,-5],
                            [0,4,7],
                            [-4,3,-7]])
    answers = np.array([ [-50], [-30], [40] ])
    print('x1,x2,x3 =\n', np.linalg.solve(coefficient,answers))
    print('Transpose:\n', coefficient.T)
    print('Inverse:\n', np.linalg.inv(coefficient))
    
#%%
def problem_8_10():
    '''
    Coeffiecients = F1, F2, F3, V2, V3, H2
    '''
    
    coefficients = np.array([ 
                              [np.sin(np.deg2rad(30)), 0, np.sin(np.deg2rad(60)), 0, 0, 0], #Node 1, Vertical
                              [np.cos(np.deg2rad(30)), 0, -np.cos(np.deg2rad(60)), 0, 0, 0], #Node 1, Horizontal
                              [-np.sin(np.deg2rad(30)), 0, 0, 1, 0, 0], #Node 2, Vertical
                              [-np.cos(np.deg2rad(30)), 1, 0, 0, 0, 1], #Node 2, Horizontal
                              [0, 0, -np.sin(np.deg2rad(60)), 0, 1, 0], #Node 3, Vertical
                              [0, -1, np.cos(np.deg2rad(60)), 0, 0, 0] #Node 3, Horizontal
                                                                        ])
    answers = np.array([ [1000],[0],[0],[0],[0],[0] ])
    print('F1, F2, F3, V2, V3, H2\n', np.linalg.solve(coefficients,answers))
    
problem_8_10()
    