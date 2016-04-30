#
##   Tutorial2 Question3
## a) Write a python function to integrate the vector(in question #2) using
##   Simpson's Rule
#
import numpy as np
def simpsonsrule(f, x0, xf, n):
   
    if n & 1:
       print ("Error: n is not a even number.")
       return 0.0
    h = float(xf - x0) / n
    integral = 0.0

    x = float(x0)
    for i in range(0, n / 2):
        integral += f(x) + (2.0 * f(x + h))
        x += 2 * h

    integral = (2.0 * integral) - f(x0)+f(x0)
    integral = h * integral / 3.0
    return integral

def f(x): 
    #f(x) = np.cos(x)
    return np.cos(x)
  

x0=0.0; xf=np.pi/2
N = (10,30,100,300,1000)
for n in N:
    print(simpsonsrule(f, x0, xf, n))
