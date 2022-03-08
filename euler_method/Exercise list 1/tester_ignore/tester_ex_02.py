from numpy import linspace
import matplotlib.pyplot as plt 

h = 0.5
t_final = 1
n = int(t_final/h)

# criando arrays de zeros
x = [0 for _ in range(n)]
y = [0 for _ in range(n)]

#definindo condições iniciais
y[0] = 1
x[0] = 0

# methodo de euler para h=0.5
for k in range(1, n):
    x[k] = x[k-1] + h
    y[k] = y[k-1] + h*((1 + 4*x[k-1]) * y[k-1]**(1/2))
# plot 1
plt.plot(x, y, color='orange', label = 'Método de Euler: h = 0.5')

# methodo de euler para h=0.25
# reconfigurando variáveis 
h = 0.25
n = int(t_final/h)
x = [0 for _ in range(n)]
y = [0 for _ in range(n)]
y[0] = 1
x[0] = 0
for i in range(1, n):
    x[i] = x[i-1] + h
    y[i] = y[i-1] + h*((4*x[i-1] + 1) * y[i-1]**(1/2))

# plotagem 2, gráfico todo
xa = linspace(x[0], t_final, 1000) # x axis for analytical solution
ya = (xa**2 + xa**2/2 + 1)**2 # analytical solution
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Exercício 2')
plt.plot(xa, ya, color='Green', label = 'Analítica', linestyle='dotted')
plt.plot(x, y, color='blue', label = 'Método de Euler: h = 0.25', linestyle='dashdot')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()