from numpy import exp, linspace
import matplotlib.pyplot as plt 


# ex_1. Solve the following differential equation analytically 
# and by the Euler method (Runge Kutta 1),
# with h = 0.5 and h = 0.25: Show both solutions in the same graph.

# setting 
h = 0.5
t_final = 2
n = int(t_final/h)

# creating arrays full of zeros
t = [0 for _ in range(n)]
y = [0 for _ in range(n)]

#defining initial conditions
y[0] = 1
t[0] = 0

# Euler Method
for k in range(1, n):
    t[k] = t[k-1] + h
    y[k] = y[k-1] + h*(y[k-1] * (t[k-1]**3 - 1.5))

# plot graph
ta = linspace(t[0], t_final, 1000) # time axis for analytical solution
ya = exp(((ta**4 - 6*ta)/4)) # analytical solution
plt.xlabel('t axis')
plt.ylabel('y axis')
plt.title('Exercise 1')
plt.plot(ta, ya, color='red', label = 'Analitic')
plt.plot(t, y, color='blue', label = f'Euler Method: h = {h}')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()
