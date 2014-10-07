import numpy as np
import matplotlib.pylab as plt

#f(x)
def f(a):
    y = a**(3) - np.sin(a)
    
    return y
    
#f'(x)
def f_(a):  
    y_ = 3*a**(2) - np.cos(a)
    
    return y_
  
def foward_difference():
    
    h = 0.000001 #step size
    x = 2 #find the derivative at x = 2
    f_prime = (f(x + h) - f(x))/h #calculate f'(x) 
    error = (f_prime - f_(x))/(f_prime) #find the error
    
    return f_prime, error
    

def central_difference():
    
    h = 0.000001 #step size
    x = 2 #find the derivative at x = 2
    f_prime = (f(x+h/2.0) - f(x-h/2.0))/h #calculate f'(x)
    error = (f_prime - f_(x))/(f_prime) #find the error
    
    return f_prime, error

#function for euler's method ~ a = x, b = t
def dxdt(a,b):
    y = -a**(3) + a*np.sin(b) + 1
    
    return y
    
def eulers_method():
    x = 0
    t = 0
    
    a = 1.0
    b = 10.0
    N = 1000
    
    h = (b-a)/N 
    tarray = np.arange(a,b,h)
    xlist = []
    
    for i in tarray:
        xlist.append(x)
        x += h*dxdt(x,t)
        
    plt.plot(tarray, xlist)
    plt.xlabel('$t$')
    plt.ylabel('$x(t)$')
    plt.show()
 
print f_(2)  
print foward_difference()
print central_difference()
eulers_method()
