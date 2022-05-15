# Portuguese Version -- Versão em Português

import numpy as np # usado para trabalhar com matrizes, vetores e operações matemáticas
import matplotlib.pyplot as plt # usado para plotar gráfico


def funcao_analitica():
    # aqui é montada a função anítica escolhida
    x = np.linspace(0, 2, 1000)
    y = np.exp(x**4/4 - 1.5*x)
    
    # colocando para plotar
    plt.plot(x, y, 'r--', label = 'Analítica', linewidth=1)


def funcao_numerica(n):
    # configurando as bordas
    start = 0
    final = 2
    
    # calculando os passos
    h = (final-start)/n
    
    # configurando o eixo X
    x = np.linspace(start , final, n)

    # Criando a matriz A, e os vetores b e y
    A = np.zeros([n, n])
    b = np.zeros(n)
    y = np.zeros(n)

    # definindo os pontos conhecidos
    b[-1] = 2.72
    b[0] = 1
    y[1:] = 1 # valor que foi estipulado
    y[-1] = 2.72
    y[0] = 1

    # montando a matriz A
    for i in range(1, n-1):
        A[i, i+1] = 1
        A[i , i-1] = -1
    
    A[0,0] = 1
    A[n-1,n-1] = 1

    # CALCULANDO #
    for j in range(1000):
        for i in range(1, n-1):
            b[i] = 2 * h * y[i] * (x[i]**3 - 1.5)
        y = np.linalg.solve(A, b)

    u = np.matmul(np.linalg.inv(A), b)

    # colocando para plotar
    plt.plot(x, u, 'b', label = 'Numérica', linewidth=1)


# plotando as configurações com h difrente
# e por último mostra na tela

n = 10
for c in range(1, 4): # aqui conta de 1 -> 2 -> 3, parou antes de 4
    funcao_numerica(n**c)
    funcao_analitica()
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title(f'Exercício Lista 3: h = {n**c}')
    plt.legend(loc = 'upper left')
    plt.grid()
    plt.show()


