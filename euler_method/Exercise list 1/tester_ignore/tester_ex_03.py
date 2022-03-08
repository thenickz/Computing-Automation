import matplotlib.pyplot as plt 


 
h = 0.5
t_final = 2
n = int(t_final/h)

# criando arrays com zeros
t = [0 for _ in range(n)]
y = [0 for _ in range(n)]

# definindo condições inicias
y[0] = 1
t[0] = 0

# Método de Euler h = 0.5
for k in range(1, n):
    t[k] = t[k-1] + h
    y[k] = y[k-1] + h*(t[k-1]**2 - 2*y[k-1])
# plot 1
plt.plot(t, y, color='orange', label = 'Método de Euler: h = 0.5', linestyle='dashdot')

# Método de Euler h = 0.25
# reconfigurando variáveis
h = 0.25
n = int(t_final/h)
t = [0 for _ in range(n)]
y = [0 for _ in range(n)]
t[0] = 0
y[0] = 1
for i in range(1, n):
    t[i] = t[i-1] + h
    y[i] = y[i-1] + h*(t[i-1]**2 - 2*y[i-1])

# plotagem 2, gráfico todo
plt.xlabel('Eixo t')
plt.ylabel('Eixo y')
plt.title('Exercício 3')
plt.plot(t, y, color='blue', label = 'Método de Euler: h = 0.25')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()
