# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 11:06:16 2025

@author: micha
"""
import numpy as np
import scipy.stats as scistats

def prob_1():
    #Breaking strength in Newtons after heat treatment
    test60 = [43,52,52,58,49,52,41,52,56,54]
    test120 = [59,55,59,66,62,55,57,66,66,51]
    
    #Calculate a 99% confidence interval for the difference in between the means
    CI = scistats.ttest_ind(test60, test120).confidence_interval(.99)
    print('99% Confidence interval = [',CI.low, CI.high,']')
    
def prob_10():
    #Time for an ibuprofen tablet to dissolve in seconds based on shape
    disk = [269.0,249.3,255.2,252.7,247.0,261.6]
    oval = [268.8,260.0,273.5,253.9,278.5,289.4,261.6,280.2]
    
    #Calculate variances to see if we can use an equal variance test
    var1 = np.var(disk)
    var2 = np.var(oval)
    var_ratio = var2 / var1
    print('Using unequal variance is more accurate, as shown by this large variance ratio:', var_ratio)
    
    #Calculate probability the means are the same using an unequal variance model
    ttest2_result = scistats.ttest_ind(disk,oval, equal_var=False)
    print('\nP-value with unequal variance:', ttest2_result.pvalue)

def prob_2():
    #Breathing rates in breaths per minute of 10 subjects at rest and during excercise
    rest = [15,16,21,17,18,15,19,21,18,14]
    excercise = [30,37,39,37,40,39,34,40,38,34]
    
    CI = scistats.ttest_rel(rest,excercise).confidence_interval(0.95)
    print('95% Confidence interval = [',CI.low, CI.high,']')

def prob_9():
    '''I also did this problem on paper, but am turning in my code because everything is here'''
    
    #Miles for 80% of tread to wear off from two tire brands on the same 7 cars
    brand1 = [36925,45300,36240,32100,37210,48360,38200]
    brand2 = [34318,42280,35500,31950,38015,47800,33215]
    
    #State null and alternative hypotheses
    print('Null: There is no difference in the mean lifetimes of the two tire brands'
          '\nAlternative:There is a difference in the mean lifetimes of the two tire brands')
    
    #Calculate the probability of the mean being the same
    ttest_result = scistats.ttest_rel(brand1, brand2)
    print('Test statistic:', ttest_result[0])
    print('P-value:', ttest_result[1])
    
    #State results
    print('Conclusion: Because the p-value is not significant at the 0.05 level, we cannot'
          ' rejct the null hypothesis meaning we cannot say the means are different.')
