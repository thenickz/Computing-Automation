import matplotlib.pyplot as plt 
from numpy import linspace

def fn(x, y):
    return (1 + 4*x) * y**(1/2)


def fa(x):
    return (x**2 + x/2 + 1)**(1/2)


def euler_method(h, y0 ,x0, x_end):
    '''h = times it will run
    y0 = inicial condition
    x0 = first coordenate
    x_end = last coordenate'''
    n = int(x_end/h)

    # creating arrays full of zeros
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]

    #defining initial conditions
    x[0] = x0
    y[0] = y0
    
    # Euler Method
    for k in range(1, n):
        x[k] = x[k-1] + h
        y[k] = y[k-1] + h*(fa(x[k-1], y[k-1]))

    # plot graphs
    xa = linspace(x[0], x_end, 1000) # x axis for analytical solution
    ya = fn(xa, 0) # analytical solution
    plt.plot(xa, ya, color='red', label = f'Analytical')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('Exercise 1')    
    plt.plot(x, y, color='blue', label = f'Euler Method: h = {h}')
    plt.legend(loc = 'upper left')
    plt.grid()
    plt.show()


euler_method(0.5, 1, 0, 1)
