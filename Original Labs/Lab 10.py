# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 15:53:29 2025

@author: micha
"""

import pandas as pd
import numpy as np
import scipy.stats as scistats

#Military Personnel statistics
army_stats = pd.read_csv('male_ansur_heightandweight.csv')

army_mu_height = np.mean(army_stats.Heightin) #in, Average military personnel height
army_mu_weight = np.mean(army_stats.Weightlbs) #lbs, Average military personnel weight

#General population statistics
gen_mu_height = 69 #in, Average general height
gen_mu_weight = 199.8 #lbs, Average general weight


def step_1():
    #Test for if the mean army height and mean general height are the same (H0)
    test_result_h = scistats.ttest_1samp(  a = army_stats.Heightin, popmean = gen_mu_height)
    print('Probability the means are the same:', test_result_h.pvalue)
    
    #Test for if the mean army weight is greater than or equal to the mean general weight (H0)
    test_result_w = scistats.ttest_1samp(a = army_stats.Weightlbs, popmean = gen_mu_weight, alternative = 'less')
    print('Probability the mean is greater than the general population mean:', test_result_w.pvalue)

def step_2():
    army_samp = [215, 174, 200, 170, 211, 190, 153, 194, 149, 200, 168, 180, 235, 195, 170, 200, 195, 223, 162, 165]

    #Test for if the sample mean army weight is greater than or equal to the mean general weight (H0)
    test_result_w = scistats.ttest_1samp(a = army_samp, popmean = gen_mu_weight, alternative = 'less')
    print('T statistic the sample mean is greater than the general population mean:', test_result_w.statistic)
    print('Probability the sample mean is greater than the general population mean:', test_result_w.pvalue)
    samp_mu = np.mean(army_samp)
    
# def step_3():
#Swedish army statistics
swede_stats = pd.read_csv('hypo_swedish_height_inches.csv')

#Proportion of 
po = 0.1

taller = swede_stats[swede_stats.Heights > 74]
p = len(taller) / len(swede_stats.Heights)

#Calculate p-value that the proportion is less than or equal to 0.1
z = (p - po) / np.sqrt(po*(1-po)/len(swede_stats.Heights))
p_val = 1 - scistats.norm.cdf(z)
print('Z-statistic that the proportion of Swedes with a height less than 74in is less than or equal to 0.1:', z)
print('P-value that the proportion of Swedes with a height less than 74in is less than or equal to 0.1:', p_val)
