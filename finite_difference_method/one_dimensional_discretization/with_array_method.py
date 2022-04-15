import numpy as np
import matplotlib.pyplot as plt
# this method works, but i dont know how

a = 0
b = 1
n = 11
h = (b-a)/(n-1)
x = np.linspace(a , b, n)
A = np.zeros([n, n])
b = np.zeros(n)
A[0,0] = 1
b[0] = 5

for i in range(1, n):
    A[i, i] = 1
    A[i , i] = -1
    b[i] = 10 * h * (x[i] - 1)

A[n-1,n-1] = 1
b[n-1] = 0
u = np.flipud(A/b)

xx = np.linspace(0, 1)
yy = 5*(xx - 1)**2



plt.plot(x, u, 'o')
plt.ylim([-1, 6])
plt.plot(xx, yy, 'red', linewidth=0.4)
plt.grid()
plt.show()