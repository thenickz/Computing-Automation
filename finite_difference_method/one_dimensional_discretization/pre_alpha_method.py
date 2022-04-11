import matplotlib.pyplot as plt
import numpy as np
# this method works, but i dont know how

def method(t, te, td, L, n, s, alpha, tot):
    
    dx = L/(n-1)
    dt = s*dx**2/alpha
    x = np.linspace(0, L, n+1)
    T = x * 0
    T[0] = te 
    T[n] = td

    while t <= tot:

        ta = T
        
        for i in range(1, n):
            T[i] = ta[i] + alpha*dx*(ta[i-1] - 2*ta[i] + ta[i+1])/dx**2
        
        t += dt
        plt.plot(x, T, 'blue', linewidth=0.4)
        
    plt.grid()
    plt.show()
