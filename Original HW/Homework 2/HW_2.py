import numpy as np
#HOMEWORK 2, P3.6


def polar2cart(): #3.6.1
    '''Takes a radius and a radian value and then gives the cartesian coords'''
    r = float(input("Radius: ")) #Get a radius
    theta = float(input("Radians: ")) #Get a theta value
    
    x = r*np.cos(theta) #Convert polar to cartesian
    y= r*np.sin(theta)
    
    print(f'{x},{y}') #Print the cartesian coordinates
    
def cart2polar(): #3.6.2
    '''Takes an x and y value and gives the polar coords'''
    x = float(input('X: ')) #Get an x coordinate
    y = float(input('Y: ')) #Get a y coordinate
    
    r = (x**2 + y**2)**.5 #Convert cartesian to polar
    theta = np.atan2(y,x)
    
    print(f'{r},{theta}') #Print the polar coordinates


def polar2cartarray(): #3.7.1
    '''Takes an array of polar coordinates and gives an array of carestians coordinates'''
    polar_arr = np.array([[1,1],[3,4],[1,2]])
    
    r = polar_arr[:,0] #Seperate different variables as vectors
    theta = polar_arr[:,1]
    
    x = r*np.cos(theta) #Convert polar to cartesian
    y= r*np.sin(theta)
    
    cartesian_arr = np.column_stack((x,y))
    print(cartesian_arr)
     
def cart2polararray(): #3.7.1
    '''Takes an array of cartesian coordinates and gives an array of polar coordinates'''
    cart_arr = np.array([[1,1],[3,4],[1,2]])
    
    x = cart_arr[:,0] 
    y = cart_arr[:,1]
    
    r = (x**2 + y**2)**.5 #Convert cartesian to polar
    theta = np.atan2(y,x)
    
    polar_arr = np.column_stack((r,theta))
    print(polar_arr)
