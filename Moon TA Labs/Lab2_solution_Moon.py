import numpy as np
import matplotlib.pyplot as plt


# STEP 1: ROUND-OFF ERROR
n = 15

pi_error = np.zeros(n+1)
for i in range(n+1):
    pi_approx = round(np.pi,i)
    pi_error[i] = abs( (np.pi - pi_approx) / np.pi )*100

plt.semilogy(np.arange(0,n+1,1), pi_error, marker='o')
plt.xlabel('Number of decimal places, n')
plt.ylabel('Approximation of pi')


# STEP 2: TRUNCATION ERROR
N = 20

# Leibniz approximation
Leibniz_approx = 0
Leibniz_error = np.zeros(N+1)
for k in range(N+1):
    Leibniz_approx = Leibniz_approx + ((-1)**k) / (2*k + 1)
    Leibniz_error[k] = abs( (np.pi - 4*Leibniz_approx) / np.pi )*100
     
# Wallis approximation (OPTIONAL)
Wallis_approx = 1
Wallis_error = np.zeros(N+1)
Wallis_error[0] = np.nan
for k in np.arange(1,N+1,1):
    Wallis_approx = Wallis_approx * (2*k/(2*k-1) * 2*k/(2*k+1))
    Wallis_error[k] = abs( (np.pi - 2*Wallis_approx) / np.pi )*100
    
# Plot
plt.figure()
plt.scatter(np.arange(0,N+1,1), Leibniz_error, marker='.', label='Leibniz')
plt.scatter(np.arange(0,N+1,1), Wallis_error, marker='.', label='Wallis')   # OPTIONAL
plt.xlabel('Number of highest term included, N')
plt.ylabel('Approximation of pi')
plt.legend(loc='upper right')


