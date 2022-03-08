from numpy import exp, linspace
import matplotlib.pyplot as plt 


# ex_2. Solve the following differential equation analytically 
# and by the Euler method (Runge Kutta 1),
# with h = 0.5 and h = 0.25: Show both solutions in the same graph.

# setting 
h = 0.5
t_final = 1
n = int(t_final/h)

# creating arrays full of zeros
x = [0 for _ in range(n)]
y = [0 for _ in range(n)]

# defining initial conditions
y[0] = 1
x[0] = 0

# Euler Method  h = 0.5
for k in range(1, n):
    x[k] = x[k-1] + h
    y[k] = y[k-1] + h*((1 + 4*x[k-1]) * y[k-1]**(1/2))
plt.plot(x, y, color='orange', label = f'Euler Method: h = 0.5')

# Euler Method  h = 0.25

h = 0.25
n = int(t_final/h)
x = [0 for _ in range(n)]
y = [0 for _ in range(n)]
x[0] = 0
y[0] = 1

for i in range(1, n):
    x[i] = x[i-1] + h
    y[i] = y[i-1] + h*((4*x[i-1] + 1) * y[i-1]**(1/2))

# plot graph
xa = linspace(x[0], t_final, 1000) # x axis for analytical solution
ya = (xa**2 + xa**2/2 + 1)**2 # analytical solution
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Exercise 2')
plt.plot(xa, ya, color='Green', label = 'Analitic', linestyle='dotted')
plt.plot(x, y, color='blue', label = f'Euler Method: h = 0.25',  linestyle='dashdot')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()
