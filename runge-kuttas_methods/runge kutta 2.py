import matplotlib.pyplot as plt 
from numpy import linspace

#how to use: put the fn(x, y) the values to calculate what you will need from your ODE
def fn(x, y):
    # put your own ODE after return
    return y*(x**3) - (1.5*y)


def runge_kutta_2(h, y0 ,x0, x_end):
    '''h = "times it will run" (i dont exactly know what the hell happens here)
    y0 = inicial condition
    x0 = first coordenate
    x_end = last coordenate'''
    n = int(x_end/h) + 1

    # creating arrays full of zeros
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]

    #defining initial conditions
    x[0] = x0
    y[0] = y0
    
    # Runge Kutta 2 method
    for k in range(1, n):
        x[k] = x[k-1] + h 
        k1 = fn(x[k-1], y[k-1])
        k2 = fn(x[k-1] + h, y[k-1] + h*k1)
        y[k] = y[k-1] + h*(k1 + k2)/2

    # plot graphs
    plt.plot(x, y, 'r--o', label = f'Runge Kutta 2 for h={h}')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title('Runge Kutta 2 Graph')    
    plt.legend(loc = 'upper left')
    plt.grid()
    plt.show()
