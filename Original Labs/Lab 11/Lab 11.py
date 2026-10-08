# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 16:06:58 2025

@author: micha
"""

import pandas as pd
import scipy.stats as scistats
from statsmodels.stats.proportion import proportions_ztest
import matplotlib.pyplot as plt

def step_1():
    #Import all data
    rough_sm = pd.read_csv('roughness_smallsample.csv')
    
    #Seperate the two columns as different variables
    old_rough = rough_sm['Original Surface Roughness (um)']
    new_rough = rough_sm['New Surface Roughness (um)']
    
    #Null: The new has a greater roughness than the old
    t,p = scistats.ttest_ind(new_rough, old_rough, equal_var= False, alternative= 'less')
    print('P value that the old samples have a higher roughness than the new ones:', p)
    
def step_2():
    #Import larger data set
    rough_lg = pd.read_csv('roughness_largesample.csv')
    
    #Seperate the two columns as different variables
    old_rough_lg = rough_lg['Original Surface Roughness (um)']
    new_rough_lg = rough_lg['New Surface Roughness (um)']
    
    #Null: The new has a greater roughness than the old
    t,p = scistats.ttest_ind(new_rough_lg, old_rough_lg, equal_var= False, alternative= 'less')
    print('P value that the old samples have a higher roughness than the new ones:', p)

def step_3():
    #Import data about pens leaking
    pen_leaks = pd.read_csv('defects.csv')
    
    #Seperate the old and new pens: 0 means a leak, 1 means it works
    old_leaks = pen_leaks['Original']
    new_leaks = pen_leaks['New']
    
    #Sum the columns to find the number of successes in each brand of pen
    old_works = old_leaks.sum()
    new_works = new_leaks.sum()
    
    #Null: The old pens have a higher proportion of pens that leak
    z,p = proportions_ztest([old_works,new_works],[len(old_leaks),len(new_leaks)], value= 0, alternative= 'smaller')
    print(z,p)
    print('The chance that the proportion of failures is the same:', p)

def step_4():
    #Import data about how much ink discharge the old versus new ink cartridges produce
    ink = pd.read_csv('ink.csv')
            
    #Seperate the old and new ink cartridges
    old_ink = ink['Original Ink (ml)']
    new_ink = ink['New Ink (ml)']
    
    #Create a scatter plot with the information
    plt.xlabel('Pen ID')
    plt.ylabel('Ink Used (ml)')
    plt.xticks(ink['ID'])
    plt.grid(axis='x')
    plt.scatter(x= ink['ID'], y= ink['Original Ink (ml)'], marker= 'x', label= 'Old Cartridges')
    plt.scatter(x= ink['ID'], y= ink['New Ink (ml)'], marker= 'o', facecolor= 'none', edgecolors= 'orange', label= 'New Cartridges')
    plt.legend()
    
    #Null: The old pens use less ink than the new ones
    t,p = scistats.ttest_rel(old_ink, new_ink, alternative= 'less')
    print('P value that the old samples leak less than the new ones:', p)
