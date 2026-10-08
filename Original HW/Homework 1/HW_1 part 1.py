import numpy as np
import matplot.pyplot as plt


#Goal, plot y=sqrt(x) for x = 0, 0.01, 0.02, … , 5
#Method 1: Start with empty variables and append to them
x_arr = []
y_arr = []

x_arr_size = round((5-0)/0.01 + 1) #Need to round so it turns into an integer

for i in range(x_arr_size): #This loops through every integer from 0 to 501-1
    x = 0.01*i
    x_arr = np.append(x_arr, x)
    y_arr = np.append(y_arr, np.sqrt(x))
    
plt.scatter(x_arr, y_arr)
plt.show
