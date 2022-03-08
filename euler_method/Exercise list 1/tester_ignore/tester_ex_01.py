from numpy import exp, linspace
import matplotlib.pyplot as plt 


h = 0.5
t_final = 2
n = int(t_final/h)

# criando os arrays de zeros
t = [0 for _ in range(n)]
y = [0 for _ in range(n)]

#definindo condições iniciais
y[0] = 1
t[0] = 0

# método de Euler para h = 0.5
for k in range(1, n):
    t[k] = t[k-1] + h
    y[k] = y[k-1] + h*(y[k-1] * (t[k-1]**3 - 1.5))
# plot
plt.plot(t, y, color='orange', label = f'Método de Euler: h = 0.5')

# método de Euler para h = 0.25
# reconfigurando variáveis
h = 0.25
t_final = 2
n = int(t_final/h)
t = [0 for _ in range(n)]
y = [0 for _ in range(n)]
y[0] = 1
t[0] = 0
for i in range(1, n):
    t[i] = t[i-1] + h
    y[i] = y[i-1] + h*(y[i-1] * (t[i-1]**3 - 1.5))


# plotagem inteira
ta = linspace(t[0], t_final, 1000) # tempo para solução analítica
ya = exp(((ta**4 - 6*ta)/4)) # solução analítica
plt.xlabel('Eixo t')
plt.ylabel('Eixo y')
plt.title('Exercício 1')
plt.plot(ta, ya, color='red', label = 'Analítico', linestyle='dotted')
plt.plot(t, y, color='blue', label = 'Método de Euler: h = 0.25', linestyle='dashdot')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()
