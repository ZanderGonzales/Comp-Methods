import numpy as np

#Define matrix with values of n,S,B,H
A= np.array([
             [0.035,0.0001,10,2.0],
             [0.020,0.0002,8,1.0],
             [0.015,0.0010,20,1.5],
             [0.030,0.0007,24,3.0],
             [0.022,0.0003,15,2.5]
            ])

print(f'A: {A}')

#Make each column a variable
n= A[:,0]
S= A[:,1]
B= A[:,2]
H= A[:,3]

#Equation to plug into
U = (S**(1/2) / n) * ((B * H)/ (B + 2 * H))**(2/3)

# Convert U to a column vector
U = U.reshape(-1, 1)  # or U = U[:, np.newaxis]

print(f'U: {U}')


#numerator1 = S**(1/2)
#denominator1 = n
#numerator2 = B*H
#denominator2 = B + 2*H

#U = numerator1/denominator1 * (numerator2/denominator2)**(2/3)
