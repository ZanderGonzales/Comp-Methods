# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 12:38:02 2025

@author: micha
"""
import numpy as np
'''Use Variable explorer to look at all arrays'''

#Lists or tuples aren't good for doing math
a = [1,2,3]
print('This is a list multiplied:', 3*a) #This doesn't give what we want

b = np.array([1,2,3])
print('This is an array multiplied:', 3*b) #This is better

c = np.array(a) #You can also cast lists as an array

print('Adding two arrays:', c+b) #Arrays can do element by element operations

A = np.array([a,b])
print('This takes smaller rows and makes them rows:\n', A)
A = np.array( [ [1,2,3] , [1,2,3] ] ) #Breakdown of syntax. Vertical is first (0th) dimension,
#horizontal is second
#You can also take a list and use it as a row in an array

column = np.array([ [1],[2],[3] ])
print('Coumn Vector:\n', column)

#Vertical stacking only takes a tuple as the main arguement, to allow for other arguments
vstacked = np.vstack((A,b))
print('Vertical stacking:\n', vstacked)
hstacked = np.hstack((A,A))
D = np.dstack((A,A))
print('Dimension stacking:\n', D)

#You can pull out multiple elements at once if you'd like, as an array
print('Pulling out array elements:\n', A[1,[0,2]]) #Putting -1 gives you the last element

#Left inclusive, right exclusive gives you elements in a row using a :
print('Right exclusive pulling:\n', hstacked[1,1:4]) #Leaving one or both sides empty starts
                                                     #at the first and goes to the last
                                                     
'''Linear Algebra Stuff from here on'''
#Addition and subtraction are simply element by element. To do multiplication you use @, but
#they must be compatible sizes
B = np.array( [ [2,4,6]  ,[8,10,12] ] )
#print(A@B), this doesn't work
print('Matrix multiplication:\n', A@np.transpose(B))

#Can do linear algebra stuff, like inverse
#print(np.linalg.inv(A[:,:2]))

#Or it can give you rank, or eigenvalues
square_matrix = np.array( [ [1,2] , [3,4] ] )
print('Matrix rank:\n', np.linalg.matrix_rank(square_matrix))
print('Eigenvalues/vectors:\n', np.linalg.eig(square_matrix))

#Can also solve using np.linalg.solve, with a matrix and column vector of answers
