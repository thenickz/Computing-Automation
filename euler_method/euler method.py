from numpy import linspace
import matplotlib.pyplot as plt 

def f(function, x, y):
    return eval(function, {'x': x, 'y': y})


def euler_method(h, x0, x_end, fx_numeric, fx_analytical = None):

    n = int(x_end/h)

    # creating arrays full of zeros
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]

    #defining initial conditions
    x[0] = x0
    y[0] = 1
    
    # Euler Method
    for k in range(1, n):
        x[k] = x[k-1] + h
        y[k] = y[k-1] + h*(f(fx_numeric, x[k-1], y[k-1]))

    # plot graphs
    if fx_analytical != None:
        xa = linspace(x[0], x_end, 1000) # x axis for analytical solution
        ya = eval(fx_analytical) # analytical solution
        plt.plot(xa, ya, color='red', label = f'Analytical')
    
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('Exercise 1')    
    plt.plot(x, y, color='blue', label = f'Euler Method: h = {h}')
    plt.legend(loc = 'upper left')
    plt.grid()
    plt.show()


euler_method(0.5, 0, 1, '(1+4*x)*y**(1/2)', '(x**2+x/2+1)**(1/2)')

