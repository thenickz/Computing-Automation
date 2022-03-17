import matplotlib.pyplot as plt 


# ex_3. Solve the following differential equation
# by the Euler method (Runge Kutta 1),
# with h = 0.5 and h = 0.25: Show both solutions in the same graph.

# setting 
h = 0.5
t_final = 2
n = int(t_final/h) + 1

# creating arrays full of zeros
t = [0 for _ in range(n)]
y = [0 for _ in range(n)]

# defining initial conditions
y[0] = 1
t[0] = 0

# Euler Method h = 0.5
for k in range(1, n):
    t[k] = t[k-1] + h
    y[k] = y[k-1] + h*(t[k-1]**2 - 2*y[k-1])
plt.plot(t, y, color='orange', label = 'Euler Method: h = 0.5', linestyle='dashdot')

# Euler Method h = 0.5
# reconfig variables
h = 0.25
n = int(t_final/h) + 1
t = [0 for _ in range(n)]
y = [0 for _ in range(n)]
t[0] = 0
y[0] = 1
for i in range(1, n):
    t[i] = t[i-1] + h
    y[i] = y[i-1] + h*(t[i-1]**2 - 2*y[i-1])

# plot graph
plt.xlabel('t axis')
plt.ylabel('y axis')
plt.title('Exercise 3')
plt.plot(t, y, color='blue', label = 'Euler Method: h = 0.25')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()
