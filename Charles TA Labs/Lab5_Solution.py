import numpy as np
import scipy.integrate as scint
import matplotlib.pyplot as plt


# STEP 1 ---------------------------------------------------------------------
t, ax, ay, az, atot = np.loadtxt('rocking_baby.csv', unpack=True, \
                                 delimiter = ',', skiprows=1)

# Plot acceleration in different directions
plt.figure()
plt.plot(t,ax,label='ax')
plt.plot(t,ay,label='ay')
plt.plot(t,az,label='az')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s**2)')
plt.legend()
plt.show()

# Answers:  The z-axis mostly recorded the higher-frequency up-and-down bouncing,
#           whereas the x-axis mostly recorded the lower-frequency side-to-side swaying.
#           The y-axis is a combination.

# Compute and plot velocity and position in z-direction
# Deprecation note: we used to use scint.cumtrapz, but this has been replaced
# by scint.cumulative_trapezoid
vz = scint.cumulative_trapezoid(az,x=t,initial=0)
pz = scint.cumulative_trapezoid(vz,x=t,initial=0)

plt.figure()
plt.subplot(3,1,1)
plt.plot(t,pz)
plt.ylabel('z-displacement (m)')
plt.subplot(3,1,2)
plt.plot(t,vz)
plt.ylabel('z-velocity (m/s)')
plt.subplot(3,1,3)
plt.plot(t,az)
plt.xlabel('Time (s)')
plt.ylabel('z-acceleration (m/s**2)')
plt.show()

# Answers:  The large movement in the z-direction represents drift, which results
#           from integrating small amounts of sensor noise over many steps


# STEP 2 ---------------------------------------------------------------------
# Importing Image and ImageOps module from PIL package 
from PIL import Image, ImageOps

# Create image array
im = np.array([  [0,0,0,0] , [1,1,1,1] , [1,1,2,2]  ])

# Calculate gradient
grad = np.gradient(im)
grad_x = grad[1]
grad_y = grad[0]
grad_mag = np.sqrt(grad_x**2 + grad_y**2)

# Plot
plt.subplot(2,2,1)
plt.imshow(im, cmap='gray')
plt.subplot(2,2,2)
plt.imshow(grad_x, cmap='gray')
plt.subplot(2,2,3)
plt.imshow(grad_y, cmap='gray')
plt.subplot(2,2,4)
plt.imshow(grad_mag, cmap='gray')
plt.show()


# STEP 3 ---------------------------------------------------------------------
# Load image 
im = Image.open(r"Cosmo_Cougar.jpg") 
 
# Make image grayscale 
im = ImageOps.grayscale(im)

# Transform image into array
im_arr = np.array(im)

# Calculate gradient
grad = np.gradient(im_arr)
grad_x = grad[1]
grad_y = grad[0]
grad_mag = np.sqrt(grad_x**2 + grad_y**2)

# Plot
plt.figure()
plt.subplot(2,2,1)
plt.imshow(im_arr, cmap='gray')
plt.subplot(2,2,2)
plt.imshow(grad_x, cmap='gray')
plt.subplot(2,2,3)
plt.imshow(grad_y, cmap='gray')
plt.subplot(2,2,4)
plt.imshow(grad_mag, cmap='gray')
plt.show()