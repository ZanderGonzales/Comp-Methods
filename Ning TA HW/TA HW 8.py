# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 16:22:41 2025

@author: micha
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# ---------- P1 ----
data_m = np.genfromtxt('male_ansur.csv', delimiter=',', names=True, encoding='ISO-8859-1')
data_f = np.genfromtxt('female_ansur.csv', delimiter=',', names=True, encoding='ISO-8859-1')
knee_m = data_m["kneeheightmidpatella"]
stature_m = data_m["stature"]
knee_f = data_f["kneeheightmidpatella"]
stature_f = data_f["stature"]

# combine male and female data
knee = np.concatenate((knee_m, knee_f))
stature = np.concatenate((stature_m, stature_f))

# histogram
plt.figure()
plt.hist(knee, bins=30)
plt.xlabel("knee height (mm)")
plt.ylabel("frequency")

# split into sizes
subset = knee[(knee >= 425) & (knee <= 550)]
a = np.percentile(subset, 25)
b = np.percentile(subset, 50)
c = np.percentile(subset, 75)

print("size1 = ", 425, "to", a)
print("size2 = ", a, "to", b)
print("size3 = ", b, "to", c)
print("size4 = ", c, "to", 550)

# least square fit
A = np.column_stack((stature, np.ones_like(stature)))
coeff, _, _, _ = np.linalg.lstsq(A, knee, rcond=None)
x = np.linspace(np.min(stature), np.max(stature), 200)
y = coeff[0]*x + coeff[1]

plt.figure()
plt.plot(stature, knee, ".")
plt.plot(x, y, "k--")
plt.xlabel("person height (mm)")
plt.ylabel("knee height (mm)")

# correlation coefficient
print("r = ", pearsonr(stature, knee).statistic)

plt.show()