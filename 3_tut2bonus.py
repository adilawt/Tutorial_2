### Tutorial2 Bonus
##
## The difference of the two Area can be seen integrating the function in to two parts, 
## like in this case the integration from -5 to 5 is 1st part from -5 to 3 and 2nd part 
## 3 to 5, Therefore, 1st integral is the sum of the two parts and the 2nd interation is
## just the 1st only
#  one can see from the resualts that the two areas are not the same. 
import numpy as np
import scipy.integrate as quad
def mygauss(x,cent=0,sig=0.1):
    return np.exp(-0.5*(x-cent)**2/sig**2)

print 'By integrating into two parts'
I,err=quad.quad(mygauss,-np.pi,np.pi) 
print 'Area = ', I
I1,err=quad.quad(mygauss,-np.pi,1)
print 'Area1 = ', I1
I2,err=quad.quad(mygauss, 1,np.pi)
print 'Area2 = ', I2
