import numpy as np
import pylab

x = np.arange(0 , np.pi / 2 , np.pi / 40)

y = 5*np.exp(-2*x)*np.sin(5*x)*(0.0012*x**4-.15*x**3+.075*x**2+(2.5*x))

print(f"x: {x}")
print(f'y: {y}')

z = y**2

print(f'z: {z}')

pylab.plot(x,y,label='Y')

pylab.plot(x,z,ls ='--',c='m',label='Z')

pylab.title('Y vs Z')

pylab.xlabel('X')

pylab.ylabel('Outpot')

pylab.grid()

pylab.legend(loc='lower right')