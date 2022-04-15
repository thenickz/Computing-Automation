import matplotlib.pyplot as plt
import numpy as np

# not working yet
tb = 20
tt = 100
te = 30
td = 30
ti = 25
L = 1
alpha = 0.0155
n = 5
dx = L/(n-1)
dy = L/(n-1)
s = 1/20 # 1/tb?
dt = s/(alpha*(1/dx**2 + 1/dy**2))
x = np.linspace(0, L, n+1)
tot = 10



T = np.ones([n+1, n+1]) * ti
T[1:n,1] = te
T[0, 1:n] = tb
T[1:n, n] = td
T[n, 1:n] = tt
t = 0
k = 0
while t <= tot:
    T0 = T
    for i in range(1, n):
        for j in range(1, n):
            T[i, j] = T0[i, j] + dt*alpha*((T0[i-1, j] - 2*T0[i, j] + T0[i+1, j])/dx**2 + (T0[i, j-1] - 2*T0[i, j] + T0[i, j+1])/dy**2)
    t += dt
    
plt.plot(x,)
plt.grid()
plt.show()

tf = T[1:n, 1:n]
print(tf)
plt.plot(tf)
plt.grid()
plt.show()