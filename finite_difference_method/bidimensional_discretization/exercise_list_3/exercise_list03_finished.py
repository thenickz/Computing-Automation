# english version

import numpy as np
import matplotlib.pyplot as plt

def analytic_function():
    # here goes the analytic function choosen
    x = np.linspace(0, 2, 1000)
    y = np.exp(x**4/4 - 1.5*x)
    
    # setting to plot
    plt.plot(x, y, 'r--', label = 'Analytic', linewidth=1)

def numeric_function(n):
    # setting the boundrys
    start = 0
    final = 2
    
    # calculating steps
    h = (final-start)/n
    
    # setting the x axis
    x = np.linspace(start , final, n)

    # creating the A matrix, b & y vectors
    A = np.zeros([n, n])
    b = np.zeros(n)
    y = np.zeros(n)

    # defining the knowing points
    b[-1] = 2.72
    b[0] = 1
    y[1:] = 1 # a value estimated
    y[-1] = 2.72
    y[0] = 1

    # setting the A matrix
    for i in range(1, n-1):
        A[i, i+1] = 1
        A[i , i-1] = -1
    
    A[0,0] = 1
    A[n-1,n-1] = 1

    # CALCULATING 
    for j in range(1000):
        for i in range(1, n-1):
            b[i] = 2 * h * y[i] * (x[i]**3 - 1.5)
        y = np.linalg.solve(A, b)

    u = np.matmul(np.linalg.inv(A), b)

    # setting to plotting
    plt.plot(x, u, 'b', label = 'Numeric', linewidth=1)

# ploting the configurations 3 times with difference h,
# then show
def plotting():
    n = 10
    for c in range(1, 4):
        numeric_function(n**c)
        analytic_function()
        plt.xlabel('Axis X')
        plt.ylabel('Axis Y')
        plt.title(f'Exercise List 3: h = {n**c}')
        plt.legend(loc = 'upper left')
        plt.grid()
        plt.show()

# this basically runs the code
if __name__ == '__main__':
    plotting()

