import matplotlib.pyplot as plt
import numpy as np
Te = 0
Td = 100
L = 1
n = 6
s = 1/20
alpha = 0.0834
T_total = 4
dx = L/(n-1)
dt = s*dx**2/alpha
t = 0
x = np.linspace(0, L, n+1)
T = x * 0
T[0] = Te
T[n] = Td

while t <= T_total:
    Ta = T
    for i in range(1, n):
        T[i] = Ta[i] + alpha * dx * (Ta[i-1] - 2 * Ta[i] + Ta[i+1])/(dx**2)
    plt.plot(x, T, 'blue', linewidth=0.4)
    t += dt

plt.grid()
plt.show()
