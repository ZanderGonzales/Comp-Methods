# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:01:22 2025

@author: micha
"""
import math
import numpy as np

#STEP 1
A3 = np.array([[3,4,5],[4,5,6]])

A2 = np.array([[1,2,3,4],[4,3,2,1],[0,9,8,7]])

A1 = np.array([2.0, 3, 4, 5])

def step1_a():
    print('Add constant:', A1 + 4)

def step1_b():
    print('Multiply constant:', A1 * 4)

def step1_c():
    print('Multiply by itself:', A1 * A1)
    #print(A1**2) does the same

def step1_d():
    print('Add two arrays:\n', A1 + A2)
    #print(A1 + A3) doeos not work

def step1_e():  
    print('Multiply two arrays:\n', A1 * A2)
    #print(A2 * A3) does not work

#step1_a(), step1_b(), step1_c(), step1_d(), step1_e()

#STEP 2

def step2_method1():
    '''Start with empty arrays, and then append each value for both x and y'''
    x = np.array([])
    y = np.array([])
    
    for i in np.arange(0,10.01,0.01):
        x = np.append(x,i)
        y = np.append(y,np.sin(i))
    print('Method 1:\n', x,y)

def step2_method2():
    '''Create the x array directly and add each y value one by one'''
    x = np.arange(0,10.01,0.01)
    y = ([])
    for i in x:
        y = np.append(y,np.sin(i))
    print('Method 2:\n', x,y)
    
def step2_method3():
    '''Create the x array directly and change the entire array to make the y array directly'''
    x = np.arange(0,10.01,0.01)
    y = np.sin(x)
    print('Method 3:\n', x, y)
        
#step2_method1(), step2_method2(), step2_method3()

#STEP 3
#I can call functions from the console or have them called from the script

#STEP 4

def step4_1(array = A1):
    total = sum(array)
    length = len(array)
    average = total / length
    print('1:', average)
    
def step4_2(array = A1, C = 2):
    total = sum(array)
    length = len(array)
    average = total / length
    average = average * C
    print('2:', average)
    
def step4_3():
    row_1, row_2 = np.loadtxt('Lab_1.txt')
    
    total_1 = sum(row_1)
    length_1 = len(row_1)
    average_1 = total_1 / length_1
    print('3 Row 1:', average_1)
    
    total_2 = sum(row_2)
    length_2 = len(row_2)
    average_2 = total_2 / length_2
    print('3 Row 2:', average_2)
    
def step4_function(x):
    return 4*x**2 + 7*x + 3

def step4_4():
    y = step4_function(A1)
    total = sum(y)
    length = len(y)
    average = total / length
    print('4:', average)
       
# step4_1(), step4_2(), step4_3(), step4_4()

