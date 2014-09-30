#loads a txt file with primes in it, and sums them
from numpy import loadtxt

a = loadtxt('/Users/joykimmel/Documents/College/Senior_Year/Python_Course/Simple_Programs/primes.txt', float)

sum = 0
for m in a:
    sum = sum + m

#sum = 2827.0    
print sum
