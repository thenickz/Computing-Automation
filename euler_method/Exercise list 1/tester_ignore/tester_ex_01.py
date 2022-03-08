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

# método de Euler
for k in range(1, n):
    t[k] = t[k-1] + h
    y[k] = y[k-1] + h*(y[k-1] * (t[k-1]**3 - 1.5))

# plotagem
ta = linspace(t[0], t_final, 1000) # tempo para solução analítica
ya = exp(((ta**4 - 6*ta)/4)) # solução analítica
plt.xlabel('Eixo t')
plt.ylabel('Eixo y')
plt.title('Exercício 1')
plt.plot(ta, ya, color='red', label = 'Analítico')
plt.plot(t, y, color='blue', label = f'Método de Euler: h = {h}')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()
