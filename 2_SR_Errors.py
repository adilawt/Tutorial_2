## Tutorial2 Question4a
## 4a)Plot the error as a function of #of points using Simpson's Rule and Standard sum
#
## Error is defined by abs(Exact-Experment), the exact vale is Area = 1 and the Experment comes from 
## Simpson's Rule integiration and the Standard sum.
#
import numpy as np 
from matplotlib import pyplot as plt 
A = (1.0,1.0,1.0,1.0,1.0) # This is exact Aear should be each time
n = (10,30,100,300,1000)  # This is the number of spacings
Axs = (1.05236326978,1.01745333429, 1.00523598809, 1.00174532926, 1.00052359878) # This is the Area using Simpson's Rule
Axi = (1.0764828026941022, 1.025951465275319, 1.0078334198735821, 
1.0026157092462991, 1.0007851925466307) # This is the Area using standard sum
Es = abs(np.subtract(Axs,A))
Ei = abs(np.subtract(Axi,A))

plt.plot(n,Es,color='b')
plt.plot(n,Ei,color='r')
ax=plt.gca()
ax.set_yscale('log')
plt.title('Error as a function of #points')
plt.grid(True)
plt.show()

