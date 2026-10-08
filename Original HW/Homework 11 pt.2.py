# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:00:13 2025

@author: micha
"""

import numpy as np
import matplotlib.pyplot as plt

def prob22_8_euler(h, t_max):
    t = np.arange(0, t_max + h, h)
    n = len(t)
    
    y_values = np.zeros(n)
    v_values = np.zeros(n)
    
    y_values[0] = 1  # y(0) = 1
    v_values[0] = 1  # v(0) = dy/dt(0) = 1
    

    for k in range(n - 1):
        y = y_values[k]
        v = v_values[k]
        
        dy_dt = v
        dv_dt = (1 - y**2) * v - y
        
        y_values[k + 1] = y + h * dy_dt
        v_values[k + 1] = v + h * dv_dt
    
    return t, y_values

t_02, y_02 = prob22_8_euler(h=0.2, t_max=10)
t_01, y_01 = prob22_8_euler(h=0.1, t_max=10)

plt.plot(t_02, y_02, label="h = 0.2")
plt.plot(t_01, y_01, label="h = 0.1")

plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Euler's Method")
plt.legend()
plt.grid()
plt.show()
