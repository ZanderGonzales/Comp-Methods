# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 14:05:19 2025

@author: micha
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def step_1():
    file = 'Fremont_weather.txt'
    df = pd.read_csv(file)
    
    #1
    print('dtypes:\n', df.dtypes)
    
    #2
    print('\nColumns:\n', df.columns)
    
    #3
    print('\nDescribe:\n', df.describe())
    
    #4
    print('\nSorted Record Highs:\n', df.sort_values('record_high', ascending=True))
    
    #5
    print('\nAverage Low:\n', df.avg_low)
    
    #6
    print('\nThird and Fourth Row:\n', df[2:4])
    
    #7
    print('\nAverage High and Low:\n', df[['avg_low', 'avg_high']])
    
    #8
    print('\nAverage precipitation of month 10:\n', df.loc[9,['avg_precipitation']])
    
    #9
    print('\nAll months with average precipitation over 1 inch:\n', df[df.avg_precipitation > 1.0])
    
    #10
    df['avg_day'] = (df.avg_low + df.avg_high) / 2
    print('\nCreated an average day column:\n', df)
    
    #Average Temp Range
    df['avg_temp_range'] = (df.avg_high - df.avg_low)
    print('\nCreated an average temperature range column:\n')
    print(df.sort_values('avg_temp_range', ascending=False))

def ansur_questions():
    #Import male and female data
    fdata = pd.read_csv('female_ansur.csv')
    mdata = pd.read_csv('male_ansur.csv', encoding = 'iso8859_15')
    
    #Combine the two data sets
    frames = [mdata, fdata]
    df = pd.concat(frames) 
    
    #Plot all data for knee height on a histogram
    hist = df.kneeheightmidpatella.hist()
    hist.set_xlabel('Knee hight (mm)')
    hist.set_ylabel('Number of people')
    
    
    #Create a dataset with only heights between 425 and 550
    new_df = df[df.kneeheightmidpatella < 550]
    new_df = new_df[new_df.kneeheightmidpatella > 425]
    
    #Pull out all four quartiles
    bottom = 425.0
    quart1 = np.quantile(new_df.kneeheightmidpatella, 0.25)
    quart2 = np.quantile(new_df.kneeheightmidpatella, 0.5)
    quart3 = np.quantile(new_df.kneeheightmidpatella, 0.75)
    quart4 = np.quantile(new_df.kneeheightmidpatella, 1.0)
    top = 550.0
    boundaries = [bottom, quart1, quart2, quart3, quart4, top]
    
    #Find averages
    i = 0
    average = []
    
    #Adds the top of the last quartile and the current one and then divide by 2,
    #giving an average
    for value in np.arange(len(boundaries)-2):
        average.append( ( boundaries[i] + boundaries[i+1] ) / 2 )
        i += 1
        
        
    #Plot knee height versus height
    plt.figure()
    plt.scatter(df.kneeheightmidpatella, df.Heightin)
    plt.xlabel('Knee height (mm)')
    plt.ylabel('Total height (in)')
    plt.grid()
    
    #Plot least-squares line
    x = df.kneeheightmidpatella
    least_squares = np.polyfit(df.kneeheightmidpatella,df.Heightin,1)
    plt.plot(x, (least_squares[0]*x + least_squares[1]), color = 'orange', label = 'Least-Squares Line')
    plt.legend()

ansur_questions()