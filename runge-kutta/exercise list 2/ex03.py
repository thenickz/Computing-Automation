import matplotlib.pyplot as plt


def function_ex3(t, y):
    return t**2 - 2*y


# resolvendo agora para runge kutta 2

# primeiro com h valendo 0.5
h1 = 0.5
t_final = 2
n1 = int(t_final/h1) + 1

# criando os arrays de zeros
t1 = [0 for _ in range(n1)]
y1 = [0 for _ in range(n1)]

# definindo condições iniciais
y1[0] = 1
t1[0] = 0

# método de runge kutta 2 para h de 0.5
for k in range(1, n1):
    t1[k] = t1[k-1] + h1 
    k1 = function_ex3(t1[k-1], y1[k-1])
    k2 = function_ex3(t1[k-1] + h1, y1[k-1] + h1*k1)
    y1[k] = y1[k-1] + h1*(k1 + k2)/2

# agora preparar para plotar no gráfico o que foi calculado
# na cor vermelha
plt.plot(t1, y1, color='red', label = 'runge kutta 2 para h= 0.5')

# agora com h valendo 0.25, configurando novas variáveis
h2 = 0.25
t_final = 2
n2 = int(t_final/h2) + 1

# criando os arrays de zeros
t2 = [0 for _ in range(n2)]
y2 = [0 for _ in range(n2)]

# definindo condições iniciais
y2[0] = 1
t2[0] = 0

# método de runge kutta 2 para h de 0.25
for k in range(1, n2):
    t2[k] = t2[k-1] + h2 
    k1 = function_ex3(t2[k-1], y2[k-1])
    k2 = function_ex3(t2[k-1] + h2, y2[k-1] + h2*k1)
    y2[k] = y2[k-1] + h2*(k1 + k2)/2

# agora preparar para plotar no gráfico o que foi calculado
# na cor azul e pontilhado
plt.plot(t2, y2, 'o', label = 'runge kutta 2 para h= 0.25', linestyle = 'dotted')

# plotando os runge kuttas 2 que foram calculados.
plt.xlabel('Eixo t')
plt.ylabel('Eixo y')
plt.title('Exercício 3')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()

#################################
# agora fazendo com runge kutta 4

# para h de 0.5
h3 = 0.5
t_final = 2
n3 = int(t_final/h3) + 1

# criando os arrays de zeros
t3 = [0 for _ in range(n3)]
y3 = [0 for _ in range(n3)]

# definindo condições iniciais
t3[0] = 0
y3[0] = 1 

# método de runge kutta 4 para h de 0.5
for k in range(1, n3):
    t3[k] = t3[k-1] + h3
    k1 = h3*function_ex3(t3[k-1], y3[k-1])
    k2 = h3*function_ex3(t3[k-1] + h3/2, y3[k-1] + k1/2)
    k3 = h3*function_ex3(t3[k-1] + h3/2, y3[k-1] + k2/2)
    k4 = h3*function_ex3(t3[k-1] + h3, y3[k-1] + k3)
    y3[k] = y3[k-1] + (k1 + 2*k2 + 2*k3 + k4)/6
    
# agora preparar para plotar no gráfico o que foi calculado
# na cor vermelho
plt.plot(t3, y3, color='red', label = 'runge kutta 4 para h= 0.5')

# para h de 0.25
h4 = 0.25
t_final = 2
n4 = int(t_final/h4) + 1

# criando os arrays de zeros
t4 = [0 for _ in range(n4)]
y4 = [0 for _ in range(n4)]

# definindo condições iniciais

t4[0] = 0
y4[0] = 1 
# método de runge kutta 4 para h de 0.25
for k in range(1, n4):
    t4[k] = t4[k-1] + h4
    k1 = h4*function_ex3(t4[k-1], y4[k-1])
    k2 = h4*function_ex3(t4[k-1] + h4/2, y4[k-1] + k1/2)
    k3 = h4*function_ex3(t4[k-1] + h4/2, y4[k-1] + k2/2)
    k4 = h4*function_ex3(t4[k-1] + h4, y4[k-1] + k3)
    y4[k] = y4[k-1] + (k1 + 2*k2 + 2*k3 + k4)/6

# agora preparar para plotar no gráfico o que foi calculado
# na cor azul e pontilhada
plt.plot(t4, y4, 'bo', label = 'runge kutta 4 para h= 0.25', linestyle='dotted')

# plotando os runge kuttas 4 que foram calculados.
plt.xlabel('Eixo t')
plt.ylabel('Eixo y')
plt.title('Exercício 3')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()
