# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 12:00:16 2025

@author: micha
"""

import pandas as pd
import scipy.stats as scistats
import matplotlib.pyplot as plt
import seaborn as sns
#-----------------------------------Get Data---------------------------------------------#

#Read in the data from Kaggle
data = pd.read_csv('Groundhog_data.csv')

#Filter data that doesn't have temperatures
df = data[data['February Average Temperature'].notna()]
df = df[df['Year'] != '1901-2000']
df = df[df['Punxsutawney Phil'].isin(['Full Shadow', 'No Shadow'])]

#Split it into whether he saw his shadow or not
winter_df = df[df['Punxsutawney Phil'] == 'Full Shadow']
spring_df = df[df['Punxsutawney Phil'] == 'No Shadow']

#------------------------------Qualitative descriptions----------------------------------#

#Create violin plots for all the years, when he did see his shadow, and when he didn't see his shadow
fig, ax = plt.subplots(ncols = 3, sharey= True)

sns.violinplot(data= df, y= 'February Average Temperature', ax= ax[0], color= 'grey', inner= 'quart')
ax[0].set_title("All Years")
sns.violinplot(data= winter_df, y= 'February Average Temperature', ax= ax[1], inner= 'quart')
ax[1].set_title("Full Shadow")
sns.violinplot(data= spring_df, y= 'February Average Temperature', ax= ax[2], color= 'orange', inner= 'quart')
ax[2].set_title("No Shadow")

#Find sample size, mean, and standard deviation for all the data sets
ss_all = len(df['Year'])
mu_all = df['February Average Temperature'].mean()
std_all = df['February Average Temperature'].std()

ss_winter = len(winter_df['Year'])
mu_winter = winter_df['February Average Temperature'].mean()
std_winter = winter_df['February Average Temperature'].std()

ss_spring = len(spring_df['Year'])
mu_spring = spring_df['February Average Temperature'].mean()
std_spring = spring_df['February Average Temperature'].std()

#-------------------------Find if mean difference is significant overall-----------------#

winter_diff = scistats.ttest_ind(a= winter_df['February Average Temperature'], b= df['February Average Temperature'], alternative='less', equal_var=False)
winter_ci = scistats.ttest_ind(a= winter_df['February Average Temperature'], b= df['February Average Temperature'], alternative='less', equal_var=False).confidence_interval()
print('Probability that the mean temperature is greater than or the same as normal if he does not see his shadow:', winter_diff.pvalue)
print('Winter CI: [', winter_ci.low, winter_ci.high,']')

spring_diff = scistats.ttest_ind(a= spring_df['February Average Temperature'], b= df['February Average Temperature'], alternative='greater', equal_var=False)
spring_ci = scistats.ttest_ind(a= spring_df['February Average Temperature'], b= df['February Average Temperature'], alternative='greater', equal_var=False).confidence_interval()
print('\nProbability that the mean temperature is less than or the same as normal if he sees his shadow:', spring_diff.pvalue)
print('Spring CI: [', spring_ci.low, spring_ci.high,']')