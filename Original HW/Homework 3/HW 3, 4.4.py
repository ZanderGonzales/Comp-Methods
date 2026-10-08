# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:23:08 2025

@author: micha
"""
import numpy as np

true_eps = np.finfo(float).eps

def calculate_eps():
    eps = 1
    while True:
        if 1 + eps <= 1:
            eps = 2*eps
            break
        else: eps = eps / 2
    return eps
        
print(calculate_eps(),true_eps)