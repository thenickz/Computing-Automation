import numpy as np 
import matplotlib.pyplot as plt 


def f(x):
    return x**2 + 2*x*(x+1)


def func(x, y):
    return y + x


def Euler_Method(func, y0, x0, b, n):
    
    h = (b - x0)/n
    
    x = x0
    yi = y0 + h*func(x,y0)
    #print("Para a iteração " + str(0) + ", resulta em "+ str(yi))
    xi = x0+h
    
    for i in range(1,n):
        xi = xi + h
        yi = yi + h*(func(xi,yi))
        #print("Para a iteração " + str(i+1) + ", resulta em "+ str(yi))

    return yi

print(Euler_Method(1, 2, 3, 4, 5))