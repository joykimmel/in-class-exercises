#trapazoidal rule and simpsons rule
def f(x):
    return ((x**4) - 2*(x**2) - 1)
    
N = 10000
a = 0.0
b = 2.0

step = (b-a)/N
S = 0.5*f(a) + 0.5*f(b)

for i in range(1,N):
    new_x = a + i*step
    S += f(new_x)
    
S = step*S

print S


n = 10000
st = (b-a)/n
SS = f(a) + f(b)

for j in range(1,n):
    new = a + j*st
    
    if j%2 == 1:
        SS = SS+ 4.0*f(new)
    
    else:
        SS = SS+ 2.0*f(new)
    
SS = st* (SS/3.0)
print SS

real = -14.0/15.0
print real

error1 = real - S
error2 = real - SS

print "error 1: %s" % (error1)
print "error 2: %s" % (error2)

print "error subtraction %s" % ((S - SS)/15.0)
